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

### Core Contributions

- **Explicit Relational Discretization**: By integrating a Gumbel-Sigmoid bottleneck within a self-attention mechanism, the network forces continuous attention weights into interpretable, binary adjacency matrices ($A \in \{0, 1\}^{N \times N}$). Thus, the decoder is forced to interpret this signal as existance of a specific relation between objects instead of relying on sensory data. The result is self-emergence of intuitive relational symbols such as `on top of` or `the left of`. Moreover, these discrete symbols can be interpreted as a ruleset.

- **Variable-Length Entity Processing**: The model scales to scenes containing an arbitrary number of independent physical objects without requiring structural or parametric reconfiguration. This is achieved by preserving the dimension for number of objects throughout the network alongside the batch dimension.

- **Self-Supervised Grounding**: Symbol formation is guided entirely by an auxiliary forward dynamics task (predicting the continuous displacements $\Delta x, \Delta y, \Delta z$ of objects), capturing environment dynamics with minimal outside supervision.

### My Contributions

- Designed and executed the simulated **UR10 tabletop manipulation environment** with its effect and data visualizations. 

- Created an **autonomous experimentation pipeline** with custom scheduling and WandB cloud integration, facilitated rapid experimentation(10-50 runs per night, automatically scheduled considering the available VRAM, 80-95% VRAM usage).

- Throughly **tested the previously proposed attentive deepsym architecture** and identified its shortcomings in predicting effects in scenes containing two identical structures. Please note that while the paper uses 4 object environments, these models are designed with 12 objects in mind, which our future work focused on.

- Using these findings, devised the **relational symbols** concept and developed the self-attention bottleneck architecture.

- Conducted post-training probing analysis to verify the emergent semantics of the discrete latent vectors

## Experimental Results




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

\```