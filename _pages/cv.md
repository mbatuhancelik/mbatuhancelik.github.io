---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
description: "Curriculum vitae of Batuhan Çelik: B.S. Computer Engineering, Boğaziçi University; research at CoLoRs Lab and Osaka University SISReC; publications in RA-L 2024 and ICDL 2023."
redirect_from:
  - /resume
---
{% include base_path %}

**Email:** batuhancelik.boun@gmail.com

**Links:** [Google Scholar](https://scholar.google.com/citations?user=ALv_oq0AAAAJ&hl=en) · [GitHub](https://github.com/mbatuhancelik) · [LinkedIn](https://www.linkedin.com/in/mehmet-batuhan-%C3%A7elik-9a8795172) · [ORCID](https://orcid.org/0009-0005-7085-986X)

<!-- TODO (Batuhan): the file assets/files/Batuhan_Celik_CV.pdf does not exist in this repo, so the
     button below was a 404. Drop the PDF at that path and delete these comment markers to restore it.
     Check that every date in the PDF matches this page before you do.
[Download Full CV (PDF)]({{ base_path }}/assets/files/Batuhan_Celik_CV.pdf){: .btn .btn--info}
-->

---

## Research Interests

I work on neurosymbolic approaches to robot learning: extracting discrete, compositional representations from raw sensorimotor data, and using them for sample-efficient skill acquisition and planning. Within that, my focus is curiosity-driven and developmental exploration — how an agent should choose its own experience — and, increasingly, what it would take for the symbols such an agent learns to be causal rather than merely predictive.

---

## Education

### **Boğaziçi University** | *Istanbul, Turkey*
**B.S. in Computer Engineering** | **GPA:** 3.68 / 4.00
*Sept 2018 – Jan 2025*
* **Relevant Coursework:** Deep Learning in Robotics, Machine Learning, Parallel Algorithms, Advanced Theoretical Computer Science, Reconfigurable Computing, Quantum Algorithms.
* **University entrance:** Ranked 517th nationally in the science/quantitative (MF) track out of approximately 2.3 million candidates, Turkish university entrance examination (YKS), 2018.
* I extended my undergraduate studies beyond the standard four years by choice, on the advice of Prof. Suzan Üsküdarlı, in order to keep working in the CoLoRs and SISReC labs rather than finish sooner.

---

## Publications

### Journal Articles
* **Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers**\
   Alper Ahmetoğlu, **Batuhan Çelik**, Erhan Öztop, Emre Uğur\
  *IEEE Robotics and Automation Letters (RA-L)*, Feb 2024. \
  [DOI: 10.1109/LRA.2024.3350994](https://doi.org/10.1109/LRA.2024.3350994)

### Conference Proceedings
* **Developmental Scaffolding with Large Language Models**\
  **Batuhan Çelik**, Alper Ahmetoğlu, Emre Uğur, Erhan Öztop\
  *IEEE International Conference on Development and Learning (ICDL)*, Nov 2023.\
  [DOI: 10.1109/ICDL55364.2023.10364374](https://doi.org/10.1109/ICDL55364.2023.10364374)

*Published as **Batuhan Celik**; full legal name **Mehmet Batuhan Çelik**.*

---

## Research Experience

### **Undergraduate Researcher** | *Cognitive Learning and Robotics Lab (CoLoRs), Boğaziçi University*, Turkey
*Sep 2023 – Feb 2024* · Funded researcher on **TÜBİTAK ARDEB 1001 project 120E274** · Day-to-day supervision from Alper Ahmetoğlu; thesis requirements set and assessed by Assoc. Prof. Emre Uğur

* **Intrinsic Motivation for Deep Symbol Learning (B.S. Thesis):**
  * Began as an attempt to grow the symbol set itself, searching for novelty in symbolic rather than effect space — the lifelong-learning objective the project grant had not yet addressed. Gains over random exploration were indistinguishable from noise: the encoder producing the symbols is trained on the data collected so far, so genuinely novel states map onto familiar symbols rather than extrapolating to new ones. Reformulating the objective from *which states are novel* to *which states are predicted poorly* removed that dependence and motivated the disagreement signal below.
  * Replaced uniform random exploration in the [Relational DeepSym](/publication/2023-relational) framework with an epistemic uncertainty reward, computed from the covariance across a five-member forward-model council, addressing the exploration bottleneck in the original paper: effect-prediction error grew with object count even as the datasets scaled to 240K samples.
  * Under a restricted data budget, improved planning accuracy from **52% to 62%** over the random-exploration baseline at matched sample size (51k). At 23% fewer samples (39k vs. 51k) the curiosity-driven policy still reached 58%, exceeding what the baseline achieved with the larger budget.
  * Qualitative inspection found emergent behaviours the action repertoire did not contain, including object rotation via controlled collapses.

  [Project Page](/projects/intrinsic_curiosity) with qualitative inspection.

### **Research Intern** | *Symbiotic Intelligent Systems Research Center (SISReC), Osaka University*, Japan
*June 2023 – Sept 2023* · Position funded by **Osaka University's International Joint Research Promotion Program** · Supervised by Prof. Erhan Öztop.

* **Developmental Scaffolding with Large Language Models (ICDL 2023):**

  * Conceived and led the study as **first author**, designing a zero-shot, token-efficient state serialization layer that converts physical scene configurations into LLM-consumable inputs.
  * Co-developed the PyBullet-based UR10 simulation and designed the experiments comparing language-guided exploration against a random baseline, which surfaced systematic hallucinations in GPT-3.5's physical-world planning.
  * Drafted the manuscript and figures, incorporated co-author and faculty feedback, and served as **corresponding author** through the ICDL revision process.

  [Publication Page](/publication/2023-icdl-scaffolding).

* **Human-to-Robot Motion Transfer (Blending-CNMPs):**
  * Extended the Blending-CNMP architecture — originally for robot-to-robot skill transfer — to a human-in-the-loop setup, capturing demonstrations with an Intel RealSense camera and MediaPipe 3D tracking.
  * Diagnosed the CNMP encoder's sensitivity to the low-frequency drift that vision tracking introduces, which is distinct from the high-frequency jitter the architecture was designed to tolerate, and corrected it with a filtering and normalization pipeline.
  * Achieved cross-embodiment Cartesian-to-joint-space motion transfer to the Torobo manipulator, with ~3 cm error on held-out interpolated targets.

  [Project Page](/projects/correspondence_learning) with demonstrations.

### **Undergraduate Research Intern** | *Cognitive Learning and Robotics Lab (CoLoRs), Boğaziçi University*, Turkey
*Aug 2022 – May 2023* · Supported by a six-month **TÜBİTAK STAR** scholarship · Faculty supervision from Assoc. Prof. Emre Uğur; day-to-day mentorship from Alper Ahmetoğlu, then a PhD candidate in the lab

* **Discovering Predictive Relational Object Symbols (RA-L 2024):**
  * Designed and implemented the PyBullet simulation experiments for *Relational DeepSym*.
  * Tested the preceding attentive DeepSym architecture systematically and identified the failure that motivated the work: it cannot distinguish scenes containing two identical structures. Proposed the relational symbols formulation that addresses it — discretizing self-attention weights with Gumbel-Sigmoid to yield one sparse relational adjacency matrix per attention head ($$A \in \{0, 1\}^{k \times n \times n}$$ for $$k$$ heads and $$n$$ objects) alongside object properties. The working implementation is my co-author Alper Ahmetoğlu's.
  * Built an automated experimentation pipeline with WandB integration, managing concurrent VRAM scheduling (80–95% utilization across 10–50 runs) to make hyperparameter sweeps and multi-seed evaluation practical.

  [Publication Page](/publication/2023-relational).

* **Lab Service:** Specified and administered the lab's GPU server, organized the weekly seminar, and mentored incoming students. Detailed under [Service](#service).

---

## Course Projects

*Both projects below were advised by Prof. Arda Yurdakul, Boğaziçi University.*

### **FPGA Design Space Exploration via Constraint-Aware Genetic Algorithms** *(CMPE583 Reconfigurable Computing Term Project)*
* **Methodology:** Modeled non-convex High-Level Synthesis (HLS) design parameter search in Vitis HLS as an integer-boolean optimization problem, and argued for evolutionary algorithms as the appropriate method for this problem class. Mapped synthesis pragmas (array partitioning, loop unrolling, pipelining) directly into chromosome representations.
* **System Design:** Implemented a selection rule that makes candidates oscillate along a strict resource constraint (8,000 LUTs), and built a Python-Tcl controller managing parallel HLS compilation instances. Mapped the Pareto frontier between latency and LUT utilization.

  [Project Page](/projects/evolutionary) with full problem definition and methodology.

### **Autonomous RC Vehicle Architecture** *(1st Place – CMPE443 Competition)*
* Wrote bare-metal C firmware for STM32 Nucleo-144 boards using direct register manipulation, without HAL dependencies.
* Tuned hardware execution profiles for real-time sensor processing, trading energy consumption against motor speed.

---

## Talks & Presentations

* **Developmental Scaffolding with Large Language Models**
  * Lab-exchange presentation, NAIST Robot Learning Lab, Aug 2023.
  * Poster presentation, ROYAL Group, Boğaziçi University, 2023.
* Paper presentations on NS-CL and PaLM-E, CoLoRs Lab reading group, 2023.

[See more at Presentations](/presentations)

---

## Industry & Engineering Experience

### **Freelance AI / Software Engineer** | *Remote*
*Jul 2024 – Present*
Client work on LLM-backed conversational agents, a real-time interactive video agent pairing a language model with speech synthesis and viseme-driven lip-sync, and a grounded customer-support agent that answers only from retrieved policy and the caller's own account records, hands off to human staff when a request is outside its scope or it cannot ground an answer, and runs at a fraction of a cent per question to support high request volume.

* **Tech Stack:** Python, Anthropic and OpenAI APIs, AWS Polly, OpenCV, ffmpeg.

### **AI / Software Engineer Contractor** | *Upstash* (Remote / San Jose, USA)
*Feb 2024 – May 2024*
* Built **GitFix**, an LLM-based automated grammar correction tool for GitHub repositories.
* Used GitFix and smaller projects to demonstrate Upstash products for AI applications.
* Evaluated and proposed indexing strategies for Upstash Vector as a closed-beta tester, targeting computer vision use cases.
* **Tech Stack:** Python, TypeScript, FastAPI, Next.js, Redis, Fly.io, Vercel.

### **Software Engineering Intern** | *Atlassian* | *Ankara, Turkey*
*June 2022 – Aug 2022*
* Contributed to OpsGenie's core distributed infrastructure using **AWS primitives (S3, DynamoDB, SNS, SQS)**.
* Worked in international teams to integrate the OpsGenie API with other Atlassian products and their microservices.
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
*Feb 2022 – Jan 2025*
* **CMPE443: Principles of Embedded Systems Design** (*Fall 2024*) — Co-instructed lab sessions and graded embedded hardware assignments, for Prof. Arda Yurdakul.
* **CMPE160: Introduction to Object-Oriented Programming** (*Fall 2023*) — Delivered problem sessions and wrote question sets.
* **CMPE250: Data Structures & Algorithms** (*Spring 2023*) — Ran one course project end-to-end, from problem formulation to grading.
* **CMPE150: Introduction to Computing** (*Spring 2022*) — Wrote problem-session question sets.

[See more at Teaching](/teaching)

---

## Technical Skills

* **Research Skills:** Experimental design, symbolic representation learning, structured world models, ensemble-based uncertainty estimation, sensorimotor data analysis, statistical evaluation of model performance.
* **Languages:** **Python**, **C++**, C, Embedded C, Java, TypeScript, JavaScript, SQL, Bash.
* **AI & High-Performance Computing:** PyTorch, TensorFlow, CUDA, OpenMP, MPI, WandB, NumPy.
* **Data Analysis & Visualization:** Matplotlib, Plotly, Pandas.
* **Robotics:** PyBullet.
* **Cloud & DevOps:** Docker, AWS (EC2, Lambda, SQS, S3, DynamoDB), Redis, FastAPI, Spring, Node.js, Next.js, Git, Linux.
* **Hardware & Tooling:** FPGA (Xilinx), STM32 Microcontrollers, MATLAB/Simulink, LaTeX.
* **Familiar with:** ROS.

---

## Honors & Awards

* **STAR Undergraduate Research Scholarship** — TÜBİTAK (Scientific and Technological Research Council of Turkey). Six-month scholarship supporting my work on the "Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers" study (RA-L 2024).
* **Ethics in Academia Delegate** — Bilkent University, 2016. One of 150 students selected nationally, on assessed likelihood of pursuing a scientific career, to attend a academic-ethics lecture by Nobel laureate Aziz Sancar.


---

## Service

* **Departmental ABET Accreditation Representative** — Computer Engineering department, Boğaziçi University. Selected by two faculty, who knew me through lectures and teaching assistant positions, to join the accreditation review interviews and coordinate senior-class participation.
* **Research computing procurement and administration** — CoLoRs Lab, Spring 2023. Co-specified and deployed the lab's local GPU server on a roughly $12,000 budget.
  * Presented a report comparing NVIDIA against AMD GPUs on the lab's workloads, and the configurations the budget allowed.
  * Brought the machine up on Linux, resolving GPU, motherboard and Ethernet driver problems, and served it to the lab over SSH.
  * Specified the lab's laptop purchase from members' requirements, weighing local training throughput and Linux support.
* **Weekly research seminar organizer** — CoLoRs Lab, Spring 2023. Ran the lab's internal seminars for the semester: work updates and literature reviews.
* **Mentoring** — CoLoRs Lab. Mentored incoming students in deep learning and experimental design.

---

## References

Contact details available on request.

* **Dr. Alper Ahmetoğlu** — day-to-day research mentorship at CoLoRs Lab, 2022–2024; co-author on both publications.
* **Prof. Erhan Öztop** (Özyeğin University / Osaka University) — supervised my SISReC internship; co-author on both publications.
* **Prof. Suzan Üsküdarlı** (Boğaziçi University) — informal academic mentor across four years of my degree, in coursework and on research direction; advised the decision to extend my studies for lab work.
* **Prof. Arda Yurdakul** (Boğaziçi University) — advised both course projects above, and was the instructor for CMPE443 during my teaching assistantship.


---

## Languages

* **Turkish:** Native
* **English:** Full professional proficiency. TOEFL iBT 106 (2023); retaking in **Dec 2026** ahead of the Fall 2027 application cycle.
* **Japanese:** Conversational proficiency, classroom study at roughly N2 level.
