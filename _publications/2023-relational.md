---
title: "Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers"
collection: publications
category: manuscripts
authors: "Alper Ahmetoğlu, <b>Batuhan Çelik</b>, Erhan Öztop, Emre Uğur"
permalink: /publication/2023-relational
date: 2024-01-08
venue: 'IEEE Robotics and Automation Letters (RA-L)'
paperurl : "https://arxiv.org/abs/2309.00889"
description: "IEEE RA-L 2024. A deep architecture that discovers object symbols and explicit relational symbols from a robot's self-supervised interaction with a varying number of objects on a tabletop."
---

### Abstract
In this paper, we propose and realize a new deep learning architecture for discovering symbolic representations for objects and their relations based on the self-supervised continuous interaction of a manipulator robot with multiple objects on a tabletop environment. The key feature of the model is that it can handle a changing number of objects naturally and map the object-object relations into symbolic domain explicitly. In the model, we employ a self-attention layer that computes discrete attention weights from object features, which are treated as relational symbols between objects. These relational symbols are then used to aggregate the learned object symbols and predict the effects of executed actions on each object. The result is a pipeline that allows the formation of object symbols and relational symbols from a dataset of object features, actions, and effects in an end-to-end manner. We compare the performance of our proposed architecture with state-of-the-art symbol discovery methods in a simulated tabletop environment where the robot needs to discover symbols related to the relative positions of objects to predict the observed effect successfully. Our experiments show that the proposed architecture performs better than other baselines in effect prediction while forming not only object symbols but also relational symbols. Furthermore, we analyze the learned symbols and relational patterns between objects to learn about how the model interprets the environment. Our analysis shows that the learned symbols relate to the relative positions of objects, object types, and their horizontal alignment on the table, which reflect the regularities in the environment.

[arXiv](https://arxiv.org/abs/2309.00889) · [IEEE Xplore](https://ieeexplore.ieee.org/document/10382551) · [GitHub](https://github.com/alper111/attentive-deepsym)

<!-- more -->

Second author. Carried out at the CoLoRs Lab, Boğaziçi University.

<div style="text-align: center; margin: 2rem 0; width: 100%;">
  <video 
    width="100%" 
    controls 
    preload="metadata"
    style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.15); max-height: 480px; background: #000;">
    <source src="https://aahmetoglu.com/static/relational_deepsym.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p style="font-style: italic; color: #666; margin-top: 0.75rem; font-size: 0.95rem;">
    Multi-object symbol discovery and effect prediction on the simulated UR10 tabletop platform.
  </p>
</div>

## Method

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/DeepSym.png" alt="Relational DeepSym: the encoder and the self-attention module take object features as input and process them in parallel; the encoder outputs an object symbol for each object while the self-attention module outputs query and key vectors used to compute relational symbols, which are aggregated and decoded into per-object effect predictions." style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Fig. 1: The Relational DeepSym architecture. Object symbols and relational symbols are produced in parallel from the same object features, then aggregated with the executed action and decoded into per-object effects.</p>
</div>

The state vector is a set of object poses and types $\{o_1, \dots, o_n\}$, where $n$ varies from sample to sample. The model consists of four components: an encoder that transforms the state vector into fixed-size binary symbolic representations for each object, a self-attention module that outputs query and key vectors for each object, an aggregation function that combines information from multiple objects by multiplying object symbols with relational symbols, and a decoder that predicts the effect of the executed action for each object. The architecture is differentiable and trained end to end to minimize the effect prediction error, so the encoder and the self-attention module are expected to learn symbols and relations useful to the decoder.

**Object symbols.** The encoder processes the objects independently, outputting a set of discrete vectors treated as object symbols. To output a discrete vector without removing the differentiability, the activation of the last layer is set to the Gumbel-sigmoid function. Processing objects independently is what lets the model handle a changing number of objects naturally, which in the original DeepSym could only be achieved by fixing the number of input objects.

**Relational symbols.** The self-attention module processes the same object features to output query and key vectors, and the attention weights are computed as $A = \text{GumbelSigmoid}(QK^T/\sqrt{d})$. This differs from regular self-attention, where a softmax is used, and the modification creates two behaviours: a sigmoid allows multiple attention weights to be active at the same time, whereas in softmax attentions compete with each other; and the Gumbel-sigmoid discretizes the weights while preserving differentiability, which allows them to be treated as relational symbols between objects. Four attention heads are used, modelling different relations.

In the preceding attentive architecture the self-attention module takes the encoder's object symbols as input and directly outputs the aggregated representation, restricting the model to learning attention weights only from the learned symbols. Here they are learned from object features, which makes the relations more general. Those weights were also continuous, and continuous weights cannot be easily expressed as relational symbols between objects.

**Aggregation and effect prediction.** Object symbols are concatenated with the discrete action vector, multiplied by the relational symbols, concatenated across heads and passed to the decoder. Effects are the concatenation of the position change of objects before the pick-up action and after the release action, a representation that filters out the movement from the source location to the target location, so what is modelled is what happens immediately after the pick-up and immediately after the release. No symbolic supervision is given at any point; the symbols are formed solely to minimize the effect prediction error.

## My contributions

I joined this project as a research intern, tasked with getting the preceding attentive architecture to produce the expected results for resubmission. Eight months of experiments established that it could not, for structural reasons rather than for want of tuning, and the relational symbols formulation is what came out of that.

- Built the simulated **UR10 tabletop manipulation environment** and the data, effect and symbol visualizations used throughout the paper.
- Built an **autonomous experimentation pipeline** with custom scheduling and Weights & Biases integration, running 10–50 concurrent training runs scheduled against available VRAM at 80–95% utilization.
- **Tested the preceding attentive architecture** and showed that its failure to differentiate between two stacks built from the same set of objects was structural rather than a matter of tuning. Because attention was computed from the encoder's own symbols, whenever the same relation holds twice in a scene the encoder would have to spend capacity on a unique identifier per object for the model to resolve which pair is interacting.
- From that finding, came up with the idea of using attention heads as directional graphs and **coined the term relational symbols**, since their combination indicates how two objects relate to each other. I did not get a working implementation of it; the self-attention module in the paper is Alper Ahmetoğlu's.
- Ran the **preliminary evaluations** confirming the trained model behaved as intended in simulation, and made the first qualitative observations of what the discrete symbols encoded. The in-depth symbol analysis reported below is Alper Ahmetoğlu's.

## Experiments

The environment consists of a UR10 robot and two to four objects, either short blocks or long blocks. The robot has a single type of high-level action: grasping and releasing an object on top of or near another object. Three datasets containing exactly two, three and four objects are collected, with 120K, 180K and 240K samples, and a fourth combines them into a varying-object-count set. All architectures are trained for 4000 epochs with five repetitions using different seeds.

Reported results are absolute errors summed over all dimensions, in centimetres, averaged over the five runs. Welch's t-test shows significant differences ($p < 0.02$ for all cases) between the proposed method and the others.

| Dataset | Vanilla DeepSym | Attentive DeepSym | Relational DeepSym |
| :--- | :---: | :---: | :---: |
| 2 objects | $$2.22 \pm 0.56$$ | $$0.89 \pm 0.10$$ | $$\boldsymbol{0.50 \pm 0.03}$$ |
| 3 objects | $$3.06 \pm 0.16$$ | $$2.55 \pm 0.09$$ | $$\boldsymbol{1.67 \pm 0.02}$$ |
| 4 objects | $$4.26 \pm 0.68$$ | $$2.75 \pm 0.12$$ | $$\boldsymbol{2.00 \pm 0.04}$$ |
| 2–4 objects | $$2.38 \pm 0.25$$ | $$1.86 \pm 0.12$$ | $$\boldsymbol{1.35 \pm 0.04}$$ |

The variance is also lower than that of the others, indicating that Relational DeepSym is more robust to different seeds. Errors increase as the number of objects increases. This is expected since the number of unique effects increases with the number of objects as the robot creates more complex structures in random exploration; the paper names a guided exploration schedule as a promising future direction, which I pursued from two sides: externally, by having an LLM choose among the robot's available actions in [Developmental Scaffolding with Large Language Models](/publication/2023-icdl-scaffolding) (ICDL 2023), and internally, by deriving the signal from the learner's own predictive uncertainty in my [thesis](/projects/intrinsic_curiosity).

Feeding the predicted effect back into the state vector allows the final state of an action sequence to be predicted. Relational DeepSym is more accurate than the others here, especially in the $z$ axis, the most significant axis in these experiments, showing that the model accounts for the presence of an object on top of another.

## Interpreting the learned symbols

Because the symbols are discrete, the states that activate each of them can be collected and inspected directly.

One object symbol is activated only with long blocks, while the others respond to short blocks; among those, some are activated for short blocks below the grasped object and others for short blocks above it, the positions being relative to the grasped object. These symbol groundings show that the object type and the relative $z$-axis position are the most significant factors in predicting the effect. No symbol is specialized on the $x$-axis position, as it does not bring any additional advantage for the effect prediction.

Among the relational symbols, one is activated only when objects are aligned within the $y$ axis. This suits the environment, since objects are only aligned when they are mostly on top of each other, and the alignment helps the model differentiate between two stacks built from the same set of objects. The remaining relations are activated for a wide range of relative positions and object types, suggesting they are not as significant.

The next step named in the paper is to convert the learned symbols into PDDL operators for domain-agnostic planning, which would remove the cascading of errors in action sequence prediction and allow a fast search in symbolic space without a neural network.

### BibTeX
```bibtex
@article{Ahmetoglu_2024,
   title={Discovering Predictive Relational Object Symbols With Symbolic Attentive Layers},
   volume={9},
   ISSN={2377-3774},
   url={http://dx.doi.org/10.1109/LRA.2024.3350994},
   DOI={10.1109/lra.2024.3350994},
   number={2},
   journal={IEEE Robotics and Automation Letters},
   publisher={Institute of Electrical and Electronics Engineers (IEEE)},
   author={Ahmetoglu, Alper and Celik, Batuhan and Oztop, Erhan and Ugur, Emre},
   year={2024},
   month=Feb,
   pages={1977--1984} }
```

<style>
  /* Reduce side padding for the main content area */
  #main {
    
    padding-right: 1em !important;
    max-width: 95% !important; /* Allows the content to expand wider */
  }

  /* Optional: If you want to reduce the gap between the sidebar and the content */
  .archive {
    padding-right: 0 !important;
  }
</style>