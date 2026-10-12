---
permalink: /
title: "Batuhan Çelik"
author_profile: true
description: "Batuhan Çelik, applying for master's and PhD admission for Fall 2027. Research on extracting symbolic representations from raw sensory data, and on robots that actively seek out the physical interactions they cannot yet predict. RA-L 2024, ICDL 2023."
redirect_from: 
  - /about/
  - /about.html
---

Welcome! I am Batuhan, a computer engineering graduate of Boğaziçi University, applying for master's and PhD admission for **Fall 2027**. My work focuses on symbolic representations: how to **extract them from raw sensory data in a self-supervised manner**, and which inductive biases let a model **learn disentangled symbols and compose them to support counterfactual reasoning**. I believe a curriculum of increasing complexity is an essential part of this process, and I want robots to build it themselves by actively seeking out physical interactions they cannot yet predict and learning from them. Ultimately, such robots could uncover the physical mechanisms of the real world one interaction at a time.

---

## Research & Selected Projects

* [Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers](/publication/2023-relational) (*RA-L 2024*, second author). Relational DeepSym learns symbolic representations of objects and their relations from a robot's self-supervised interaction with a varying number of objects, and uses them to predict the effects of the robot's actions. I proposed using discrete attention weights between objects as relational symbols, and coined the term. The working implementation is my co-author Alper Ahmetoğlu's.
* [Developmental Scaffolding with Large Language Models](/publication/2023-icdl-scaffolding) (*ICDL 2023*, first author). GPT-3.5 chooses the next pick-and-place action of a robot that learns to predict the effects of its actions, in the role a caregiver plays in parental scaffolding. With cubes, the robot reached tall towers much earlier than it did under random exploration. Once a sphere was added, GPT-3.5 kept trying to stack cubes on it, calling the sphere a stable base.
* [Intrinsic Motivation for Deep Symbol Learning](/projects/intrinsic_curiosity) (*graduation project*). This follow-up to the RA-L paper replaces random exploration with active exploration. The robot seeks out the interactions it cannot yet predict, as measured by the disagreement of an ensemble of forward models. At equal sample counts, planning accuracy rises from 52% to 62%, and the active policy reaches 58% with 23% fewer samples than random exploration needs for 52%.
* [Human-to-Robot Skill Transfer through Correspondence Learning](/projects/correspondence_learning) (*independent project at SISReC, Osaka University, under Prof. Erhan Öztop*). Aktaş et al. learn correspondences between robots with different bodies through a common latent representation. I extended their framework to a human demonstrator tracked by a camera, whose reaching movements are decoded into joint trajectories for a simulated Torobo humanoid.
* [FPGA Design Optimization using Genetic Algorithms](/projects/evolutionary) (*course term project, with Ilgaz Er*). A genetic algorithm searches the pragma settings of a High-Level Synthesis design for the lowest latency that fits on the device. I proposed its selection rule, which keeps the population close to the resource constraint, where the fastest designs are likely to lie.

*Dates and further details are on the [CV](/cv).*

---

## How I got here

My research direction came out of a specific afternoon at CoLoRs, the Cognitive Learning and Robotics Lab at Boğaziçi University. A colleague was building a Lego tower out of hundreds of blocks while our symbol-discovery models were struggling with four objects. Alper Ahmetoğlu and I looked at that tower and decided a robot doing the same thing was the goal worth aiming at.

Eight months of failed iterations later, I traced the information flow through the network and found where it was losing the structure. The model computed its relations from symbols the encoder had already produced, so it could never represent a relation the encoder had missed, and two scenes built from the same blocks in different arrangements collapsed to one representation. That is a limit of the architecture's inductive bias, which is why more data had not helped. The fix I specified, and named, became Relational DeepSym.

Solving the representation exposed the next wall, which was data. Effect prediction error kept climbing with the object count even as the datasets grew alongside it: 240,000 samples for four objects with the error still rising. Later, in experiments I ran after the paper was published, the random exploration policy failed to discover enough samples to learn eight-object structures even with one million samples. My explanation is that the probability of randomly reaching a specific $$n$$-object interaction falls off exponentially in $$n$$, so almost everything being collected was the same trivial event again.

My internship at SISReC was my way into the cognitive and developmental robotics literature, and it gave me the response: let the robot choose which interactions to collect. I pitched active exploration driven by intrinsic motivation to Assoc. Prof. Emre Uğur as my graduation project. The resulting agent explores 5-to-10-object environments and reaches configurations absent from the randomly collected datasets, including a rotation of a wide block, which it was never given a primitive for.

---

## Beyond the lab

Outside research, I like to teach myself new things. Nowadays my focus is on psychology and communication.

* **Mathematical modeling and statistics:** building and picking apart models outside of computer science, such as models of biological, physical, and socioeconomic phenomena.
* **Music and guitar:** self-taught electric guitar player for 10 years, currently enjoying Irish revolutionary folk songs.
* **Debate:** university debate discussions, for the structured-argument practice.

---

*Reach me at [batuhancelik.boun@gmail.com](mailto:batuhancelik.boun@gmail.com). References available on request from Dr. Alper Ahmetoğlu and Prof. Erhan Öztop.*
