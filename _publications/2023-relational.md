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

## Proposed Architecture

![Alternative text description](/images/DeepSym.png)

Relational DeepSym introduces an end-to-end neural pipeline designed to convert sensorimotor data into discrete symbolic representations.

The information flow within the model operates through three synchronized mechanisms:
1. **Categorical Entity Discretization:** Object features and locations extracted from the scene are passed through a MLP. **Gumbel-Sigmoid activation layer** is used to generate discrete latent vectors .
2. **Relational Symbols:** Concurrently, object features and locations feed into a modified self-attention block. The network routes the standard query ($Q$) and key ($K$) continuous dot-products through a structural Gumbel-Sigmoid layer. This mathematical constraint forces continuous attention fields to settle into sparse, binary adjacency matrices ($$A \in \{0, 1\}^{N \times N}$$), uncovering explicit relational links (e.g., spatial stacking or lateral orientation) without external supervision.
3. **Discrete Action Interfacing:** The robot interacts with the tabletop environment utilizing a predefined repertoire of macro-actions (e.g., `place object A left of object B`). Because displacement and targets are structurally deterministic, actions are injected as categorical vectors. 

By calculating the continuous matrix multiplication of the binarized relations, the learned object properties, and the input action vectors, the decoder optimizes an auxiliary forward dynamics module. The **model learns valid symbols solely by attempting to minimize the prediction error** of continuous environmental displacements ($$\Delta x, \Delta y, \Delta z$$).

## Core Contributions

- **Explicit Relational Discretization**: By integrating a Gumbel-Sigmoid bottleneck within a self-attention mechanism, the network forces continuous attention weights into interpretable, binary adjacency matrices ($$A \in \{0, 1\}^{N \times N}$$). Thus, the decoder is forced to interpret this signal as the existence of a specific relation between two objects. This rich representation layer relieves the encoder from interpreting object-object relations and allows it to focus entirely on object-specific affordances. Concurrently, relational symbols can be interpreted as a self-emerging relation graph, capturing complex multi-object interactions. The result is the self-emergence of intuitive relational symbols—such as `on top of` or `to the left of`—which can describe complex scenes when used in conjunction.
  
  As a result, object-specific and relational symbols allow us to construct semantic binary representations of physical environments directly from raw sensorimotor data.
  
  Notably, this architecture is natively scaled to capture interactions containing more than 4 objects. While empirical evaluations within the paper are bounded to 4–5 object setups due to data scaling and baseline constraints, future work focus on evaluating scalability across significantly higher object numbers.

- **Variable-Length Entity Processing**: The model scales to scenes containing an arbitrary number of independent physical objects without requiring structural or parametric reconfiguration. This is achieved by explicitly preserving the dimension representing the total number of objects throughout the network layers, processed symmetrically alongside the standard batch dimension.

- **Self-Supervised Grounding**: Symbol formation is guided entirely by an auxiliary forward dynamics task (predicting the continuous displacements $$\Delta x, \Delta y, \Delta z$$ of objects), capturing complex environment dynamics with minimal outside supervision.

## My Contributions

- Designed and implemented the simulated **UR10 tabletop manipulation environment** experiments with their data visualizations. 

- Created an **autonomous experimentation pipeline** with custom scheduling and WandB cloud integration, facilitated rapid experimentation(10-50 runs per night, automatically scheduled considering the available VRAM, 80-95% VRAM usage).

- Throughly **tested the previously proposed attentive deepsym architecture** and identified its shortcomings in predicting effects in scenes containing two identical structures. Please note that while the paper uses 4 object environments, these models are designed with 12 objects in mind, which our future work focused on.

- Using these findings, **devised the relational symbols** concept and co-developed the self-attention bottleneck architecture.

- Conducted **post-training analysis to verify the emergent semantics of the discrete latent vectors**.

## Experimental Results

The framework was benchmarked against leading symbol discovery baselines across environments of increasing complexity. Relational DeepSym demonstrated a notable reduction in Mean Squared Error (MSE) when mapping multi-object spatial dynamics:

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

