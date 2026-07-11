---
title: "Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers"
collection: publications
category: manuscripts
authors: "Alper Ahmetoğlu, <b>Batuhan Çelik</b>, Erhan Öztop, Emre Uğur"
permalink: /publication/2023-relational
date: 2024-01-08
venue: 'IEEE Robotics and Automation Letters (RA-L)'
paperurl : "https://arxiv.org/abs/2309.00889"
---

### Abstract
In this paper, we propose and realize a new deep learning architecture for discovering symbolic representations for objects and their relations based on the self-supervised continuous interaction of a manipulator robot with multiple objects on a tabletop environment. The key feature of the model is that it can handle a changing number number of objects naturally and map the object-object relations into symbolic domain explicitly. In the model, we employ a self-attention layer that computes discrete attention weights from object features, which are treated as relational symbols between objects. These relational symbols are then used to aggregate the learned object symbols and predict the effects of executed actions on each object. The result is a pipeline that allows the formation of object symbols and relational symbols from a dataset of object features, actions, and effects in an end-to-end manner. We compare the performance of our proposed architecture with state-of-the-art symbol discovery methods in a simulated tabletop environment where the robot needs to discover symbols related to the relative positions of objects to predict the observed effect successfully. Our experiments show that the proposed architecture performs better than other baselines in effect prediction while forming not only object symbols but also relational symbols. Furthermore, we analyze the learned symbols and relational patterns between objects to learn about how the model interprets the environment. Our analysis shows that the learned symbols relate to the relative positions of objects, object types, and their horizontal alignment on the table, which reflect the regularities in the environment.

[Arxiv](https://arxiv.org/abs/2309.00889), [IEEExplore](https://ieeexplore.ieee.org/document/10382551)

## 📺 Promotional Video and Model Breakdown

I strongly suggest watching this video for a better understanding of this paper. If you do so, please jump to **My Contributions** section.

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
    Autonomous multi-object symbol discovery and effect prediction rollouts on the simulated UR10 tabletop manipulation platform.
  </p>
</div>
 
## 🛠️ Methodology & Core Contributions

![Relational DeepSym Pipeline Overview](/images/DeepSym.png)

Relational DeepSym introduces an end-to-end neural pipeline designed to convert continuous sensorimotor experience into grounded, discrete symbolic representations in a self supervised manner.

### 1. Categorical Entity Discretization & Variable-Length Processing
Object features and spatial locations extracted from the scene are passed through a shared MLP. A **Gumbel-Sigmoid activation layer** is utilized to encode object properties into discrete latent feature vectors. 

* **Variable-Length Scaling:** Unlike standard architectures constrained by rigid input dimensions, this model **scales to scenes containing an arbitrary number of independent physical objects without structural or parametric reconfiguration**. This is achieved by explicitly preserving the entity count dimension throughout the network layers, processing it symmetrically alongside the batch dimension. By decoupling the encoder from object-to-object interactions, the network can focus entirely on extracting intrinsic, object-specific affordances.

### 2. Explicit Relational Discretization
Concurrently, entity features and locations feed into a **modified self-attention block**. The network discretize the standard query ($$Q$$) and key ($$K$$) dot-products through **Gumbel-Sigmoid** activation.

* **Emergent Relational Graphs:** This mathematical constraint forces continuous attention fields to settle into sparse, binary adjacency matrices ($$A \in \{0, 1\}^{N \times N}$$), compelling the decoder to interpret the signal as existence or absence of an explicit rule-based link. This relieves the entity encoder from tracking multi-object spatial dynamics while allowing for the self-emergence of an **intuitive/interpretable relational graph** (capturing concepts like `on top of` or `to the left of`). 
* **Scene Semantic Scaling:** Used in conjunction, these property and relational symbols construct a full semantic binary representation of physical environments from raw sensorimotor data. While empirical evaluations within the paper are bounded to 4–5 object setups due to data scaling and baseline constraints, the underlying math natively scales to capture complex interactions among significantly higher object numbers(tested up to 12 in future work).

### 3. Discrete Action Interfacing & Self-Supervised Grounding
The robot interacts with the tabletop environment utilizing a predefined repertoire of discrete macro-actions (e.g., `place object A left of object B`). Because displacement and targets are structurally deterministic, actions are injected as categorical vectors. 

* **Forward Dynamics Grounding:** By calculating the continuous matrix multiplication of the binarized relations, the learned object properties, and the input action vectors, the decoder optimizes a forward dynamics module. The model grounds its symbols without human labels or outside supervision; valid symbols are learned solely by attempting to minimize the prediction error of continuous environmental displacements ($$\Delta x, \Delta y, \Delta z$$). Then the learned symbols can be converted into rulesets for traditional planning methods like PDDL.

## 💻 My Contributions

- Designed and implemented the simulated **UR10 tabletop manipulation environment** experiments with their data, effect, and symbol visualizations. 

- Created an **autonomous experimentation pipeline** with custom scheduling and WandB cloud integration, facilitated rapid experimentation(10-50 concurrent training runs, automatically scheduled considering the available VRAM, 80-95% VRAM usage).

- Throughly **tested the previously proposed attentive deepsym architecture** and identified its shortcomings in encoding scenes containing two identical structures.

- Using these findings, **devised the relational symbols** concept and co-developed the self-attention module.

- Conducted **post-training analysis to verify the emergent semantics of the discrete latent vectors**.

## 📊 Experimental Results

The framework was benchmarked against our previous symbol discovery baselines across environments of increasing complexity. Relational DeepSym demonstrated a notable reduction in MSE when mapping multi-object spatial dynamics:

| Dataset Configuration | Vanilla DeepSym MSE (cm) | Attentive DeepSym MSE (cm) | Relational DeepSym MSE (cm) |
| :--- | :---: | :---: | :---: |
| **2-Object Environment** | $$2.22 \pm 0.56$$ | $$0.89 \pm 0.10$$ | **$$\boldsymbol{0.50 \pm 0.03}$$** |
| **3-Object Environment** | $$3.06 \pm 0.16$$ | $$2.55 \pm 0.09$$ | **$$\boldsymbol{1.67 \pm 0.02}$$** |
| **4-Object Environment** | $$4.26 \pm 0.68$$ | $$2.75 \pm 0.12$$ | **$$\boldsymbol{2.00 \pm 0.04}$$** |
| **Mixed Scenes (2–4 Objects)** | $$2.38 \pm 0.25$$ | $$1.86 \pm 0.12$$ | **$$\boldsymbol{1.35 \pm 0.04}$$** |


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
   month=Feb, pages={1977–1984} }

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

