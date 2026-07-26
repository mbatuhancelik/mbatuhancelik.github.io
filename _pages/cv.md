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

**Links:** [Google Scholar](https://scholar.google.com/citations?user=ALv_oq0AAAAJ&hl=en) · [GitHub](https://github.com/mbatuhancelik) · [LinkedIn](https://www.linkedin.com/in/mehmet-batuhan-%C3%A7elik-9a8795172) · [ORCID](https://orcid.org/0009-0005-7085-986X)

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

### **Research Intern** | *Symbiotic Intelligent Systems Research Center (SISReC), Osaka University*, Japan
*June 2023 – Sept 2023*

* **Developmental Scaffolding with Large Language Models (ICDL 2023):**

  * Conceived and led the study as **first author**, designing a zero-shot, token-efficient state serialization layer converting physical scene configurations into LLM-consumable inputs.
  * Co-developed the PyBullet-based UR10 simulation and designed experiments comparing language-guided high-information-gain exploration against standard stochastic exploration, uncovering systematic hallucinations in GPT-3.5's physical-world planning.
  * Drafted the manuscript and figures, incorporated co-author and faculty feedback, and served as **corresponding author** through the ICDL revision process.

  [Publication Page](/publication/2023-icdl-scaffolding).

* **Human-to-Robot Motion Transfer (Blending-CNMPs):** Extended the Blending-CNMP architecture to a human-in-the-loop setup using an Intel RealSense camera and MediaPipe 3D tracking — full write-up under Selected Projects.

### **Research Intern** | *Cognitive Learning and Robotics Lab (CoLoRs), Boğaziçi University*, Turkey
*Aug 2022 – Jan 2024*

* **Discovering Predictive Relational Object Symbols (RA-L 2024):**
  * Designed and implemented the PyBullet simulation experiments for *Relational DeepSym*.
  * Co-developed a discrete self-attention block using Gumbel-Sigmoid activations to extract sparse relational adjacency matrices ($$A \in \{0, 1\}^{N \times N}$$) to serve as relational symbols alongside object properties.
  * Built an automated experimentation pipeline with WandB cloud integration to manage concurrent VRAM scheduling (80–95% utilization across 10–50 runs).

  [Publication Page](/projects/2023-relational).

* **Intrinsic Curiosity for Deep Symbolic Learning (B.S. Thesis):** Designed an active exploration framework using 5-member ensemble disagreement over 5-step lookahead horizons, improving planning accuracy by 10% at equal sample size — full write-up under Selected Projects.
* **Lab Leadership:** Organized weekly research seminars, managed local GPU server infrastructure, and mentored incoming students in deep learning and experimental design.

---

## Selected Projects

### **Intrinsic Curiosity for Deep Symbolic Robot Learning** *(B.S. Senior Thesis)*
* **Motivation & Method:** Replaced uniform random exploration in [Relational DeepSym](/projects/2023-relational) framework with an epistemic uncertainty reward computed via covariance matrices across a forward-dynamics prediction ensemble.
* **Key Results:** In a data-constrained regime, improved planning accuracy from **52% to 62%** over the random-exploration baseline at matched sample size (51k). Using 23% fewer samples (39k vs. 51k), the curiosity-driven policy still reached 58% — exceeding the baseline's 51k-sample accuracy despite using less data. Further inspection revealed complex emergent behaviors — including convoluted symbol manipulation and unprogrammed rotation primitives via controlled collapses.

  [Project Page](/projects/intrinsic_curiosity) with qualitative inspection.

### **Human-to-Robot Motion Transfer (Blending-CNMPs)**
* **Motivation & Method:** Extended the Blending-CNMP architecture — originally focused on robot-to-robot skill transfer — to a human-in-the-loop setup, capturing demonstrations via an Intel RealSense camera and MediaPipe 3D tracking, then diagnosing and correcting the CNMP encoder's sensitivity to the resulting low-frequency drift (distinct from the high-frequency jitter it was originally designed to tolerate) with a custom filtering and normalization pipeline.
* **Key Results:** Achieved cross-embodiment **Cartesian-to-joint-space motion transfer** to the Torobo manipulator with a **~3 cm** end-effector accuracy.

  [Project Page](/projects/correspondence_learning) with demonstrations.

### **FPGA Design Space Exploration via Constraint-Aware Genetic Algorithms** *(CMPE583 Reconfigurable Computing Term Project)*
* **Methodology:** Modeled non-convex High-Level Synthesis (HLS) design parameter search in Vitis HLS as an integer-boolean optimization problem, and argued for evolutionary algorithms as the most suitable approach for this problem class. Direct-mapped synthesis pragmas (array partitioning, loop unrolling, pipelining) into chromosome representations.
* **System Design & Optimization:** Implemented a selection rule enforcing candidate boundary oscillation along strict resource constraints (8,000 LUTs) and engineered a Python-Tcl controller managing parallel HLS compilation instances. Successfully mapped the Pareto frontier between latency and LUT utilization.

  [Project Page](/projects/evolutionary) with full problem definition and methodology.

### **Autonomous RC Vehicle Architecture** *(1st Place – CMPE443 Competition)*
* Programmed bare-metal C firmware on STM32 Nucleo-144 boards via direct register manipulation without HAL dependencies.
* Optimized hardware execution profiles for real-time sensor processing while balancing energy consumption against motor speeds.

---

## Talks & Presentations

* **Developmental Scaffolding with Large Language Models**
  * Invited talk, NAIST Robot Learning Lab, 2023.
  * Invited talk, ROYAL Group, Boğaziçi University, 2023.
* Weekly paper presentations on NSCL and PaLM-E, CoLoRs Lab reading group, 2022–2024.

---

## Industry & Engineering Experience

### **AI / Software Engineer Contractor** | *Upstash* (Remote / San Jose, USA)
*Feb 2024 – May 2024*
* Engineered **GitFix**, an automated grammar correction tool for GitHub repositories built on LLMs.
* Used GitFix and smaller projects to promote Upstash products for AI applications.
* Evaluated and proposed indexing strategies for Upstash Vector as a closed-beta tester, targeting computer vision use cases.
* **Tech Stack:** Python, TypeScript, FastAPI, Next.js, Redis, Fly.io, Vercel.

### **Software Engineering Intern** | *Atlassian* | *Ankara, Turkey*
*June 2022 – Aug 2022*
* Contributed to OpsGenie's core distributed infrastructure using **AWS primitives (S3, DynamoDB, SNS, SQS)**.
* Worked in international teams to integrate the OpsGenie API with other Atlassian products and their respective microservices.
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
* **Data Analysis & Visualization:** Matplotlib, Plotly, Pandas
* **Robotics:** PyBullet, ROS (limited)
* **Cloud & DevOps:** Docker, AWS (EC2, Lambda, SQS, S3, DynamoDB), Redis, FastAPI, Spring, Node.js, Next.js, Git, Linux.
* **Hardware & Tooling:** FPGA (Xilinx), STM32 Microcontrollers, MATLAB/Simulink, LaTeX.

---

## Honors & Scholastic Achievements

* **STAR Undergraduate Research Scholarship** — TÜBİTAK (Scientific and Technological Research Council of Turkey), awarded for the "Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers" study.
* **Ethics in Academia Delegate** — Selected participant, Bilkent University symposium on academic ethics with Nobel Laureate Aziz Sancar (2016).
---
## Service

* **Departmental ABET Accreditation Representative** — Selected by the Computer Engineering department to represent it, choosing the senior-class students who participated in interviews for the ABET accreditation review.

---

## Languages

* **Turkish:** Native
* **English:** Professional fluency (TOEFL iBT: 106, 2023 — pending renewal)
* **Japanese:** JLPT N3 (written), N2-equivalent (oral)