---
title: "Intrinsic Curiosity for Deep Symbolic Robot Learning"
collection: portfolio
header:
    video_teaser: '/images/instrinsic_curiosity_demo_fixed.mp4'
excerpt: 'The prior [Relational DeepSym](/publications/2023-relational) framework requires on the order of **1 million samples** just to learn dynamics in a 4-object environment — a data bottleneck rooted in its reliance on uniform random exploration. I proposed and and led this project, my **graduation project**, to tackle this bottleneck directly: to explore complex, counter-intuitive, and high-information-gain interactions and to probe the limitations of the Relational DeepSym architecture.'
---

## Abstract

Curiosity is a form of intrinsic motivation key to reinforcing active learning and spontaneous exploration. Conceived and proposed independently following a comprehensive active learning literature review during concurrent work on [robotic scaffolding](/publications/2023-icdl-scafolding), this project directly addresses the staggering data-efficiency and scalability limits of recently proposed [Relational Deepsym](/publications/2023-relational) architecture. Specifically, the framework aims to alleviate the severe data collection bottleneck of the baseline Relational DeepSym framework—which demands upwards of **1 million samples just to discover simple dynamics of 4-object environments**. By introducing an intrinsic curiosity paradigm driven by ensemble disagreement, the robotic agent utilizes the variance of a forward-prediction dynamics council as an epistemic motivation signal to actively target unlearned state-action pairs. We evaluate the proposed formulation within a simulated tabletop environment featuring 5 to 10 distinct physical entities. Our results demonstrate that targeting **"gaps in knowledge"** via active exploration drastically reduces data overhead, providing up to a **10% planning accuracy improvement over uniform random exploration**. Furthermore, qualitative analysis confirms that the **curiosity policy uncovers highly complex, counter-intuitive multi-object physical interactions that remain statistically improbable under random exploration policies**.

[Github](https://github.com/mbatuhancelik/human2robot_cnmp/tree/master)

<div class="archive__item-teaser">
    <video autoplay loop muted playsinline width="100%" style="display:block; object-fit:cover;">
      <source src="/images/instrinsic_curiosity_demo_fixed.mp4" type="video/mp4">Your browser does not support the video tag.
    </video>
</div>

---

## Motivation

While the original Relational DeepSym framework discovers symbolic relations reliably, it scales poorly due to its reliance on uniform random exploration. The baseline architecture requires roughly **1,000,000 samples** to learn forward dynamics in a **simple 4-object setup**. Most of this data consists of **redundant, low-information repetitions**, such as repeatedly restacking the same two blocks.

To formalize this bottleneck, the probability of an agent organically discovering a meaningful $n$-object composite interaction scales inversely with the factorial of the entity count:

$$P(\text{discovery}) \propto \frac{1}{n!}$$

As environments scale past simple setups, uniform random sampling becomes mathematically unviable under realistic robotics data constraints. This project replaces random sampling with an epistemic uncertainty mechanism to **actively discover the improbable, high-information-gain interactions** to bypass these scaling limits.

## 🛠️ Methodology & Core Contributions

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/curiosity_loop.png" alt="Active Exploration Loop and Training Framework" style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Figure: Active Exploration Loop.</p>
</div>
This active data collection architecture replaces uniform random baselines with targeted, curiosity-driven exploration split into distinct operational phases.

### 1. Data Bootstrapping and Partitioning
* **Seed Dataset:** The model is bootstrapped using a small 15k sample dataset collected via a standard random exploration policy.
* **80% Data Partitioning:** At each iteration, the dataset expands into a "Next iteration Dataset." Each individual Council Member ($0$ through $4$) trains on a randomized **80% partition of this data**, ensuring architectural and predictive diversity.

### 2. The Epistemic Disagreement Council
During online exploration, the agent utilizes **council disagreement** to estimate epistemic uncertainty over long-horizon effect predictions.

* **State-Action Filtering:** The environment feeds the current **State** and a random subset of 300 **Available Action Sequences** (constrained to a lookahead horizon length of 5 due to VRAM limits) into the council.
* **Variance-Driven Rewards:** Each member generates a forward prediction. The system computes the intrinsic motivation reward using the trace of the covariance matrix across flattened prediction vectors as the measure of disagreement:

$$motivation(s, a_i, \{f_0, \dots, f_k\}) = \sum \text{trace}\left(\text{cov}\begin{bmatrix} \text{predict}(f_0(s, a_0, \dots, a_i)) \\ \text{predict}(f_1(s, a_0, \dots, a_i)) \\ \vdots \\ \text{predict}(f_k(s, a_0, \dots, a_i)) \end{bmatrix}\right)$$

* **Mitigating Stochastic Traps:** To avoid getting stuck in sthocastic dynamics (the "noisy TV" trap), the **policy samples randomly** from the top 10 highest-disagreement trajectories instead of greedy picking.

### 3. Multi-Generational Regeneration Loop
* **Feedback Pipeline:** The chosen action sequences(2 selections, 10 actions total) execute in simulation, returning 6k high-information samples per generation back into the training pool.
* **Council Resetting:** Rather than fine-tuning weights—which traps networks in local minima, **new councils are re-trained from scratch** on the updated data pools. Retraining cost is small relative to the cost of data collection at this scale.

---

## 📊 Experimental Results

The framework was evaluated using a UR10 robotic manipulator interacting with 5 to 10 distinct entities (cubes, cylinders, tall blocks, and wide blocks) using high-level, object-relative grasp and place actions. Models were benchmarked on planning success rates using the $A^*$ algorithm to reach target states within a strict 4 cm (half-cube width) error margin. Data budgets were intentionally restricted to highlight sample-efficiency differentials.

### Planning Performance Comparison
The actively explored councils achieved significant sample-efficiency gains over the random baseline:

| Exploration Policy Generation | Accuracy on Random Test Data | Target Sample Size |
| :--- | :---: | :---: |
| **Random Baseline (Gen 6)** | $$0.52$$ | 51k samples |
| **Single Horizon (Gen 4)** | **$$0.58$$** | **39k samples** |
| **Single Horizon (Gen 6)** | **$$0.62$$** | 51k samples |

> **Key Takeaway:** Generation 4 of the curiosity model outperformed Generation 6 of the random baseline while utilizing **12,000 fewer (23% less) training samples**.

### Emergent Exploration Themes
The variance tracker forces the agent through distinct learning phases as it exhausts predictable environment dynamics:
* **Generation 1:** Targets structural contact physics, executing boundary actions to resolve grasp failures.
* **Generations 2–5:** Shifts directly toward complex multi-object movements and structural stacking to maximize council uncertainty.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/grasp_rate.png" alt="Active Exploration Loop and Training Framework" style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Figure: Successful grasp rate among different generations. Stark drop in generation 1 indicates the active exploration of unsuccessful grasp operation.</p>
</div>

---

### 🔍 Qualitative Analysis

The Generation 6 curiosity policy consistently yielded clusters of high-information trajectories matching two distinct emergent physical themes.

### 1. Emergent Rotation Operations via Controlled Collapses
Despite **rotation primitives being explicitly omitted** from the action repertoire, the active exploration policy discovered a multi-step sequence that rotates wide objects using a controlled fall. Because rotated states have yet to be encountered, these configurations induce maximum epistemic uncertainty, making rotation a primary exploration theme.

Crucially, this specific simulation environment was used continuously by twelve undergraduate students, three master's students, and a PhD candidate over an 18-month period. Throughout that lifecycle, **this precise physical interaction boundary was never discovered** through manual testing, validating the method's ability to locate isolated, high-information edge cases.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
  <video width="100%" controls autoplay loop muted playsinline style="border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <source src="/images/tall_cut_demo_fixed.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p style="font-style: italic; color: #666; margin-top: 8px;">Figure: Emergent rotation dynamics. The agent exploits physics boundaries to induce a controlled perpendicular drop, generating high-uncertainty spatial states.</p>
</div>

### 2. Multi-Step Manipulation of Composite Structures
The agent autonomously **constructs complex composite structures to probe their affordances** by interacting with their base components. In this example, the policy attempts to position a brown cube to the right of a green cube. Because action primitives are restricted to top-down vectors, targeting the foundation displaces an overlapping blue cylinder, forcing the agent to reason directly through the structural hierarchy.

Evaluating this transition requires **multi-step structural reasoning over nested symbolic relations**, which is an out-of-distribution bottleneck for standard Relational DeepSym. To compute the grasping target, the model must resolve that a wide object sits on top of the brown cube, which in turn supports a blue cylinder on its leftmost component. An equivalent multi-tier inference chain must be resolved to identify the valid placement coordinate. This complex relational dependency caused high council uncertainty, fulfilling the exact objective of the active framework.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
  <video width="100%" controls autoplay loop muted playsinline style="border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <source src="/images/complex_cut_demo.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p style="font-style: italic; color: #666; margin-top: 8px;">Figure: High-order composite interaction. The agent targets foundational blocks within a multi-tier structure, forcing the model to predict complex, nested physical dependencies.</p>
</div>

---

## Conclusion

This project demonstrates that an epistemic, curiosity-driven active exploration policy successfully mitigates the data collection bottlenecks of relational world models. While baseline configurations require upwards of 1 million samples to comprehend simple 4-object dynamics, this architecture **uncovers complex multi-object physics with a fraction of the data overhead**. Bootstrapped on a modest 15k sample seed dataset, the 5-member disagreement council drives the agent to isolate high-information state-action pairs efficiently. 

Experimental results validate a 10% planning accuracy improvement over random exploration within a strict 4 cm error margin. Notably, the Generation 4 curiosity model outpaces the Generation 6 random baseline while utilizing 23% less training data, **proving that targeting gaps in knowledge yields major sample-efficiency gains**. Finally, qualitative analysis confirms that maximizing epistemic uncertainty provokes the autonomous discovery of complex, out-of-distribution behaviors—such as unprogrammed rotation actions and multi-step structural manipulation—which were completely missed during 18 months of manual testing.

## Future Work

This active framework provides a highly promising foundation for data-efficient symbolic learning, with several clear trajectories for future extension:

* **Better Quantitative Analysis:** The entire quantitative evaluation for this project was crammed into a six-hour window during finals week. Needless to say, neither I nor my advisor, Dr. Ahmetoglu, were in the right state of mind to envision insightful data visualizations, explaining their absence.
* **Incremental Symbolic Models:** Integrating incremental training logic (similar to [NSCL](https://arxiv.org/abs/1904.12584) by Mao et al.) could resolve Relational DeepSym's architectural limits. A model supporting incremental symbolic logic would further compress data requirements by exploiting overlaps between generations.
* **Full Dynamics Convergence:** Because the data budget in this iteration was restricted to highlight sample-efficiency differentials, a logical next step is running the multi-generational training loop to full convergence to discover the council's true learning capacity.
* **Structural Exploration Biases:** Future iterations will explore integrating structural heuristics. Biasing action selection toward existing object clusters and tall assemblies will deliberately force the agent into highly intricate, high-order multi-object manipulation episodes.
* **Scaling Environment Complexity:** The current setup manages 5 to 10 physical entities. Increasing the entity count is necessary to stress-test the limits of the framework, as the current model successfully resolved all dynamics explored by the active policy.
* **Alleviating Compute and VRAM Constraints:** Hardware limitations currently cap lookahead horizons to a length of 5 and a subset of 300 action sequences despite optimization. Scaling compute capabilities or optimizing the underlying prediction pipeline will allow the framework to scale to longer horizons, eliminating in-generation repetitions.