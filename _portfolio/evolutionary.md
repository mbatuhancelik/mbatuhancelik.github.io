---
title: "FPGA Design Optimization using Genetic Algorithms"
collection: portfolio
excerpt: "Automating High-Level Synthesis (HLS) design space exploration using a custom, constraint-aware genetic algorithm on a non-convex, integer-boolean search space."
venue: "CMPE583 (Reconfigurable Programming) Term Project"
date: 05.06.2023
---

Design parameter optimization in FPGA programming is a **non-convex, high-dimensional, integer-boolean optimization problem**. Because closed-form mathematical solutions do not exist for compiler-driven hardware generation, industrial FPGA designs are traditionally tuned through trial, error, and designer intuition. 

In this project, developed with **Ilgaz Er** for *CMPE583: Reconfigurable Programming* (taught by Prof. Arda Yurdakul), we frame FPGA Design Space Exploration (DSE) as an automated integer-boolean optimization process. We built a custom, constraint-aware **Genetic Algorithm (GA)** that maps Vitis HLS synthesis pragmas directly into design genomes, navigating the non-convex trade-off space under strict hardware constraints.

---

## Technical Highlights

* **Genome-Pragma Encoding:** Direct mapping of array partitioning factors, partition types, loop unrolling factors, and pipelining flags into dependent chromosomes.
* **Constraint-Boundary Oscillation:** A specialized selection rule that excludes infeasible offspring derived from already-infeasible parents, forcing the population to bounce along—rather than drift away from—the feasible resource boundary.
* **Binomial Directional Mutation:** Uses binomial distributions over uniform or Gaussian noise to preserve gene structure while biasing local search space exploration.
* **Parallel Orchestration Engine:** A Python controller running multiple Vitis HLS instances via Tcl scripts in parallel, complete with automatic 10-minute timeout management.

---

## Problem Definition & Motivation

Standard mathematical optimization approaches (such as Simplex, MaxSAT, or Gradient Descent) fail in HLS Design Space Exploration due to several core domain challenges:

1. **No Closed Cost Model:** Vitis HLS internal compiler heuristics are proprietary, preventing the construction of an analytical cost function.
2. **Non-Convexity & High-Frequency Noise:** The search space is discrete, non-convex, and noisy. Small parameter shifts (e.g., changing a loop unroll factor from 2 to 3) can drastically alter pipeline depth or resource instantiation.
3. **Inter-Dependent Boolean Logic:** Pragmas do not act independently; enabling a pipelining flag can change how array partitioning pragmas are mapped into block RAM vs. registers at the register-transfer level (RTL).
4. **Combinatorial Explosion:** Code bases with multiple loops, array accesses, and function calls generate huge combinatorial spaces when pragmas are applied across every block.
5. **High Synthesis Overhead:** Evaluating a single design candidate requires full HLS compilation to extract exact resource and latency metrics. Because each run takes several minutes, brute-force or greedy searches are computationally intractable.

> **Why Evolutionary Approaches?** Given the lack of analytical gradients, discrete search boundaries, and high evaluation cost, evolutionary algorithms provide an effective framework for discovering viable hardware designs without requiring closed-form cost models.

---


## Genetic Algorithm Design

* **Genome Representation:** Directly encodes synthesis pragmas into dependent chromosomes. Array partitioning maps to partition type and factor, while loop pragmas map to pipeline booleans and unroll factors.
* **Binomial Mutation:** Replaces standard Gaussian/uniform noise with a binomial distribution. This maintains local variance while actively biasing mutation in a specific search direction.
* **Selection & Boundary Control:** Keeps the top $2p$ parents across generations (retired after 5 generations). To prevent drift into invalid spaces, offspring derived from an infeasible parent are immediately excluded if they remain infeasible.
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

The GA successfully explored the trade-off space to locate low-latency, hardware-feasible candidates. However, evolutionary dynamics varied across runs: **Population 1** hit a local optimum early and stagnated, while **Population 2** dynamically oscillated across the resource limit before settling on a high-performing point.

### Performance Metrics Across Generations

| Population Profile | Generation | Latency (Cycles) | LUT Usage (%) | Status |
| :--- | :---: | :---: | :---: | :--- |
| **Population 1** | Gen 0 | 148,481 | 72.6% | Feasible |
| **Population 1** | Gen 0 | 144,385 | 70.5% | Feasible (Stagnated) |
| **Population 1** | **Gen 24** | **62,465** | **77.2%**| Feasible (Stagnated) |
| **Population 2** | Gen 0 | 231,425 | 67.9% | Feasible |
| **Population 2** | Gen 0 | 149,153 | 95.3% | Feasible |
| **Population 2** | **Gen 20** | **64,001** | **79.5%** | **Optimal Feasible** |
| **Merged Pop.** | Gen 9 | 62,977 | 86.7% | Feasible |
| **Merged Pop.** | Gen 15 | *46,081* | *180.0%* | **Infeasible (Resource Breach)** |

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/population2_lineage.png" alt="Blending-CNMP Architecture Overview" style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Family tree of Population 2's top candidate over 5 generations, numbers of the dots indicate the individual design's generation.</p>
</div>

> **Lineage detail**: The inclusion of an infeasible parent at Generation 23 demonstrates the search strategy in action. The algorithm intentionally explores near the 8,000 LUT constraint to uncover high-performing, feasible designs.

---

## Key Takeaways & Discussion

1. **Intra-Population Optimization:** Single-population runs successfully discovered coupled hardware patterns—such as matching a loop's unroll factor directly to an array's partition factor.
2. **The Population Merging Bottleneck:** Breeding independently-converged populations did not reliably improve upon parent optima. Combining distant local optima, both populations evolved different strategies, frequently broke co-adapted gene complexes. While this variation yielded high utilization of the hardware, 180% LUT utilization in generation 15, it did not converge to a feasible optima in **10 generations**.
3. **Future Directions:** Moving beyond baseline GAs, future work will integrate more advanced evolutionary algorithms, such as **NSGA-II**, to preserve Pareto front diversity and explore explicit inter-gene dependency modeling to guide directional mutations.

## Disclaimer

Upon our initial success at this term project this endevour evolved into a research effort under supervision of Prof. Arda Yurdakul which I initially contributed to. However, as its work coincided with my summer internship at SISREC, Osaka University, I had to hand-off this work to my collegue Ilgaz Er.