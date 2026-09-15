---
title: "FPGA Design Optimization using Genetic Algorithms"
collection: projects
excerpt: "Automating High-Level Synthesis (HLS) design space exploration using a custom, constraint-aware genetic algorithm on a non-convex, integer-boolean search space."
venue: "CMPE583 (Reconfigurable Computing) Term Project"
date: 2023-06-05
description: "Course term project: framing FPGA high-level-synthesis design space exploration as constrained integer-boolean optimization, and solving it with a genetic algorithm that oscillates along the LUT resource boundary."
---

Design parameter optimization in FPGA programming is a **non-convex, high-dimensional, integer-boolean optimization problem**. Because closed-form mathematical solutions do not exist for compiler-driven hardware generation, industrial FPGA designs are traditionally tuned through trial, error, and designer intuition. 

In this project, developed with **Ilgaz Er** for *CMPE583: Reconfigurable Computing* (taught by Prof. Arda Yurdakul), we frame FPGA Design Space Exploration (DSE) as an automated integer-boolean optimization process. We built a constraint-aware genetic algorithm that maps Vitis HLS synthesis pragmas directly into design genomes, navigating the non-convex trade-off space under strict hardware constraints.

*The code is not public: the same repository is used for a research project this project initiated and preserved as the private repo for that project.*

---

## Technical Highlights

* **Genome-Pragma Encoding:** Direct mapping of array partitioning factors, partition types, loop unrolling factors, and pipelining flags into dependent chromosomes.
* **Constraint-Boundary Oscillation:** A specialized selection rule that excludes infeasible offspring derived from already-infeasible parents, forcing the population to bounce along—rather than drift away from—the feasible resource boundary.
* **Binomial Directional Mutation:** Uses binomial distributions over uniform or Gaussian noise to preserve gene structure while biasing local search space exploration.
* **Parallel evaluation:** A Python controller that runs multiple Vitis HLS instances in parallel via Tcl scripts, with a 10-minute timeout per synthesis run.

---

## Problem Definition & Motivation

Standard mathematical optimization approaches — linear programming, gradient-based methods, and SAT/SMT-based formulations — are poorly suited to HLS design space exploration for several reasons. (SAT- and SMT-based DSE is a real line of work in this field; the objection below is to the cost of building a faithful model, not to the technique.)

1. **No Closed Cost Model:** Vitis HLS internal compiler heuristics are proprietary, preventing the construction of an analytical cost function.
2. **Non-Convexity:** The search space is discrete and non-convex. Small parameter shifts — changing a loop unroll factor from 2 to 3 — can change pipeline depth or resource instantiation substantially.
3. **Inter-Dependent Boolean Logic:** Pragmas do not act independently; enabling a pipelining flag can change how array partitioning pragmas are mapped into block RAM vs. registers at the register-transfer level (RTL).
4. **Combinatorial Explosion:** Code bases with multiple loops, array accesses, and function calls generate huge combinatorial spaces when pragmas are applied across every block.
5. **High Synthesis Overhead:** Evaluating a single design candidate requires full HLS compilation to extract exact resource and latency metrics. Because each run takes several minutes, brute-force or greedy searches are computationally intractable.

> **Why Evolutionary Approaches?** Given the lack of analytical gradients, discrete search boundaries, and high evaluation cost, evolutionary algorithms provide an effective framework for discovering viable hardware designs without requiring closed-form cost models.

---


## Genetic Algorithm Design

* **Genome Representation:** Directly encodes synthesis pragmas into dependent chromosomes. Array partitioning maps to partition type and factor, while loop pragmas map to pipeline booleans and unroll factors.
* **Binomial Mutation:** Replaces standard Gaussian/uniform noise with a binomial distribution. This maintains local variance while actively biasing mutation in a specific search direction.
* **Selection & Boundary Control:** Keeps the top $2p$ candidates as carried-over parents, where $p$ is the per-generation survivor count listed in the [population profiles](#population-profiles) below; each is retired after five generations. To prevent drift into invalid regions, offspring derived from an infeasible parent are excluded if they remain infeasible.
* **Population Merging:** Periodically combines independently converged populations by breeding their top candidates to test for cross-population synergy.


<img src="/images/evolution_path.png" alt="Illustration of the constrained update rule" style="width:80%; display:block; margin:20px auto;">

> **The Boundary Rule:** When mutation or crossover pushes a design past hard hardware limits (e.g., 8,000 LUTs), the modified selection rule penalizes continued movement into the infeasible space, steering subsequent generations back toward valid hardware implementations.

---

## Experimental Setup

To stress-test the algorithm's ability to operate under tight hardware limits, we targeted a constrained board setup:

* **Benchmark Kernel:** Dilation-with-padding image processing kernel.
* **Target Hardware:** Xilinx `xc7s15cpga196-2` FPGA.
* **Binding Constraint:** **8,000 Look-Up Tables (LUTs)**.

### Population Profiles

| Run Profile | Offspring / Gen | Survivors / Gen | Max Generations |
| :--- | :---: | :---: | :---: |
| **Population 1** | 50 | 6 | 40 |
| **Population 2** | 50 | 10 | 40 |
| **Merged Population** | 50 | 10 | 30 |

---

## Results & Pareto Frontier Exploration

Both populations improved substantially and both stayed inside the resource budget — Population 1 from roughly 148k to 62,465 cycles by generation 24, Population 2 from roughly 231k to 64,001 by generation 20. They arrived at comparable latency by different routes, converging on distinct local optima rather than rediscovering the same design: Population 1 climbed steadily, while Population 2 oscillated across the resource limit before settling. That the two runs land close on latency but differ in their pragma configurations indicates both discovered different sections of the Pareto Frontier. This urged us to merge these populations.

### Performance Metrics Across Generations

| Population Profile | Generation | Latency (Cycles) | LUT Usage (%) | Status |
| :--- | :---: | :---: | :---: | :--- |
| **Population 1** | Gen 0, seed 1 | 148,481 | 72.6% | Feasible |
| **Population 1** | Gen 0, seed 2 | 144,385 | 70.5% | Feasible |
| **Population 1** | **Gen 24** | **62,465** | **77.2%**| Feasible (Stagnated) |
| **Population 2** | Gen 0, seed 1 | 231,425 | 67.9% | Feasible |
| **Population 2** | Gen 0, seed 2 | 149,153 | 95.3% | Feasible |
| **Population 2** | **Gen 20** | **64,001** | **79.5%** | **Optimal Feasible** |
| **Merged Pop.** | Gen 9 | 62,977 | 86.7% | Feasible |
| **Merged Pop.** | Gen 15 | *46,081* | *180.0%* | **Infeasible (Resource Breach)** |

Each population was initialized twice from independent random seeds; the two Gen 0 rows are those two starting points. The 180% in the last row is a Vitis HLS resource *estimate* — what the design would require, not what was placed — so that candidate cannot be synthesized onto this board. It is still the fastest design the search found, by a wide margin — see the discussion below for why that matters.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/population2_lineage.png" alt="Family tree of Population 2's best candidate: nodes are individual designs labelled by generation, edges show parent-offspring relationships, and infeasible parents are marked" style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Family tree of Population 2's best candidate, spanning the five generations that produced it. The number on each node is that individual's generation.</p>
</div>

> **Lineage detail**: An infeasible parent appears in this lineage, which is the selection rule working as intended — the algorithm deliberately searches close to the 8,000 LUT constraint, and candidates that cross it can still produce feasible, high-performing offspring.

---

## Key Takeaways & Discussion

1. **Within a population, the GA finds coupled parameters.** Single-population runs discovered hardware patterns that depend on two pragmas agreeing — matching a loop's unroll factor to the partition factor of the array it reads, for instance — which is the kind of interaction a coordinate-wise search misses.
2. **Merging populations combined their strategies, and hit the device rather than the algorithm.** The two populations had converged on different approaches to parallelizing the kernel. Crossing them produced offspring that inherited both, and the combination was genuinely faster: the generation-15 candidate runs in **46,081 cycles against roughly 62,000 for the better parent**, a 26% latency reduction. It is also infeasible on this board, needing 180% of the device's LUTs — combining two parallelization strategies costs roughly the sum of their resources, and the budget was already tight.

    This is a useful result rather than a failed one. The merged run maps a point on the latency–resource frontier that lies beyond the target device, which is exactly the information a designer needs when choosing hardware: it says what a larger FPGA would buy, and quantifies it. The binding constraint here is the 8,000-LUT budget of the `xc7s15`, not the search.
3. **Future Directions:** Moving beyond a baseline GA, the obvious next steps are a multi-objective algorithm such as **NSGA-II** to preserve Pareto-front diversity, and explicit modelling of inter-gene dependencies to guide directional mutation.

## Disclaimer

After the term project succeeded, the work continued as a research effort under Prof. Arda Yurdakul. I contributed to that initial continuation, but handed it off to my colleague Ilgaz Er as it overlapped with my summer internship at SISReC, Osaka University.