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