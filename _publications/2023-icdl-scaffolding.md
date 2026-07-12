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

### 2. Chain-of-Thought Reasoning

By forcing the LLM to output its <reasoning> block before finalizing the action selection, and providing session history and interaction at each step of the exploration, we allowed the LLM to increment upon its reasoning. This ensured coherency across multiple actions. 

For illustration, once deciding on creating a tall stack, the LLM actively avoided decreasing stack height if further stacking operations were not available. However, once the tallest stack is achieved, GPT3.5 dismantled the stack to look for other `interesting` configurations.

### 3. Grounded Knowledge Auditing

The paper provides a thorough test of real-world physical comprehension of GPT3.5(probed by us) and othher models (probed by other works). 

While the GPT effortlessly optimize stacking sequences across uniform primitives like cubes, they exhibit a severe **"cognitive gap"** regarding mixed-physics affordances. When introduced to combinations of cubes and spheres, models routinely choose paths that place cubes on top of spheres—erroneously stating that a sphere acts as a stable foundation block. However, if asked directly `If spheres can be used as a stable base for a tower?` the model gives the correct answer, indicating an inability to utilize its inherent grounded knowledge.

## 💻 My Contributions

- **Performed a comprehensive literature review of LLM-robotics applications** and developmental parental scaffolding theories.

- **Co-developed the PyBullet-based UR10 manipulator simulation**, including high-level discrete pick-and-place action spaces.

- **Designed the zero-shot token-efficient state serialization layer**, converting physical scene configurations directly into compact LLM-consumable history inputs.

- **Engineered experiment setups** comparing language-driven high-gain information paths against standard stochastic exploration methods.

- **Created the data visualizations, figures**, and the promotional video of the paper.

- **Uncovered systemic structural hallucinations within GPT-3.5's physical world planning models**, validating semantic failure modes via targeted exploratory tasks.

- **Prepared the first draft and implemented alterations of my collegues**, presenting my work and literature review while ensuring a coherent manuscript using my 2 professor's inputs.

- **Took corresponding author responsilibities**, answered reviews of the ICDL comitee and performed necessary changes on the final draft. 

## 📊 Experimental Results


We compared the LLM scaffolding **against de-facto random exploration policy over 10-step exploration windows**.

### Tower Construction Efficiency

<div style="display: flex; align-items: center; justify-content: space-between; gap: 2rem; margin: 2rem 0; flex-wrap: wrap;">

<div style="flex: 1; min-width: 320px; text-align: center;">
    <img 
      src="/images/scaffolding_tower_results.png" 
      alt="Comparison of Maximum Object Height across Exploration Steps" 
      style="width: 100%; border-radius: 6px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"
    />
    <p style="font-style: italic; color: #666; margin-top: 0.5rem; font-size: 0.85rem;">
      Fig. 1: Evolution of the maximum height achieved across exploration steps. The solid lines represent the mean maximum height across independent experimental runs.
    </p>
  </div>
  <div style="flex: 1; min-width: 320px;">
    
    <p>
      LLM-scaffolding was evaluated by measuring the <b>maximum tower height achieved (representing rare, hard-to-reach environmental states) over 40 interaction sessions</b>. 
    </p>
    <p>Notably, nothing in the prompts urges the model to increase the tower height. </p>
    <p>
      LLM-scaffolded exploration outperformes the random exploration baseline by focusing early action choices on structural accumulation.
      </p>
      <p> In the most complex setup, <b>the random exploration policy fails to achieve the tallest stack</b>, whereas the scaffolded system regularly discovers peak tower heights within minimal operational steps.
    </p>
  </div>
</div>


### Effects of different prompts

<div style="display: flex; align-items: center; justify-content: space-between; gap: 2rem; margin: 2rem 0; flex-wrap: wrap; direction: rtl;">
  <div style="flex: 1; min-width: 320px; direction: ltr;">
    <p>
      We observed changing a <b>single word</b> in the prompts could vastly change the results.
    </p>
    <p>
      Changing the word <b><u>interesting</u></b> to <b><u>novel</u></b> significantly decreased the average tower height.
    </p>
  </div>

  <div style="flex: 1; min-width: 320px; text-align: center; direction: ltr;">
    <img 
      src="/images/scaffolding_differentadjectives.png" 
      alt="The Affordance Blindspot Failure Modes" 
      style="width: 100%; border-radius: 6px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"
    />
    <p style="font-style: italic; color: #666; margin-top: 0.5rem; font-size: 0.85rem;">
      Fig. 2: Effects of different adjectives on the tower heights in a 5 cubes 2 positions setting.
    </p>
  </div>
</div>

### 3. Different Affordances

When **spheres are introduced** to the environment, GPT's inability to use grounded knowledge emerged. Even when we tasked the LLM with creating the tallest stack we observed a significant decrease in the stack height. When probed rigirously we observed GPT to repeatedly hallucinate the sphere as a stable base. The assistants answer bellow provides an illustration.

<pre><code>[Assistant]: The best action would be to put the blue cube on top of the red sphere.
This is because</code> <code><b>**the red sphere can provide a stable base for the cube, and the cube can sit 
securely on top of the sphere**.</b></code></pre>

<div style="display: flex; align-items: center; justify-content: space-between; gap: 2rem; margin: 2rem 0; flex-wrap: wrap; direction: rtl;">
  <div style="flex: 1; min-width: 320px; direction: ltr;">
    <p>
      Even when the LLM is specifically instructed to creating the tallest stack, introduction of sphere decreased the average stack height by <b>20%</b>.
    </p>
    <p>
      When the LLM is directly asked if a sphere can provide a stable tower it correctly answered no.
    </p>
    <p>
      However, it repeatedly failed to utilize this grounded inference during the tower creation task.
    </p>
  </div>

  <div style="flex: 1; min-width: 320px; text-align: center; direction: ltr;">
    <img 
      src="/images/scaffolding_towercreation.png" 
      alt="The Affordance Blindspot Failure Modes" 
      style="width: 100%; border-radius: 6px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"
    />
    <p style="font-style: italic; color: #666; margin-top: 0.5rem; font-size: 0.85rem;">
      Fig. 3: Comparison of average heights in different environments during LLM scaffolded sessions with tower creation task and the corresponding system prompt.
    </p>
  </div>
</div>

### Future Work

I recognize the **difference between current LLMs and the GPT 3.5 capabilities is paramount**, the most important one being **visual input processing**. After this work, grounded inference capabilities of LLMs increased significantly and describing scenes and actions became way easier due to visual inputs. Therefore, I believe a repatition of these experiments could be fruitful, or even implementable practically complex environments. 


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