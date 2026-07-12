---
title: "Developmental Scaffolding with Large Language Models"
collection: publications
category: conferences
authors: "<b>Batuhan Çelik</b>, Alper Ahmetoğlu, Emre Uğur, Erhan Öztop"
permalink: /publication/2023-icdl-scaffolding
date: 2023-10-02
venue: 'IEEE International Conference on Development and Learning (ICDL)'
paperurl: "https://arxiv.org/abs/2309.00904"
---

### Abstract
Exploration and self-observation are key mechanisms of infant sensorimotor development. These processes are further guided by parental scaffolding to accelerate skill and knowledge acquisition. In developmental robotics, this approach has been adopted often by having a human acting as the source of scaffolding. In this study, we investigate whether Large Language Models (LLMs) can act as a scaffolding agent for a robotic system that aims to learn to predict the effects of its actions. To this end, an object manipulation setup is considered where one object can be picked and placed on top of or in the vicinity of another object. The adopted LLM is asked to guide the action selection process through algorithmically generated state descriptions and action selection alternatives in natural language. The simulation experiments that include cubes in this setup show that LLM-guided (GPT3.5-guided) learning yields significantly faster discovery of novel structures compared to random exploration. However, we observed that GPT3.5 fails to effectively guide the robot in generating structures with different affordances such as cubes and spheres. Overall, we conclude that even without fine-tuning, LLMs may serve as a moderate scaffolding agent for improving robot learning, however, they still lack affordance understanding which limits the applicability of the current LLMs in robotic scaffolding tasks.

[arXiv](https://arxiv.org/abs/2309.00904) | [IEEExplore](https://ieeexplore.ieee.org/document/10364374)

## 📺 Exploration & Interactive Breakdown

This study investigates how a Large Language Model can be leveraged as an automated scaffolding agent to guide high-level robot exploration toward hard-to-reach, structurally complex, or statistically improbable physical arrangements. This framework is proposed as an algorithmic solution to **achieve high throughput scaffolding while probing grounded inference capabilities of available LLMs**.

*Note: LLM capabilities have progressed significantly since the publication of this work during the GPT-3.5 era. The results documented below serve as an foundational benchmark of early text-only reasoning models applied to physical scaffolding.*

<div style="text-align: center; margin: 2rem 0; width: 100%;">
  <iframe 
    width="100%" 
    height="640" 
    src="https://www.youtube.com/embed/qLTS8Pt-7Ks" 
    title="Developmental Scaffolding with Large Language Models: Demonstration video" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    referrerpolicy="strict-origin-when-cross-origin" 
    allowfullscreen
    style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
  </iframe>
  <p style="font-style: italic; color: #666; margin-top: 0.75rem; font-size: 0.95rem;">
    LLM-guided pick-and-place task execution loop on the simulated UR10 manipulation platform.
  </p>
</div>

## 🛠️ Methodology & Core Contributions

Instead of executing resource-intensive fine-tuning or relying on dense descriptive embodiment alignments, this framework leverages the native zero-shot reasoning capabilities of LLMs to steer robot interactions toward complex environment configurations. This minimal approach allows us to directly probe the inherent physical understanding of LLMs and evaluate their broader applicability to robotics.

### 1. Token-Efficient Prompt Engineering
To bypass continuous active dialogue streams during live execution loops, a stateless prompting cycle resets at each new scene configuration. The framework programmatically constructs structured context packages combining three primary variables:

* **State Space Mapping ($$S_i$$):** Algorithmic translation of physical objects and spatial coordinates into color-coded natural language tokens (e.g., `the green cube is next to the purple cube`).
* **Interaction Trajectory History ($$H_{1,\dots,i-1}$$):** A chronological digest of previous actions within the current session to ensure temporal conditioning.
* **Bounded Action Windows ($$A_{1,\dots,k}$$):** Dynamically filtered sub-lists containing valid, kinematically executable actions extracted directly from the robot's physical repertoire.

The LLM is prompted broadly to seek an **"interesting outcome"**, implicitly drawing upon its encoded knowledge of human sensorimotor development. Crucially, the model is not explicitly informed that it is controlling a physical robot. To provoke deeper reasoning and stabilize execution selection, the prompt explicitly requires a text explanation before outputting the final choice.

**Example System Prompt:**
```text
[System]: There are some objects on the table. Which manipulation alternative on them yields an interesting outcome? 
Choose one and explain.
Your output should be in the following format:
<reasoning> some sentences </reasoning>
Selected action is : <number of the selected action>
```

**Example user prompt:**
```text
[User]: There is an orange cube, a green cube, a purple cube, a brown sphere, and a light green cube in the current scene.
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

Enforcing the `<reasoning>` block to generate prior to the final action selection token allows the model to **incrementally condition its choices on sequential logic**. Providing the running session history alongside immediate scene text at each exploration step ensures behavioral coherence across multiple steps. 

For instance, once **committing to constructing a tall stack**, the model actively avoids diminishing the stack height if additional vertical choices are unavailable. Conversely, **once peak structural capacity is achieved, the model deconstructs the stack to seek alternative configurations**.

### 3. Grounded Knowledge Auditing

The study provides a stress test of **embodied comprehension of LLMs**. While models effortlessly optimize stacking sequences across uniform geometries like cubes, they exhibit a severe **"cognitive gap"** when spheres are introduced.

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


We benchmarked the LLM-guided scaffolding framework against a **baseline random exploration policy over identical 10-step exploration windows**.

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
    <p>Crucially, no explicit directives instruct the model to increase the tower height. </p>
    <p>
      LLM-scaffolded exploration outperforms the random exploration baseline by focusing early exploration steps on structural accumulation.
      </p>
      <p> In the most complex setup, <b>the random exploration policy fails to achieve the tallest stack</b>, whereas the scaffolded system regularly discovers peak tower heights within minimal operational steps.
    </p>
  </div>
</div>


### Effects of different prompts

<div style="display: flex; align-items: center; justify-content: space-between; gap: 2rem; margin: 2rem 0; flex-wrap: wrap; direction: rtl;">
  <div style="flex: 1; min-width: 320px; direction: ltr;">
    <p>
      We observed that changing a <b>single word</b> in the prompts could yielded dramatic changes in behaviour.
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

When **spheres are introduced** to the environment, GPT's grounding vulnerabilities become apparent. Even under explicit instructions to maximize stack height, the presence of a sphere led to a performance degradation. Qualitative analysis confirmed that the model repeatedly hallucinated the sphere as a stable base. The assistants answer bellow provides an illustration.

<pre><code>[Assistant]: The best action would be to put the blue cube on top of the red sphere.
This is because</code> <code><b>**the red sphere can provide a stable base for the cube, and the cube can sit 
securely on top of the sphere**.</b></code></pre>

<div style="display: flex; align-items: center; justify-content: space-between; gap: 2rem; margin: 2rem 0; flex-wrap: wrap; direction: rtl;">
  <div style="flex: 1; min-width: 320px; direction: ltr;">
    <p>
      Even when the LLM is specifically instructed to creating the tallest stack, introduction of sphere decreased the average stack height by <b>20%</b>.
    </p>
    <p>
      When the LLM is directly asked if a sphere can provide a stable tower it correctly answered `No`.
    </p>
    <p>
      While the <b>model maintains abstract textual knowledge that a sphere is unstable, it fails to transfer this rule when executing active spatial planning</b>.
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

The gap between early text-only models and modern vision-language-action models (VLMs/VLAMs) is profound—particularly regarding embodied knowledge. By integrating direct visual peripherals, modern multi-modal architectures transcend the limitations of text, allowing the system to perceive spatial geometry, self-affordances, and physical constraints. **This sensory grounding fundamentally improves the model's grasp of embodied knowledge**. Re-evaluating developmental parental scaffolding concepts through the lens of these multimoodal foundation models offers a highly promising path toward establishing practical, robust, and self-correcting exploration loops in complex environments.


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