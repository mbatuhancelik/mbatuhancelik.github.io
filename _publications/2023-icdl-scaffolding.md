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


## 📺 Exploration & Interactive Breakdown

This study investigates how a Large Language Model can be leveraged as an automated scaffolder to guide high-level robot exploration toward hard-to-reach, structurally complex, or improbable physical arrangements. This study is suggested to relieve the **data collection problem of Relational DeepSym**.

Notably **capabilities of LLMs improved significantly since this paper released** in ChatGPT 3.5 era. Please judge accordingly.

<div style="text-align: center; margin: 2rem 0; width: 100%;">
  <iframe width="1138" height="640" src="https://www.youtube.com/embed/qLTS8Pt-7Ks" title="Developmental Scaffolding with Large Language Models: Demonstration video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  <p style="font-style: italic; color: #666; margin-top: 0.75rem; font-size: 0.95rem;">
    LLM-guided pick-and-place task execution loop on the simulated UR10 manipulation platform.
  </p>
</div>

## 🛠️ Methodology & Core Contributions

Instead of executing resource-intensive fine-tuning or relying on dense descriptive embodiment alignments, this framework uses the existing foundation-level reasoning of LLMs to steer robot interaction towards hard-to-reach environment configurations.

This simple approach allowed us to probe embodied understanding of LLMs and their wide spread applicability to robotics. 

### 1. Token-Efficient Prompt Engineering

To bypass continuous active dialogue streams during live execution loops, a stateless prompting cycle resets at each new scene configuration. The framework programmatically constructs structured prompts combining three primary variables:

* **State Space Mapping ($$S_i$$):** Algorithmic translation of physical objects and spatial coordinates into color-coded natural language tokens (e.g., `the green cube is next to the purple cube`).
* **Interaction Trajectory History ($$H_{1,\dots,i-1}$$):** A chronological digest of previous actions to ensure temporal conditioning.
* **Bounded Action Windows ($$A_{1,\dots,k}$$):** Dynamically filtered sub-lists containing valid, kinematically executable actions extracted directly from the robot's physical repertoire.

The LLM is simply instructed to seek an interesting outcome and is expected to refer to its knowledge on sensorimotor development of humans. The LLM does not know it controls a robot.

As an old prompting strategy we requested an explanation regarding action selection to provoke deeper reasoning.

An example system prompt:
```text
[System]: There are some objects on the table. Which ma-
nipulation alternative on them yields an interesting outcome?
Choose one and explain.
Your output should be in the following format:
<reasoning> some sentences </reasoning>
Selected action is : <number of the selected action>
```

An example user prompt:
```text
[User]: There is an orange cube, a green cube, a purple cube, a
brown sphere, and a light green cube in the current scene.
the green cube is next to the purple cube.
the brown sphere is in front of the purple cube.
the light green cube is stacked on the purple cube.
Previously executed actions:
Put the brown sphere in front of the purple cube
Put the green cube next to the purple cube
Put the light green cube on top of the purple cube
...
Possible actions:
1 ) Put the green cube in front of the orange cube
2 ) Put the brown sphere next to the light green cube
3 ) Put the orange cube on top of the light green cube
...
```


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