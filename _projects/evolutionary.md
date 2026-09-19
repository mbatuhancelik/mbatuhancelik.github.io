---
title: "FPGA Design Optimization using Genetic Algorithms"
collection: projects
excerpt: "A genetic algorithm for High-Level Synthesis design space exploration, with a selection rule that holds the population against the resource constraint rather than letting it drift away. Latency on a dilation kernel falls from 148,481 to 62,465 cycles under an 8,000-LUT budget. Merging two converged populations produced the fastest design of the search, at 180% of the device's LUTs."
venue: "CMPE583 (Reconfigurable Computing) Term Project"
date: 2023-06-05
description: "Course term project: framing FPGA high-level-synthesis design space exploration as constrained integer-boolean optimization, and solving it with a genetic algorithm whose selection rule keeps the population against the resource constraint."
---

Term project for CMPE583, Reconfigurable Computing, Boğaziçi University, taught by Prof. Arda Yurdakul. Joint work with Ilgaz Er.

<!-- TODO (Batuhan): if you want the report linked here, upload the PDF to the repo and add the
     link on this line. I have not written a link to a file that does not exist. -->

## Abstract

An FPGA design is parametrized by pragmas and synthesis options that unroll loops, pipeline them, and partition arrays. Optimizing design parameters is an integer-boolean problem by definition. However, the quantities to be optimized, latency and resource usage, admit no closed form, since the internal heuristics of the synthesis tool are not exposed. Design space exploration is therefore carried out by hand, and the number of designs a project can consider is bounded by the designer's time. We aim to automate this process with a genetic algorithm in which pragmas map directly onto chromosomes and an infeasible offspring of an infeasible parent is excluded from selection, so that the population oscillates along the resource constraint rather than drifting past it. On a dilation kernel targeting a device with 8,000 LUTs, latency falls from 148,481 cycles at generation 0 to 62,465 at generation 24. Merging two independently converged populations did not improve on either parent under the constraint: the fastest design the merge produced requires 180% of the device's LUTs.

## Motivation

Loop unroll factors, pipelining flags and array partition strategies map directly onto FPGA configuration, so finding an optimal design is an integer-boolean problem that the standard solvers do not reach. The objective admits no analytical form, since latency and resource usage depend on internal Vitis HLS heuristics that are not exposed. The space is not convex, which rules out simplex, and gradient descent does not consider constraints by definition, which matters because the designs worth finding sit against the resource constraint. Brute force is also unavailable: a candidate must be fully synthesized before its latency is known, at several minutes per run, and even a small design space holds millions of configurations.

## Method

An evolutionary algorithm's update step is not fixed by a formula, so the constraint can live in the selection rule rather than in an objective that cannot be written down. Pragmas map onto chromosomes one to one and their variables onto genes, with dominance where one gene disables another: while an array's `partition` gene is none, its `factor` gene never reaches the design. Offspring are produced by crossing over and then mutated; crossing over alone did not introduce enough variation, nor did Gaussian mutation, so mutated genes are drawn from a binomial with $$p > 0.5$$, which localizes the variance of the genome as a Gaussian would and additionally biases mutation in one direction.

At each generation every design is synthesized and the lowest-latency individuals are kept as parents. They survive into the following generation and are retired after five. Minimizing latency generally rewards using as much of the device as possible, so the optimum is likely to lie against the resource constraint. To search there without leaving the feasible region permanently, an infeasible offspring of an infeasible parent is excluded from selection. A lineage that crosses the constraint can continue only by producing a feasible child, so the population oscillates along the boundary instead of drifting past it; because a parent survives five generations, the return can take several attempts.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/evolution_path.png" alt="Ten labelled points joined by arrows descend from upper left to lower right across a green sigmoid curve that marks the feasibility boundary. The first three steps stay clear of the curve; from the fourth onward the path straddles it, and every point landing on the infeasible side is followed by one that returns to the feasible side." style="width:80%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Fig. 1: The constrained update rule on an abstract objective. The vertical axis is minimized and the green curve is the feasibility boundary, with the feasible region above and to the right of it. Steps u to w descend through the interior. From step a onward the path has reached the boundary, and each point that lands on the infeasible side is followed by one back inside, so the search travels along the boundary rather than through it.</p>
</div>

Since the space is non-convex, a converged population identifies one local optimum. Two are converged independently and their best members mated to form a third, on the hypothesis that the offspring inherit the distinct strategies of both populations.

## Experiments

Each candidate is evaluated by full synthesis. A controller runs several Vitis HLS instances concurrently and records every individual's genome, generation and parents, which is what makes the lineage in Fig. 2 recoverable. The target is a dilation-with-padding image kernel, a 3×3 maximum over a padded image, on a Xilinx `xc7s15cpga196-2`, whose 8,000 LUTs are the binding constraint.

| Run profile  | Offspring per generation | Survivors | Maximum generations |
| :----------- | :----------------------: | :-------: | :-----------------: |
| Population 1 |            50            |     6     |         40          |
| Population 2 |            50            |    10     |         40          |
| Merged       |            50            |    10     |         30          |

Latency is in cycles. Any LUT usage above 100% cannot be placed on this board.

| Population   | Generation | Latency | LUT usage (of 8,000) |
| :----------- | :--------: | ------: | --------: |
| Population 1 |     0      | 148,481 |     72.6% |
| Population 1 |     0      | 144,385 |     70.5% |
| Population 1 |     24     |  62,465 |     77.2% |
| Population 2 |     0      | 231,425 |     67.9% |
| Population 2 |     0      | 149,153 |     95.3% |
| Population 2 |     20     |  64,001 |     79.5% |
| Merged       |     9      |  62,977 |     86.7% |
| Merged       |     15     |  46,081 |    180.0% |
| Merged       |     21     |  65,025 |     92.9% |

Each population was initialized twice from independent random seeds. Population 1 fell to 62,465 cycles by generation 24, Population 2 to 64,001 by generation 20. They reach comparable latency through different pragma configurations, which indicates distinct local optima rather than one design found twice.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/population2_lineage.png" alt="Designs plotted by LUT count against latency and joined by lines into a family tree. Node labels give the generation and node colour lightens with it, from dark navy at generation 13 to yellow at generation 24. A vertical line at 8,000 LUTs separates designs that fit the device from those that do not, and four ancestors lie to its right, one of them near 16,000 LUTs." style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Fig. 2: Recorded ancestry of the best individual of Population 1, spanning generations 13 to 24. Each node is one design, placed by its LUT count and its latency and labelled with its generation; colour lightens with generation. The vertical line is the 8,000-LUT limit. Four ancestors sit to the right of it and cannot be placed on this device, one at roughly twice the budget, and their descendants return to the left of it at lower latency.</p>
</div>

Designs that cross the 8,000-LUT line produce feasible offspring at lower latency than themselves, which is the selection rule behaving as intended; the lowest-latency individual descends from an ancestor 15% past the limit. The remaining sixteen generations circled that optimum without improving on it, since no momentum term is implemented. Within a population the algorithm did find couplings between pragmas, such as coupling a loop's unroll factor to the partition factor of the array it reads, where neither value yields an improvement on its own.

## Negative results

Merging the two populations did not improve on either parent under the constraint. The three best feasible designs, one from each population and one from the merge, fall within 2.5% of one another in latency. This follows from how much of the device each parent already occupied: both had converged on parallelizations using close to 80% of the LUTs, so around 20% is left for whatever the other contributes, and a parallelization that fits in a fifth of the device is not the one either population converged on.

The strategies do combine, but only past the limit. The generation-15 design is where the family lines of both populations meet, and it is the fastest of the search at 46,081 cycles, requiring 180% of the device. Both figures are the tool's estimates for a design that was never placed. That it cannot be placed here is what makes it worth reporting. It prices the constraint: on those estimates, a part with 80% more logic would remove 26% of the latency, a trade a designer would otherwise discover only by running the whole search again on each candidate device. What it does not settle is whether the two strategies could be made to coexist within the budget, or whether the combination would still be ahead once it fits. The merging procedure selects on latency alone and carries no representation of the resource constraint, so it was never positioned to answer either.

## Limitations

Results come from one kernel on one device, with a single merge and no repeated runs. Population size, survivor count and parent lifetime were fixed rather than swept, so their separate contributions are unknown. The baseline is the most basic genetic algorithm, and how a current GA implementation would perform is an open question.

## Future work

A multi-objective algorithm such as NSGA-II [\[1\]](#ref-1) would maintain a Pareto front rather than collapsing latency and resources into a feasibility test, which is where the merge failed. Relations between genes could also be elicited from the generations already recorded and used to bias the mutation direction. Rerunning the merge on a larger device would settle whether the combined strategies improve on either parent once the budget is not binding.

## My contribution

- Proposed the boundary selection rule: excluding an infeasible offspring of an infeasible parent, so that a lineage crossing the resource constraint continues only by returning inside it.
- Replaced Gaussian mutation with the binomial, for the directional bias it adds.
- Defined the genome representation and the pragma-to-chromosome encoding that the crossover and mutation operators act on, and the data layer holding the synthesized results.

Synthesizing a design from a chromosome, and the parallel HLS runs and their distribution across machines, are Ilgaz Er's.

## Code

The code is not public: the repository was carried over into a research project this work started, and remains that project's private repository. I contributed to that continuation under Prof. Arda Yurdakul, then handed it off to Ilgaz Er as it overlapped with my internship at SISReC, Osaka University.

## References

<a id="ref-1"></a>[1] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, "A fast and elitist multiobjective genetic algorithm: NSGA-II," *IEEE Transactions on Evolutionary Computation*, vol. 6, no. 2, pp. 182–197, Apr. 2002. [DOI: 10.1109/4235.996017](https://doi.org/10.1109/4235.996017)