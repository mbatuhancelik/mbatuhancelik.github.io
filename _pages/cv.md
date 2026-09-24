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

[Download CV (PDF)]({{ base_path }}/assets/files/Batuhan_Celik_CV.pdf){: .btn .btn--info}

## Research Interests

Neurosymbolic robot learning: how an agent discovers discrete, compositional symbols from its own sensorimotor experience, and how it should choose which experience to collect. My current interest is what it would take for those symbols to be causal rather than merely predictive.

## Education

### **Boğaziçi University** | *Istanbul, Turkey*
**B.S. in Computer Engineering** | *Sept 2018 – Jan 2025*

Five-year programme: a one-year English preparatory year (2018–19), then the four-year B.S. · GPA 3.68 / 4.00
{: .cv-meta}

* **Coursework:** Deep Learning in Robotics, Machine Learning, Parallel Algorithms, Advanced Theoretical Computer Science, Reconfigurable Computing, Quantum Algorithms.
* **University entrance:** ranked 517th nationally out of approximately 2.3 million candidates in the science and quantitative (MF) track of the Turkish university entrance examination (YKS), 2018.
* Stayed past the standard five-year completion by choice, on the advice of Prof. Suzan Üsküdarlı, in order to keep working in the CoLoRs and SISReC labs rather than finish sooner.

## Publications

### Journal Articles
* **Discovering Predictive Relational Object Symbols with Symbolic Attentive Layers**\
  Alper Ahmetoğlu, **Batuhan Çelik**, Erhan Öztop, Emre Uğur\
  *IEEE Robotics and Automation Letters (RA-L)*, 9(2):1977–1984, Feb 2024.\
  [DOI: 10.1109/LRA.2024.3350994](https://doi.org/10.1109/LRA.2024.3350994) · [Publication page](/publication/2023-relational)

### Conference Proceedings
* **Developmental Scaffolding with Large Language Models**\
  **Batuhan Çelik**, Alper Ahmetoğlu, Emre Uğur, Erhan Öztop\
  *IEEE International Conference on Development and Learning (ICDL)*, Nov 2023, pp. 396–402. First and corresponding author.\
  [DOI: 10.1109/ICDL55364.2023.10364374](https://doi.org/10.1109/ICDL55364.2023.10364374) · [Publication page](/publication/2023-icdl-scaffolding)

*Published as **Batuhan Celik**; full legal name **Mehmet Batuhan Çelik**.*

## Research Experience

### **Undergraduate Researcher** | *Cognitive Learning and Robotics Lab (CoLoRs), Boğaziçi University*, Turkey
*Sept 2023 – Feb 2024*

Funded on **TÜBİTAK ARDEB 1001 project 120E274** · Day-to-day supervision from Alper Ahmetoğlu; thesis requirements set and assessed by Assoc. Prof. Emre Uğur
{: .cv-meta}

**Intrinsic Motivation for Deep Symbol Learning (B.S. thesis)** — [project page](/projects/intrinsic_curiosity)

* Replaced uniform random exploration in the [Relational DeepSym](/publication/2023-relational) framework with an epistemic uncertainty reward computed from the covariance across a five-member forward-model council, addressing the bottleneck in the original paper: effect-prediction error grew with object count even as the datasets scaled to 240K samples.
* Raised planning accuracy from **52% to 62%** over the random-exploration baseline at a matched budget of 51k samples, and reached 58% on 39k — 23% fewer than the baseline needed for 52%. The policy also reached interactions absent from the action repertoire, including rotation of a block through a controlled collapse.
* An earlier formulation searching for novelty in symbolic rather than effect space gained nothing measurable over random exploration, because the encoder producing the symbols maps genuinely novel states onto familiar ones. Reformulating the objective from *which states are novel* to *which are predicted poorly* removed that dependence and motivated the disagreement signal above.

### **Research Intern** | *Symbiotic Intelligent Systems Research Center (SISReC), Osaka University*, Japan
*June – Sept 2023*

Position funded by **Osaka University's International Joint Research Promotion Program** · Supervised by Prof. Erhan Öztop
{: .cv-meta}

**Developmental Scaffolding with Large Language Models (ICDL 2023)** — [publication page](/publication/2023-icdl-scaffolding)

* Realized a study proposed by Prof. Erhan Öztop and carried it to publication as first and corresponding author. Designed a zero-shot, token-efficient state serialization converting physical scene configurations into LLM-consumable prompts, co-developed the PyBullet UR10 simulation, and ran the experiments against a random-exploration baseline, which surfaced systematic failures in GPT-3.5's affordance reasoning. Drafted the manuscript and figures and handled the ICDL review response.

**Human-to-Robot Skill Transfer through Correspondence Learning** — [project page](/projects/correspondence_learning)

* On a suggestion from Prof. Minoru Asada, extended the CNMP-based correspondence-learning framework of Aktaş et al. (RA-L 2024, then in progress) from robot-to-robot transfer to a camera-tracked human demonstrator, capturing demonstrations with an Intel RealSense camera and two image-plane coordinates from MediaPipe's pose landmarks.
* Diagnosed the encoder's sensitivity to the low-frequency drift that vision tracking introduces, which is distinct from the high-frequency jitter the architecture was designed to tolerate, and corrected it with a filtering and normalization pipeline. Achieved cross-embodiment Cartesian-to-joint-space transfer to a simulated Torobo manipulator, reaching targets between the trained ones with a largest observed end-effector error of 2.98 cm, measured interactively rather than over a held-out set.

### **Undergraduate Research Intern** | *Cognitive Learning and Robotics Lab (CoLoRs), Boğaziçi University*, Turkey
*Aug 2022 – May 2023*

Six-month **TÜBİTAK STAR** scholarship · Faculty supervision from Assoc. Prof. Emre Uğur; day-to-day mentorship from Alper Ahmetoğlu, then a PhD candidate in the lab
{: .cv-meta}

**Discovering Predictive Relational Object Symbols (RA-L 2024)** — [publication page](/publication/2023-relational)

* Designed and implemented the PyBullet simulation experiments, and showed that the preceding attentive DeepSym architecture's failure to distinguish scenes containing two identical structures was structural rather than a matter of tuning. Built an automated experimentation pipeline with WandB integration and VRAM-aware scheduling, 10–50 concurrent runs at 80–95% utilization, to make hyperparameter sweeps and multi-seed evaluation practical.
* Proposed and named the relational symbols formulation that addresses it, discretizing self-attention weights with Gumbel-Sigmoid into one sparse relational adjacency matrix per attention head alongside object properties. *The working implementation is my co-author Alper Ahmetoğlu's.*

## Teaching

### **Student Teaching Assistant** | *Boğaziçi University, Computer Engineering*
*Feb 2022 – Jan 2025*

* **CMPE443: Principles of Embedded Systems Design** (*Fall 2024*) — co-instructed the STM32 lab sessions and handled grading, for Prof. Arda Yurdakul.
* **CMPE250: Data Structures & Algorithms** (*Spring 2023*) — ran one term project end to end, from problem formulation through grading.
* **CMPE160: Introduction to Object-Oriented Programming** (*Fall 2023*) and **CMPE150: Introduction to Computing** (*Spring 2022*) — problem sessions, question sets and exam problems.

[See more at Teaching](/teaching)

## Course Projects

*Both projects are joint work with Ilgaz Er, advised by Prof. Arda Yurdakul, Boğaziçi University.*
{: .cv-meta}

### **FPGA Design Space Exploration via Constraint-Aware Genetic Algorithms** *(CMPE583 Reconfigurable Computing Term Project)*

* Framed non-convex High-Level Synthesis parameter search in Vitis HLS as an integer-boolean optimization problem, and argued for evolutionary algorithms as the appropriate method for this problem class. Mapped synthesis pragmas (array partitioning, loop unrolling, pipelining) into chromosome representations, with a selection rule that holds the population against a strict 8,000-LUT resource constraint.

  [Project Page](/projects/evolutionary) with full problem definition and methodology.

### **Autonomous RC Vehicle Architecture** *(CMPE443, 1st place in the course competition)*

* Bare-metal C firmware for STM32 Nucleo-144 boards using direct register manipulation, without HAL dependencies.

## Talks & Presentations

* **Developmental Scaffolding with Large Language Models** — lab-exchange presentation, NAIST Robot Learning Lab, Aug 2023; poster presentation, ROYAL Group, Boğaziçi University, Nov 2023.
* Reading-group presentations on NS-CL and PaLM-E, CoLoRs Lab, 2023.

[See more at Presentations](/presentations)

## Industry & Engineering Experience

* **Freelance AI / Software Engineer**, remote (*Jul 2024 – present*) — LLM-backed conversational agents, a real-time interactive video agent pairing a language model with speech synthesis and viseme-driven lip-sync, and a grounded customer-support agent that answers only from retrieved policy and the caller's own account records, hands off to human staff when it cannot ground an answer, and runs at a fraction of a cent per question to support high request volume.
* **AI / Software Engineer Contractor**, Upstash, remote / San Jose (*Feb – May 2024*) — developer advocacy for AI workloads: implemented [GitFix](https://github.com/upstash/gitfix) and other demonstrations positioning Upstash's products as convenient infrastructure for AI applications; closed-beta tester for Upstash Vector.
* **Software Engineering Intern**, Atlassian, Ankara (*June – Aug 2022*) — contributed to OpsGenie's core distributed infrastructure on AWS primitives (S3, DynamoDB, SNS, SQS), and worked with teams in Poland and India to integrate the OpsGenie API with other Atlassian products.
* **IP Network & Automation Intern**, Nokia, Istanbul (*Dec 2021 – Feb 2022*) — internal tooling for remote ISP router configuration and infrastructure management.

## Technical Skills

* **Research:** experimental design · symbolic representation learning · structured world models · ensemble-based uncertainty estimation · sensorimotor data analysis · statistical evaluation of model performance
* **Languages:** Python · C++ · C and Embedded C · Java · TypeScript · JavaScript · SQL · Bash
* **ML & HPC:** PyTorch · TensorFlow · CUDA · OpenMP · MPI · WandB · NumPy · Matplotlib · Pandas · PyBullet · ROS (familiar)
* **Systems & hardware:** Docker · AWS (EC2, Lambda, S3, SQS, DynamoDB) · Redis · FastAPI · Git · Linux · FPGA (Xilinx) · STM32 · MATLAB/Simulink · LaTeX

## Honors & Awards

* **TÜBİTAK STAR Undergraduate Research Scholarship** — six-month scholarship supporting the work that became the RA-L 2024 study.
* **Ethics in Academia Delegate** — Bilkent University, 2016. One of 150 students selected nationally, on assessed likelihood of pursuing a scientific career, to attend an academic-ethics lecture by Nobel laureate Aziz Sancar.

## Service

* **Departmental ABET accreditation representative** — Computer Engineering, Boğaziçi University. Selected by two faculty, who knew me through lectures and teaching assistant positions, to join the accreditation review interviews and coordinate senior-class participation.
* **Research computing** — CoLoRs Lab, Spring 2023. Ran the hardware evaluation for the lab's newly built GPU server on a roughly $12,000 budget, as the lab's parallel-computing and hardware hobbyist: compared candidate CPUs, GPUs and motherboards on architecture and fit to the lab's workloads. Presented the comparison to the lab, and helped bring the machine up on Linux, working mainly on the GPU and Ethernet drivers.
* **Weekly research seminar organizer** — CoLoRs Lab, Spring 2023. Ran the lab's internal seminars for the semester, and mentored incoming students in deep learning and experimental design.

## Languages

Turkish (native) · English (full professional proficiency; TOEFL iBT 106 in 2023, retaking **Dec 2026** ahead of the Fall 2027 application cycle) · Japanese (conversational; classroom study at roughly N3 level)

## References

Contact details available on request.

* **Dr. Alper Ahmetoğlu** — day-to-day research mentorship at CoLoRs Lab, 2022–2024; co-author on both publications.
* **Prof. Erhan Öztop** (Özyeğin University / Osaka University) — supervised my SISReC internship; co-author on both publications.
* **Prof. Suzan Üsküdarlı** (Boğaziçi University) — academic mentor across the degree, in coursework and on research direction; advised the decision to extend my studies for lab work.
* **Prof. Arda Yurdakul** (Boğaziçi University) — advised both course projects above, and was the instructor for CMPE443 during my teaching assistantship.

<style>
/* CV page only. Two jobs: mute the meta lines under each entry heading so the eye
   goes to the entry itself, and give sections the same rule the PDF uses, which
   replaces the <hr> separators this page used to carry between sections.
   To revert: delete this block and put the "---" separators back. */
.page__content .cv-meta {
  font-size: 0.85em;
  color: #6b6b6b;
  margin: 0.1em 0 0.7em 0;
  line-height: 1.45;
}
.page__content h2 {
  margin-top: 1.7em;
  padding-bottom: 0.2em;
  border-bottom: 1px solid #e2e2e2;
}
.page__content h3 {
  margin-top: 1.1em;
  margin-bottom: 0.1em;
}
.page__content h3 + p { margin-top: 0.1em; }
.page__content ul { margin-top: 0.35em; }
.page__content li { margin-bottom: 0.4em; }
</style>