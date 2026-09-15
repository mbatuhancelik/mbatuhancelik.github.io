---
permalink: /
title: "Batuhan Çelik"
author_profile: true
description: "Batuhan Çelik — neurosymbolic robot learning: discovering discrete, compositional symbols from sensorimotor data, and letting curiosity decide what data to collect. RA-L 2024, ICDL 2023. Applying for master's/PhD admission, Fall 2027."
redirect_from: 
  - /about/
  - /about.html
---

I am applying for master's and PhD admission for **Fall 2027**. I work on neurosymbolic robot learning: how an agent can discover discrete, compositional symbols from its own sensorimotor experience, and how it should choose which experience to collect.

I hold a B.S. in Computer Engineering from Boğaziçi University (GPA **3.68**/4.0, Jan 2025). I spent most of it as an undergraduate researcher at the **Cognitive Learning and Robotics Lab (CoLoRs)** — faculty supervision from **Assoc. Prof. Emre Uğur**, day-to-day mentorship from **Alper Ahmetoğlu**, then a PhD candidate — and a summer at Osaka University's **Symbiotic Intelligent Systems Research Center (SISReC)** under **Prof. Erhan Öztop**. That produced two papers, [RA-L 2024](/publication/2023-relational) and [ICDL 2023](/publication/2023-icdl-scaffolding), and a thesis on curiosity-driven exploration. Since then I have taken freelance work on applied AI systems — conversational agents, and a realtime AI streamer — while reading into the causal representation learning literature.

The through-line is representations that are structured enough to plan over and grounded enough to be learned without labels. Robotics has been my testbed, but the questions are not specific to it, and I would as readily pursue them in **visual question answering**, **reinforcement learning**, or **multimodal models** as on a manipulator.

---

## What I want to work on next

Relational DeepSym learns symbols that predict effects. It does not learn symbols that survive intervention — and under passive data those two things are indistinguishable. A model that predicts "the tower falls" from a correlated visual cue and a model that has actually represented the support relation score identically on a held-out test set, and behave very differently the first time a robot pushes something.

Curiosity-driven exploration is where I think that gap can be closed, because an agent choosing its own actions is already running interventions — the learning rule just doesn't treat them as such. What I want to spend a PhD on is making it treat them as such: using the intervention structure that active exploration generates for free as a supervision signal for identifying causal, rather than merely predictive, symbols.

I should be direct that this is where I want to go, not where I have been. I have no published work in causal inference or causal representation learning. Over the past year I have read into it seriously — identifiability, interventional data, and what those results assume — but reading is not results, and I would rather say so here than have it come up later.

Selected reading:

* Judea Pearl, [The Seven Tools of Causal Inference, with Reflections on Machine Learning](https://doi.org/10.1145/3241036) — *Communications of the ACM*, 2019.
* Bernhard Schölkopf, [Causality for Machine Learning](https://doi.org/10.1145/3501714.3501755) — in *Probabilistic and Causal Inference: The Works of Judea Pearl*, ACM, 2022.
* Patrik O. Hoyer, Dominik Janzing, Joris M. Mooij, Jonas Peters, Bernhard Schölkopf, [Nonlinear Causal Discovery with Additive Noise Models](https://proceedings.neurips.cc/paper/2008/hash/f7664060cc52bc6f3d620bcedc94a4b6-Abstract.html) — NeurIPS, 2008.
* Brenden M. Lake, Tomer D. Ullman, Joshua B. Tenenbaum, Samuel J. Gershman, [Building Machines That Learn and Think Like People](https://arxiv.org/abs/1604.00289) — *Behavioral and Brain Sciences*, 2017.
* Artur d'Avila Garcez, Luís C. Lamb, [Neurosymbolic AI: The 3rd Wave](https://arxiv.org/abs/2012.05876) — 2020.
* Grady Booch et al., [Thinking Fast and Slow in AI](https://arxiv.org/abs/2010.06002) — AAAI, 2021.

---

## Research & Selected Projects

* **Neurosymbolic world models** (*RA-L 2024*): proposed the relational symbols formulation behind *Relational DeepSym*, which uses Gumbel-Sigmoid self-attention to extract sparse binary relational symbols for multi-object effect prediction.
* **LLM scaffolding for embodied agents** (*ICDL 2023*): first-authored a study of LLMs as automated scaffolding agents for robot exploration. GPT-3.5 guidance beats random exploration on cubes and fails on spheres, which it repeatedly treats as a stable base.
* **Intrinsic motivation for deep symbol learning** (*B.S. thesis*): an ensemble-disagreement active exploration framework. Matched-sample planning accuracy rises from 52% to 62%; the same policy reaches 58% on 23% fewer samples than the baseline needs for 52%.
* **Cross-embodiment skill transfer**: extended Blending-CNMPs to map vision-tracked human motion into Torobo joint-space trajectories.
* **FPGA design space exploration** (*course term project*): constraint-aware genetic algorithms in Python/Tcl for High-Level Synthesis parameter search.

*Full write-ups and code on the [Projects](/projects) page; dates and details on the [CV](/cv).*

---

## How I got here

My research direction came out of a specific afternoon at CoLoRs. A colleague was building a Lego tower out of hundreds of blocks while our symbol-discovery models were struggling with four objects. Alper Ahmetoğlu and I looked at that tower and decided a robot doing the same thing was the goal worth aiming at.

Eight months of failed iterations later, I traced the information flow through the network and found where it was losing the structure. The model computed its relations from symbols the encoder had already produced, so it could never represent a relation the encoder had missed — and two scenes built from the same blocks in different arrangements collapsed to one representation. That is a structural limit, not a tuning problem, which is why more data had not helped. The fix I specified, and named, became **Relational DeepSym**.

Solving the representation exposed the next wall, which was data. Effect prediction error kept climbing with the object count even as the datasets grew alongside it: 240,000 samples for four objects with the error still rising, and later a six-object environment that would not train on a million. A simple combinatorial argument explains why — the probability of randomly stumbling into a specific $n$-object interaction falls off roughly as $1/n!$ — so almost everything being collected was the same trivial event again.

My internship at SISReC was my way into the cognitive and developmental learning literature, and it gave me the response: stop sampling harder and start choosing. I pitched an intrinsic-curiosity approach to Assoc. Prof. Emre Uğur as my B.S. thesis. The resulting agent explores 5-to-10-object environments and finds interactions — including object rotations it was never given a primitive for — that random exploration essentially never reaches.

<!-- TODO (Batuhan): if you want the 12-object result here, add one precise sentence saying which
     configuration reached it and under what conditions (e.g. "the Gen 6 policy transferred to
     12-object scenes without retraining, evaluated on effect prediction only"). The homepage
     previously claimed 12 while the project page said 5–10 and listed more as future work;
     that contradiction is now removed, so only add the claim back in its exact form. -->

---

## Beyond the lab

* **Mathematical modeling:** building and picking apart models of things outside computer science — biological, physical, economic. It is where most of my reading time goes.
* **Japanese:** self-studied before taking formal coursework under Yuriko Öncü at Boğaziçi, which is part of how the Osaka internship came about.
* **Debate:** university debate discussions, for the structured-argument practice.

---

*Reach me at [batuhancelik.boun@gmail.com](mailto:batuhancelik.boun@gmail.com). References available on request from Dr. Alper Ahmetoğlu and Prof. Erhan Öztop.*
