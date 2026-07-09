---
title: "Developmental Scaffolding with Large Language Models"
collection: publications
category: conferences
authors: "<b>Batuhan Çelik</b>, Alper Ahmetoğlu, Emre Uğur, Erhan Öztop"
permalink: /publication/2023-icdl-scaffolding
date: 2023-10-02
venue: 'IEEE International Conference on Development and Learning (ICDL)'
paperurl : "https://arxiv.org/abs/2309.00904"
---

### Abstract
Exploration and self-observation are key mechanisms of infant sensorimotor development. These processes are
further guided by parental scaffolding to accelerate skill and
knowledge acquisition. In developmental robotics, this approach
has been adopted often by having a human acting as the source of
scaffolding. In this study, we investigate whether Large Language
Models (LLMs) can act as a scaffolding agent for a robotic
system that aims to learn to predict the effects of its actions.
To this end, an object manipulation setup is considered where
one object can be picked and placed on top of or in the
vicinity of another object. The adopted LLM is asked to guide
the action selection process through algorithmically generated
state descriptions and action selection alternatives in natural
language. The simulation experiments that include cubes in this
setup show that LLM-guided (GPT3.5-guided) learning yields
significantly faster discovery of novel structures compared to
random exploration. However, we observed that GPT3.5 fails to
effectively guide the robot in generating structures with different
affordances such as cubes and spheres. Overall, we conclude
that even without fine-tuning, LLMs may serve as a moderate
scaffolding agent for improving robot learning, however, they still
lack affordance understanding which limits the applicability of
the current LLMs in robotic scaffolding tasks.

[Arxiv](https://arxiv.org/abs/2309.00904), [IEEExplore](https://ieeexplore.ieee.org/document/10364374)

### BibTeX
```bibtex
@inproceedings{Celik_2023,
   title={Developmental Scaffolding with Large Language Models},
   url={http://dx.doi.org/10.1109/ICDL55364.2023.10364374},
   DOI=10.1109/icdl55364.2023.10364374,
   booktitle={2023 IEEE International Conference on Development and Learning (ICDL)},
   publisher={IEEE},
   author={Celik, Batuhan and Ahmetoglu, Alper and Ugur, Emre and Oztop, Erhan},
   year={2023},
   month=Nov, pages={396–402} }
\```