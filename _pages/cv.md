---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---
{% include base_path %}

**Email:** batuhancelik.boun@gmail.com · **Phone:** +90 551 446 95 70

**Links:** [Google Scholar](#) · [GitHub](#) · [LinkedIn](#)

[Download Full CV (PDF)]({{ base_path }}/assets/files/Batuhan_Celik_CV.pdf){: .btn .btn--info}

---

## Research Interests

I work on neurosymbolic approaches to robot learning — extracting symbolic, compositional representations from raw sensorimotor data, and using them to support sample-efficient skill acquisition. My current interests span developmental and curiosity-driven learning, parallel and hardware-aware algorithm design, and the role of large language models as scaffolds for embodied agents.

---

## Education

### **Boğaziçi University** | *Istanbul, Turkey*
**B.S. in Computer Engineering** | **GPA:** 3.68 / 4.00
*Sept 2018 – Dec 2024*
* **Relevant Coursework:** Deep Learning in Robotics, Machine Learning, Parallel Algorithms, Advanced Theoretical Computer Science, Reconfigurable Computing, Quantum Algorithms.
* **Honors:** Ranked **517th** among 2.5 million students nationwide in the Turkish Higher Education Foundations Examination.

---

## Publications

### Journal Articles
* **Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers**
  Alper Ahmetoglu, **Batuhan Celik**, Erhan Oztop, Emre Ugur
  *IEEE Robotics and Automation Letters (RA-L)*, Feb 2024. [DOI: 10.1109/LRA.2024.3350994](https://doi.org/10.1109/LRA.2024.3350994)

### Conference Proceedings
* **Developmental Scaffolding with Large Language Models**
  **Batuhan Celik**, Alper Ahmetoglu, Emre Ugur, Erhan Oztop
  *IEEE International Conference on Development and Learning (ICDL)*, Aug 2023. [DOI: 10.1109/ICDL55364.2023.10364374](https://doi.org/10.1109/ICDL55364.2023.10364374)

---

## Research Experience

### **Research Intern** | *Symbiotic Intelligent Systems Research Center (SISREC), Osaka University*, Japan[cite: 1, 4, 5]
*June 2023 – Sept 2023*[cite: 1]

* **Developmental Scaffolding with Large Language Models(ICDL 2023):** 

  * Conceived and led the study as first author, designing a zero-shot, token-efficient state serialization layer converting physical scene configurations into LLM-consumable inputs.
  * Co-developed the PyBullet-based UR10 simulation and designed experiments comparing language-guided high-information-gain exploration against standard stochastic exploration, uncovering systematic hallucinations in GPT-3.5's physical-world planning.
  * Drafted the manuscript and figures, incorporated co-author and faculty feedback, and served as corresponding author through the ICDL revision process.

  [Publication Page](/publication/2023-icdl-scaffolding)

* **Human-to-Robot Motion Transfer(Blending-CNMPs):** 

  * Extended the Blending-CNMP architecture to a human-in-the-loop setup using an Intel RealSense camera and MediaPipe 3D tracking[cite: 4]. 
  * Designed a trajectory filtering and normalization pipeline to suppress low-frequency tracking drift, achieving cross-embodiment Cartesian-to-joint-space motion transfer to the Torobo manipulator with a **~3 cm** end-effector accuracy[cite: 4].

  [Project Page](/projects/correspondence_learning)

### **Research Intern** | *Cognitive Learning and Robotics Lab (CoLoRs), Boğaziçi University*,  Turkey
*Aug 2022 – Jan 2024*[cite: 1]

* **Discovering Predictive Relational Object Symbols(RA-L 2024):** 
  * Designed and implemented the PyBullet simulation experiments for *Relational DeepSym*[cite: 3]. 
  * Co-developed a discrete self-attention block using Gumbel-Sigmoid activations to extract sparse relational adjacency matrices ($$A \in \{0, 1\}^{N \times N}$$) alongside object properties[cite: 3]. 
  * Built an automated experimentation pipeline with WandB cloud integration to manage concurrent VRAM scheduling (80–95% utilization across 10–50 runs)[cite: 3].

  [Publication Page](/projects/2023-relational)

* **Intrinsic Curiosity for Deep Symbolic Learning (B.S. Thesis):** 
  * Conceived and developed an active exploration framework to solve Relational DeepSym's 1M-sample data bottleneck[cite: 6]. 
  * Utilized a 5-member ensemble disagreement council over 5-step lookahead horizons to measure epistemic uncertainty.
  * Outperformed random exploration baselines by up to **10% in planning accuracy** and matched its performance while using **23% fewer** training samples[cite: 6].
* **Lab Leadership:** Organized weekly research seminars, managed local GPU server infrastructure, and mentored incoming students in deep learning and experimental design.

[Project Page](/projects/intrinsic_curiosity)

---

## Selected Projects

### **Intrinsic Curiosity for Deep Symbolic Robot Learning** *(B.S. Senior Thesis)*[cite: 6]
* **Motivation & Method:** Replaced uniform random sampling in [Relational DeepSym](/projects/2023-relational) with an epistemic uncertainty reward computed via covariance matrices across a forward-dynamics prediction ensemble[cite: 6].
* **Key Results:** Achieved higher planning accuracy ($0.58$ vs. $0.52$) with $39\text{k}$ samples compared to a $51\text{k}$-sample random baseline[cite: 6]. Uncovered complex emergent behaviors—including convoluted symbol manipulation and unprogrammed rotation primitives via controlled collapses[cite: 6].

### **FPGA Design Space Exploration via Constraint-Aware Genetic Algorithms** *(CMPE583 Project)*[cite: 5]
* **Methodology:** Modeled non-convex High-Level Synthesis (HLS) design parameter search in Vitis HLS as an integer-boolean evolutionary optimization problem[cite: 5]. Direct-mapped synthesis pragmas (array partitioning, loop unrolling, pipelining) into chromosome representations[cite: 5].
* **System Design & Optimization:** Implemented a selection rule enforcing candidate boundary oscillation along strict resource constraints ($8,000$ LUTs) and engineered a Python-Tcl controller managing parallel HLS compilation instances[cite: 5]. Successfully mapped the Pareto frontier between latency and LUT utilization[cite: 1, 5].

### **Autonomous RC Vehicle Architecture** *(1st Place – CMPE443 Competition)*[cite: 1]
* Programmed bare-metal C firmware on STM32 Nucleo-144 boards via direct register manipulation without HAL dependencies[cite: 1].
* Optimized hardware execution profiles for real-time sensor processing while balancing energy consumption against motor speeds[cite: 1].

---

## Talks & Presentations

* **Developmental Scaffolding with Large language models**  
  * Invited talk, NAIST Robot Learning Lab, 2023.
  * Invited talk, ROYAL Group, Boğaziçi University, 2023.
* Weekly paper presentations on NSCL and PaLM-E, CoLoRs Lab reading group, 2022–2024.

---

## Industry & Engineering Experience

### **AI / Software Engineer Contractor** | *Upstash* (Remote / San Jose, USA)
*Feb 2024 – May 2024*
* Engineered **GitFix**, an automated grammar correction tool for GitHub repositories built on LLMs.
* Used GitFix and smaller projects to promote Upstash Products for AI applications.
* Evaluated and proposed indexing strategies for Upstash Vector as a closed-beta tester, targeting computer vision use cases.
* **Tech Stack:** Python, TypeScript, FastAPI, Next.js, Redis, Fly.io, Vercel.

### **Software Engineering Intern** | *Atlassian* | *Ankara, Turkey*
*June 2022 – Aug 2022*
* Contributed to OpsGenie's core distributed infrastructure using **AWS primitives (S3, DynamoDB, SNS, SQS)**.
* Working in **international teams**, Integrated Opsgenie API to other Atlassian products and their respective microservices.
* Automated API documentation pipelines across multiple microservices.
* **Tech Stack:** Java, Spring, AWS.

### **IP Network & Automation Intern** | *Nokia* | *Istanbul, Turkey*
*Dec 2021 – Feb 2022*
* Developed internal tools for ISPs to support remote router configuration and infrastructure management.
* Completed Nokia's internal training on network management across OSI Layers 2–5.
* **Tech Stack:** Python, JavaScript, FastAPI, React, MongoDB, Docker.

---

## Teaching Experience

### **Student Teaching Assistant** | *Boğaziçi University*
*Feb 2022 – Jan 2024*
* **CMPE443: Principles of Embedded Systems Design** (*Fall 2023*) — Supervised lab hours and graded embedded hardware assignments.
* **CMPE250: Data Structures & Algorithms** (*Spring 2023*) — Managed one course project end-to-end, from problem formulation to grading.
* **CMPE160: Introduction to OOP** (*Fall 2022*) — Delivered problem sessions and authored question sets.
* **CMPE150: Introduction to Computing** (*Spring 2022*) — Authored problem-session question sets.

[See more at Teaching](/teaching)

---

## Technical Skills

* **Research Skills:** Experimental design, symbolic representation learning, structured world models, ensemble-based uncertainty estimation, sensorimotor data analysis, statistical evaluation of model performance.
* **Languages:** **Python**, **C++**, C, Embedded C, Java, TypeScript, JavaScript, SQL, Bash.
* **AI & High-Performance Computing:** PyTorch, TensorFlow, CUDA, OpenMP, MPI, WandB, NumPy.
* **Robotics:** Pybullet, ROS(limited)
* **Data:** Matplotlib, Plotly, Pandas
* **Cloud & DevOps:** Docker, AWS (EC2, Lambda, SQS, S3, DynamoDB), Redis, FastAPI, Spring, Node.js, Next.js, Git, Linux.
* **Hardware & Tooling:** FPGA (Xilinx), STM32 Microcontrollers, MATLAB/Simulink, LaTeX.

---

## Honors & Scholastic Achievements

* **STAR Undergraduate Research Scholarship** — TÜBİTAK (Scientific and Technological Research Council of Turkey), awarded for the "Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers" study.
* **Ethics in Academia Delegate** — Selected participant, Bilkent University symposium on academic ethics with Nobel Laureate Aziz Sancar (2016).

## Service

* **Departmental ABET Accreditation Representative** — Selected by the Computer Engineering department to represent it while selecting my co-interviees during ABET accreditation review.

---

## Languages

* **Turkish:** Native
* **English:** Professional fluency (TOEFL iBT: 106, [2023, pending for renewal])
* **Japanese:** JLPT N3 (written), N2-equivalent (oral)