---
title: "Developmental Scaffolding with Large Language Models"
collection: publications
category: conferences
authors: "<b>Batuhan Çelik</b>, Alper Ahmetoğlu, Emre Uğur, Erhan Öztop"
permalink: /publication/2023-icdl-scaffolding
date: 2023-11-09
venue: 'IEEE International Conference on Development and Learning (ICDL)'
paperurl: "https://arxiv.org/pdf/2309.00904"
description: "ICDL 2023. Can an LLM act as a parental scaffolding agent for a robot learning to predict its own action effects? GPT-3.5 guidance finds novel structures faster than random exploration, but fails on objects whose affordances differ from cubes."
---

### Abstract
Exploration and self-observation are key mechanisms of infant sensorimotor development. These processes are further guided by parental scaffolding to accelerate skill and knowledge acquisition. In developmental robotics, this approach has been adopted often by having a human acting as the source of scaffolding. In this study, we investigate whether Large Language Models (LLMs) can act as a scaffolding agent for a robotic system that aims to learn to predict the effects of its actions. To this end, an object manipulation setup is considered where one object can be picked and placed on top of or in the vicinity of another object. The adopted LLM is asked to guide the action selection process through algorithmically generated state descriptions and action selection alternatives in natural language. The simulation experiments that include cubes in this setup show that LLM-guided (GPT3.5-guided) learning yields significantly faster discovery of novel structures compared to random exploration. However, we observed that GPT3.5 fails to effectively guide the robot in generating structures with different affordances such as cubes and spheres. Overall, we conclude that even without fine-tuning, LLMs may serve as a moderate scaffolding agent for improving robot learning, however, they still lack affordance understanding which limits the applicability of the current LLMs in robotic scaffolding tasks.

[arXiv](https://arxiv.org/abs/2309.00904) · [IEEE Xplore](https://ieeexplore.ieee.org/document/10364374)

<!-- more -->

First author and corresponding author, CoLoRs Lab, Boğaziçi University.

<div style="text-align: center; margin: 2rem 0; width: 100%;">
  <iframe 
    width="100%" 
    height="640" 
    src="https://www.youtube.com/embed/qLTS8Pt-7Ks" 
    title="Developmental Scaffolding with Large Language Models: demonstration video" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    referrerpolicy="strict-origin-when-cross-origin" 
    allowfullscreen
    style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
  </iframe>
  <p style="font-style: italic; color: #666; margin-top: 0.75rem; font-size: 0.95rem;">
    LLM-guided pick-and-place sessions on the simulated UR10 tabletop platform.
  </p>
</div>

## Motivation

Random exploration is common practice in reinforcement learning, navigation and manipulation, but in environments where the action-to-effect mapping is non-linear, stochastic or redundant, hard-to-reach states may never be experienced. In our previous work on [effect prediction and planning](/publication/2023-relational), composite structures such as bridges, T-shaped and U-shaped structures become possible as the number of objects grows and the action set is extended. Constructing them requires performing a series of correct actions, which becomes less and less likely to experience with random exploration as the complexity of the setup increases.

Extracting the required knowledge from humans through imitation or parental scaffolding is one remedy, but data collection from humans is a labor-intensive process for complex learning tasks. Being trained on internet-scale data, LLMs can be utilized as knowledge bases instead. Grounded knowledge is scarce on the internet, however, and eliciting grounded inferences normally requires conditioning the model for the agent's embodiment, which brings an immense computation cost. Here the LLM is used solely as a light knowledge base: it selects among actions the robot can already execute, so no descriptive embodiment alignment is applied, and the sensorimotor data collected during scaffolded sessions remains grounded regardless of the reasoning that produced it.

## Method

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/developmental.png" alt="One interaction step: the object configuration, the session history and the executable action choices are described in an algorithmically generated natural-language prompt, sent to GPT-3.5, and the action named in its fixed-format reply is executed in simulation, producing the next state." style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Fig. 1: The scaffolding loop. The LLM sees only text and returns an index; every other stage is algorithmic.</p>
</div>

**The scaffolding loop.** Scaffolding is tested in sessions of ten object interactions in which the simulated robot receives action suggestions from the LLM. Each session begins with various numbers of cubes and spheres randomly initialized on the table. At each step the current object configuration and the possible action choices are described to the LLM in natural language using algorithmically generated prompts. The output is produced in a fixed format that can be easily parsed, and the selected action is executed. Providing the choices from the robot's action repertoire ensures that the selection will be within its execution capability. Each session is repeated 40 times to account for the stochasticity in initial object placement and choice generation.

**Prompt definition.** In order not to introduce any bias towards a specific selection, the task definition in the system prompt simply consists of selecting an action with an interesting outcome. The model is also conditioned to provide the reasoning behind its selection before making a decision, since generating the reasoning first increases the success rate of the GPT in robotics tasks. The user prompt is generated as $$\langle S_i \rangle \langle H_{1,\dots,i-1} \rangle \langle A_{1,\dots,k} \rangle$$: the current configuration, listing the objects and the spatial relations between them with colours as unique identifiers, the session history, and the possible actions. Rather than conducting a dialogue during the whole session, a new dialogue is initialized for each configuration and the history is summarized in $$H$$.

```text
[System]: There are some objects on the table. Which manipulation alternative on them yields an interesting outcome? 
Choose one and explain.
Your output should be in the following format:
<reasoning> some sentences </reasoning>
Selected action is : <number of the selected action>
```

```text
[User]: There is an orange cube, a green cube, a purple cube, a brown sphere, and a light green cube in the current scene.
the light green cube is stacked on the purple cube.
Previously executed actions:
Put the light green cube on top of the purple cube
...
Possible actions:
1 ) Put the green cube in front of the orange cube
2 ) Put the orange cube on top of the light green cube
...
```

All experiments use `gpt-3.5-turbo` at temperature 0.

## My contributions

- Wrote the survey of LLM-robotics grounding strategies in the introduction, which reviewers singled out for its coverage.
- Co-developed the PyBullet UR10 environment and its discrete pick-and-place action space.
- Devised the token-efficient prompting strategy, including the state description generation and the history summarization that removes the need for a dialogue across a session.
- Designed and ran the experiments against the random exploration baseline, and produced the figures and the video.
- Identified the disregard of sphere affordances and the hallucinated stacking relations through careful examination of the collected dialogues.
- Wrote the first draft, incorporated co-author revisions, and handled the ICDL review response as corresponding author.

## Results

A purely random action selection strategy is used as the baseline. The visitation frequency to hard-to-reach states such as tall towers measures the exploration efficacy gained by LLM-based scaffolding.

### Comparison with the random baseline

<div style="display: flex; align-items: center; justify-content: space-between; gap: 2rem; margin: 2rem 0; flex-wrap: wrap;">
<div style="flex: 1; min-width: 320px; text-align: center;">
    <img 
      src="/images/scaffolding_tower_results.png" 
      alt="Tower height distributions across ten interactions under random and scaffolded exploration, in three environment settings of incremental difficulty." 
      style="width: 100%; border-radius: 6px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"
    />
    <p style="font-style: italic; color: #666; margin-top: 0.5rem; font-size: 0.85rem;">
      Fig. 2: Comparison of tower heights between random and scaffolded exploration in environment settings with incremental difficulty: four cubes and two positions, then a fifth cube, then a third proximity location.
    </p>
  </div>
  <div style="flex: 1; min-width: 320px;">
    <p>
      Nothing in the prompt asks for a tall tower. LLM scaffolded exploration discovers the tallest possible tower much earlier than random exploration in all three settings. As the complexity of the environment increases, the probability of visiting hard-to-reach states during random exploration decreases: in the most complex setting, random exploration fails to reach a tower of height five, while scaffolding reaches it in eight interaction sessions.
    </p>
    <p>
      This trend does not continue till the end of a session. Tall towers lose their novelty once encountered, so upon creating tall structures at the beginning of an episode the GPT proceeds to dismantle them in order to explore proximity relations, and a decrease in average height is observed in the later stages of exploration.
    </p>
  </div>
</div>

### Effects of different prompts

<div style="display: flex; flex-direction: row-reverse; align-items: center; justify-content: space-between; gap: 2rem; margin: 2rem 0; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 320px;">
    <p>
      The experiments above requested actions yielding an "interesting" outcome. Replacing that adjective with "novel" in the system prompt produces a notable difference in the resulting tower heights.
    </p>
    <p>
      Conditioned to yield a novel outcome, GPT-3.5 focuses on the history and actively avoids actions similar to the previously executed ones. Performing the stacking operation four consecutive times is therefore unlikely, resulting in a low visit frequency to states with complex structures. These results show the importance of selecting the appropriate words when minimal prompting is used.
    </p>
  </div>
  <div style="flex: 1; min-width: 320px; text-align: center;">
    <img 
      src="/images/scaffolding_differentadjectives.png" 
      alt="Tower height distributions across ten interactions for the interesting and novel adjectives, in the five cubes and two positions setting." 
      style="width: 100%; border-radius: 6px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"
    />
    <p style="font-style: italic; color: #666; margin-top: 0.5rem; font-size: 0.85rem;">
      Fig. 3: Effects of different adjectives on the tower heights in a 5 cubes, 2 positions setting.
    </p>
  </div>
</div>

### Exploiting the LLM's affordance knowledge

Cubes are inherently easily graspable and stackable, so manipulating them does not require extensive knowledge regarding affordances. A sphere increases environmental complexity: stacking cubes on top of spheres results in the cubes dropping to the table surface, and the sphere must always occupy the topmost position of a tower. Instructed to create the highest possible tower, GPT-3.5 nevertheless shows a continuing preference towards placing spheres in middle positions, as this action immediately increases the height of the tower, and states that the sphere is a stable base to provide logical reasoning for these actions.

<pre><code>[Assistant]: The best action would be to put the blue cube on top of the red sphere.
This is because the red sphere can provide a stable base for the cube, and the cube
can sit securely on top of the sphere.</code></pre>

Asked directly whether a cube can be balanced on top of a sphere, GPT-3.5 indicates that it may not be feasible in the real world. Asked instead to generate the steps for building a high tower from a state description, the resulting steps are strongly biased toward the order of the objects appearing in it: if the sphere is not the first or the last object, it is eagerly placed in a mid position. The affordances of the sphere are disregarded in the planning task even though the knowledge is available on request.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/scaffolding_towercreation.png" alt="Tower height distributions for the tower creation task, comparing five cubes against four cubes and one sphere." style="width:80%; display:block; margin:20px auto; border-radius: 6px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Fig. 4: Comparison of average heights in different environments during LLM scaffolded sessions with the tower creation task.</p>
</div>

## Discussion

GPT-4 existed at the time but no API access was available to us, so it could not be driven from the interaction loop. Tested by hand in the tower creation task, GPT-4 was capable of placing the sphere in the top position regardless of the sphere's appearance order in the prompt, and some trials resulted in its discarding the sphere by stating it would not be stable even in the top position. These observations indicate a clear difference between the grounded reasoning capabilities of GPT-3.5 and GPT-4, and encourage future work on the exploration scaffolding capability of more powerful multimodal systems, in which geometry and affordances are available perceptually rather than through a generated description.

An external knowledge source is not the only route past this exploration bottleneck. My [graduation project](/projects/intrinsic_curiosity) approaches the same problem from the opposite direction, deriving the guidance signal from the learner's own predictive uncertainty rather than from a model that already knows something about the world.

### BibTeX
```bibtex
@inproceedings{Celik_2023,
   title={Developmental Scaffolding with Large Language Models},
   url={http://dx.doi.org/10.1109/ICDL55364.2023.10364374},
   DOI={10.1109/icdl55364.2023.10364374},
   booktitle={2023 IEEE International Conference on Development and Learning (ICDL)},
   publisher={IEEE},
   author={Celik, Batuhan and Ahmetoglu, Alper and Ugur, Emre and Oztop, Erhan},
   year={2023},
   month=Nov, pages={396--402} }
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