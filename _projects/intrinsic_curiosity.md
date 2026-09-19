---
title: "Intrinsic Motivation for Deep Symbol Learning"
collection: projects
date: 2024-02-04
header:
    video_teaser: '/images/intrinsic_curiosity_demo.mp4'
excerpt: 'An active exploration policy for Relational DeepSym that replaces uniform random exploration with an ensemble-disagreement signal. Councils trained on actively collected data improve planning accuracy by 10 percentage points over the random baseline at equal sample counts, and exceed it while using 23% fewer samples. The policy also reaches configurations absent from randomly collected datasets, including an emergent rotation that is not expressible as a single action primitive.'
description: "Undergraduate graduation project: replacing uniform random exploration in the Relational DeepSym world model with an ensemble-disagreement signal. 10 percentage points higher planning accuracy at equal sample counts, and an emergent rotation absent from the action repertoire."
---

Undergraduate graduation project (CMPE 492), Boğaziçi University. Advisors: Assoc. Prof. Emre Uğur and Alper Ahmetoğlu, CoLoRs Lab. Follow-up to [Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers](/publication/2023-relational) [\[1\]](#ref-1) (IEEE RA-L 2024), of which I am a co-author.

## Abstract

Relational DeepSym [\[1\]](#ref-1) learns object and relational symbols from the self-supervised interaction of a manipulator with a tabletop environment, but its effect prediction error grows with the number of objects even when the dataset is scaled proportionally. We hypothesize that this degradation is a property of the exploration policy rather than of the architecture: the composite structures the model is asked to predict occur with a probability that falls exponentially in the object count, so uniform random exploration under-samples precisely the states that determine performance. In this work, random exploration is replaced by an intrinsic motivation signal derived from the disagreement of an ensemble of forward models. Actions on which the ensemble cannot agree are taken to be actions it has not learned, and are preferentially executed. In a tabletop environment with five to ten objects, councils trained on actively collected data achieve approximately 10 percentage points higher planning accuracy than the random baseline at equal sample counts, and exceed the baseline while using 23% fewer training samples. Qualitative analysis shows that the policy reaches configurations random exploration does not produce, including a rotation of a wide block obtained through a controlled collapse, despite the absence of any rotation primitive in the action repertoire.

<div class="archive__item-teaser">
    <video autoplay loop muted playsinline width="100%" poster="/images/intrinsic_curiosity_demo_poster.jpg" style="display:block; object-fit:cover;">
      <source src="/images/intrinsic_curiosity_demo.mp4" type="video/mp4">
      Your browser cannot play this video. <a href="/images/intrinsic_curiosity_demo.mp4">Download it here.</a>
    </video>
</div>

## Motivation

In the preceding work [\[1\]](#ref-1), effect prediction error rises from 0.50 cm with two objects to 1.67 cm with three and 2.00 cm with four, although the corresponding datasets contain 120K, 180K and 240K samples respectively. Scaling the sample count with the object count does not arrest the degradation, which suggests that the additional samples are not distributed over the states that matter. In experiments run after publication, the random exploration policy failed to discover enough samples to learn eight-object structures even with one million samples. The number of distinct effects grows with the number of objects, and the composite structures producing those effects are rare under a uniform policy. That paper identifies a guided exploration schedule as a promising direction; the present work follows it.

The cost of this falls on data collection rather than on training. Once an interaction has been sampled enough times the model learns it, so the informative portion of a randomly collected dataset stops growing long before the dataset does, and every further sample of an already-predicted transition still costs an execution. If an interaction occurs with probability $p$ under a uniform policy, obtaining the samples it needs takes on the order of $1/p$ executions, each a pick-and-place carried out in simulation or on hardware. Adding objects lowers $p$ for every composite interaction at once, so the budget required to cover the environment grows while the useful fraction of what is collected falls. The obstacle is simulation time, training time and energy rather than any property of the model.

## Method

Let $$D$$ be a dataset of state-action-effect triplets and $$\{f_0, \dots, f_k\}$$ a set of forward models trained on overlapping subsets of $$D$$. If $$D$$ contains sufficiently many samples of a given transition, most members will learn it; conversely, disagreement among members on a state-action pair indicates that the pair is not yet learned and that further samples of it will reinforce training. This is the argument underlying Query by Committee [\[2\]](#ref-2), and it has been applied to exploration by Pathak et al. [\[3\]](#ref-3) and by Sancaktar et al. [\[4\]](#ref-4). The motivation signal for a candidate action sequence is the trace of the covariance across the flattened predictions of the council:

$$motivation(s, a_i, \{f_0, \dots, f_k\}) = \sum \text{trace}\left(\text{cov}\begin{bmatrix} \text{predict}(f_0(s, a_0, \dots, a_i)) \\ \vdots \\ \text{predict}(f_k(s, a_0, \dots, a_i)) \end{bmatrix}\right)$$

The formulation is vectorized, so signals for many candidate actions are evaluated in parallel on a GPU. For horizons greater than one, `predict` concatenates the predicted effect after each action rather than using the final predicted state, since members reaching a common final state through different erroneous intermediate predictions would otherwise register as agreement.

Rather than selecting the maximum, the policy samples uniformly from the ten highest-scoring candidates. Stochastic transitions, such as stacking a cube on a cylinder or collapsing a tower, are unpredictable by construction and would otherwise attract the policy indefinitely.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/curiosity_loop.png" alt="Exploration loop in which a seed dataset trains five council members, their prediction disagreement selects actions, and the resulting samples are appended to the dataset for the next generation." style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Fig. 1: Continuous exploration loop with intrinsic motivation.</p>
</div>

The loop is bootstrapped with a 15k-sample dataset collected under the random policy. At each generation, five councils are trained, each on a random 80% partition of the current dataset, the active policy collects 6k samples, and these are appended to the training pool. Councils are retrained from scratch at every generation rather than fine-tuned, as symbols learned from earlier data may be insufficient to describe newly discovered features, and continued training risks fixing the weights in a minimum in which the new samples are not fit. The cost of retraining is small relative to the cost of data collection at this scale.

## Experiments

The environment of the preceding work [\[1\]](#ref-1) is used, extended to five to ten objects of four types: cube, cylinder, tall block and wide block. The robot is a UR10 with a single high-level action, grasping an object and placing it on top of or near another object. Models are compared by planning accuracy: given two consecutive states from a test set, A* searches for an action sequence realizing the transition, counted as successful within 9 cm. Validation and test sets of 6k samples are collected at each generation under both policies. Data budgets were restricted deliberately in order to expose sample-efficiency differences rather than asymptotic performance.

Two configurations were evaluated. The single-horizon policy sets the search depth to one and scores all available actions. The long-horizon policy compares 100 sequences of length five, the maximum a 24 GB GPU supports, corresponding to 0.032% of the search space at that depth.

| Council | Planning accuracy | Training samples |
| :--- | :---: | :---: |
| Random baseline, gen 6 | 0.52 | 51k |
| Single horizon, gen 4 | 0.58 | 39k |
| Single horizon, gen 6 | 0.62 | 51k |

Accuracies are averaged over seven randomly collected test sets. At equal sample counts the single-horizon council is approximately 10 percentage points ahead. Generation 4 of the single-horizon policy exceeds generation 6 of the baseline while training on 12k fewer samples.

Evaluated on the actively collected test sets, all councils, including those trained under the active policy, score lower than on the randomly collected sets, and the variance across sets is higher. Both observations support the claim that the active policy samples a different and less homogeneous distribution, and indicate that the improvement above is not an artifact of a test distribution favouring the curious councils.

Themes in the collected data are traceable through Cartesian coordinates alone, and two of them mark successive phases of the exploration. Grasp success falls sharply in generation 1 and recovers thereafter, indicating that failing grasps are initially the least predictable outcomes available. Once that boundary is resolved the policy moves on: multi-object movement, in which a wide block is used as a tray to displace several objects at once, rises after generation 1 and peaks in generation 2 at roughly six times the seed level, remaining above the first two generations for the rest of the run.

<div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 1.5rem; margin: 2rem 0; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 320px; text-align: center;">
    <img src="/images/grasp_rate.png" alt="Successful grasp rate per generation, falling to approximately 0.37 in generation 1 and remaining near 0.9 in all others." style="width:100%; display:block;">
    <p style="font-style: italic; color: #666; margin-top: 8px; font-size: 0.85rem;">Fig. 2: Successful grasp rate across generations. The drop in generation 1 reflects active exploration of failing grasps.</p>
  </div>
  <div style="flex: 1; min-width: 320px; text-align: center;">
    <img src="/images/multi_object_movement.png" alt="Number of samples containing multi-object movement per generation, rising from about 59 in generation 0 to about 355 in generation 2 and settling between 143 and 240 afterwards." style="width:100%; display:block;">
    <p style="font-style: italic; color: #666; margin-top: 8px; font-size: 0.85rem;">Fig. 3: Samples involving multi-object movement across generations. Attention shifts to using a wide block as a tray once grasp failures are predictable.</p>
  </div>
</div>

## Emergent interactions

Rotation is not among the action primitives, which permit only grasping and placement. The policy nonetheless discovered a sequence leaving a wide block perpendicular to the table: the block is placed on a tall prism and a cube is then placed to its left, inducing a controlled fall. Perpendicular configurations are absent from the training distribution, so council predictions on them diverge and the policy pursues them. This environment was implemented approximately eighteen months before these experiments and used continuously over that period by its author and by a PhD student in the same laboratory, neither of whom had identified this configuration as reachable.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
  <video width="100%" controls autoplay loop muted playsinline poster="/images/tall_cut_demo_fixed_poster.jpg" style="border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <source src="/images/tall_cut_demo_fixed.mp4" type="video/mp4">
    Your browser cannot play this video. <a href="/images/tall_cut_demo_fixed.mp4">Download it here.</a>
  </video>
  <p style="font-style: italic; color: #666; margin-top: 8px;">Fig. 4: Emergent rotation. A controlled collapse yields a configuration absent from the training distribution.</p>
</div>

A second theme is interaction with the base of a composite structure. Since the primitives are top-down, targeting a foundational block displaces the objects resting above it. Predicting such a transition requires resolving several tiers of relations, which is where Relational DeepSym is weakest and where council disagreement is correspondingly highest.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
  <video width="100%" controls autoplay loop muted playsinline poster="/images/complex_cut_demo_poster.jpg" style="border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <source src="/images/complex_cut_demo.mp4" type="video/mp4">
    Your browser cannot play this video. <a href="/images/complex_cut_demo.mp4">Download it here.</a>
  </video>
  <p style="font-style: italic; color: #666; margin-top: 8px;">Fig. 5: Manipulation of a multi-tier structure through its foundation, requiring prediction over nested relations.</p>
</div>

## Negative results

The project began as an attempt to grow the symbol set itself. An earlier formulation searched for novelty in symbolic rather than effect space: a state-action pair whose symbolic description had not been observed before is one whose relations the model has not yet encoded, and collecting such pairs should extend the symbol set rather than reinforce it. Finding unexplored samples is a density estimation problem, and the Relational DeepSym encoder already extracts the relational information such an estimator requires, so the encoder was used to reduce state-action pairs to discrete graphs whose occurrence counts were stored in a lookup table, the least frequent pair being taken as the most novel. Improvements over random exploration proved indistinguishable from noise.

The reduction is performed by a network trained on the data collected so far, so a genuinely novel state, whose distinguishing properties the encoder was never trained to represent, is mapped onto familiar symbols rather than extrapolated to new ones. The metric is therefore blind precisely where it is required to discriminate. Reformulating the objective from which states are novel to which states are predicted poorly removes the dependence on extrapolation, and motivates the disagreement signal above.

Extending the horizon did not improve on the single-horizon policy. Although long-horizon councils outperform the random baseline, the datasets they collect are simpler, in the sense that all councils achieve high accuracy on them. This is attributed to parametrization rather than to horizon depth: evaluating 100 sequences samples 0.032% of the depth-five search space, and the low-probability structures the policy is intended to find are unlikely to appear among the candidates considered. Sancaktar et al. [\[4\]](#ref-4) report substantial gains from longer novelty horizons, which makes the memory constraint the more probable explanation. Distinguishing the two requires sweeping depth and width, each configuration costing several days of experiment time.

## Limitations and future work

Results come from a single seed in one environment without repeated runs; the gap is consistent across all seven test sets, but no error bars can be reported. Budgets were capped to expose sample efficiency, so neither policy was run to convergence and the ceiling of the method is unknown.

The two policies have not been combined, and the horizon parameters remain unswept. Introducing bias toward existing clusters and tall assemblies in action selection would target composite structures directly, though the literature disagrees on whether such bias is necessary [\[5\]](#ref-5), [\[6\]](#ref-6). Internal results in the laboratory indicate that removing the Gumbel-sigmoid [\[7\]](#ref-7), [\[8\]](#ref-8) discretization improves both training speed and prediction accuracy, suggesting exploration without discretization followed by training of discretized models for planning. Finally, Relational DeepSym is retrained from scratch at each generation; incrementing on learned symbols, as in NS-CL[\[9\]](#ref-9), would allow successive generations to reuse what earlier ones acquired.


## Code

The codebase is forked from the private repository of the preceding work and cannot be released publicly. Code and the full project report are available on request: batuhancelik.boun@gmail.com

## References

<a id="ref-1"></a>[1] A. Ahmetoglu, B. Celik, E. Oztop, and E. Ugur, "Discovering predictive relational object symbols with symbolic attentive layers," *IEEE Robotics and Automation Letters*, vol. 9, no. 2, pp. 1977–1984, Feb. 2024. [DOI: 10.1109/LRA.2024.3350994](https://doi.org/10.1109/LRA.2024.3350994) · [arXiv:2309.00889](https://arxiv.org/abs/2309.00889)

<a id="ref-2"></a>[2] H. S. Seung, M. Opper, and H. Sompolinsky, "Query by committee," in *Proceedings of the Fifth Annual Workshop on Computational Learning Theory*, 1992, pp. 287–294.

<a id="ref-3"></a>[3] D. Pathak, D. Gandhi, and A. Gupta, "Self-supervised exploration via disagreement," in *Proceedings of the 36th International Conference on Machine Learning*, PMLR vol. 97, 2019, pp. 5062–5071. [Link](https://proceedings.mlr.press/v97/pathak19a.html)

<a id="ref-4"></a>[4] C. Sancaktar, S. Blaes, and G. Martius, "Curious exploration via structured world models yields zero-shot object manipulation," *Advances in Neural Information Processing Systems*, vol. 35, 2022, pp. 24170–24183.

<a id="ref-5"></a>[5] B. Norman and J. Clune, "First-explore, then exploit: Meta-learning intelligent exploration," arXiv preprint, 2023. [arXiv:2307.02276](https://arxiv.org/abs/2307.02276)

<a id="ref-6"></a>[6] F. Kaplan and P.-Y. Oudeyer, "Curiosity-driven development," in *Proceedings of the International Workshop on Synergistic Intelligence Dynamics*, 2006, pp. 1–8.

<a id="ref-7"></a>[7] C. J. Maddison, A. Mnih, and Y. W. Teh, "The concrete distribution: A continuous relaxation of discrete random variables," arXiv preprint, 2016. [arXiv:1611.00712](https://arxiv.org/abs/1611.00712)

<a id="ref-8"></a>[8] E. Jang, S. Gu, and B. Poole, "Categorical reparameterization with Gumbel-softmax," arXiv preprint, 2016. [arXiv:1611.01144](https://arxiv.org/abs/1611.01144)

<a id="ref-9"></a>[9] J. Mao, C. Gan, P. Kohli, J. B. Tenenbaum, and J. Wu, "The neuro-symbolic concept learner: Interpreting scenes, words, and sentences from natural supervision," in *International Conference on Learning Representations*, 2019. [arXiv:1904.12584](https://arxiv.org/abs/1904.12584)