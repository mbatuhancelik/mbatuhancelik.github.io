---
title: "Human-to-Robot Skill Transfer with Blending CNMPs"
collection: portfolio
header:
    video_teaser: '/images/human_to_robot.mp4'
date: 28.08.2023
excerpt: 'Extending the Blending-CNMP framework to noisy, vision-based human demonstrations — bridging the embodiment and Cartesian-to-joint-space gap to transfer reaching skills between a human and the Torobo manipulator.'
---

> **Note:** This is an independent project extending Aktaş et al. (2023). I am **not an author** on that paper — see [Context](#context) below.


## Abstract

This project extends the Blending Conditional Neural Movement Primitives (Blending-CNMP) framework — originally validated only on clean, simulated robot-to-robot data — to a human-in-the-loop setting. Human reaching movements were captured with an Intel RealSense camera and MediaPipe, which introduces low-frequency drift that the blending-CNMP encoder proved highly sensitive to. A filtering and normalization pipeline conditions these trajectories before encoding, allowing the shared latent space to converge. The result is bidirectional skill transfer between a human demonstrator and the Torobo manipulator, mapping human Cartesian coordinates to Torobo joint-space trajectories on unseen, interpolated targets.

<div class="archive__item-teaser">
    <video autoplay loop muted playsinline width="100%" style="display:block; object-fit:cover;">
      <source src="/images/human_to_robot.mp4" type="video/mp4">Your browser does not support the video tag.
    </video>
</div>

*Demo: human → robot transfer on a validation target **between** two trained angles — a generalization test, not a replay of a trained motion. The robot → human direction was validated numerically only.*

---

## Motivation & Methodological Context

The core foundation of this project builds directly upon the Blending-CNMP framework introduced by Aktaş et al. (2023) for learning correspondences across morphologically different robots.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/blending_cnmp_arch.png" alt="Blending-CNMP Architecture Overview" style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Figure: Blending-CNMP architecture mapping conditional observations from diverse morphologies into a shared representation space.</p>
</div>

As illustrated above, sparse conditional observations from each agent's trajectory ($$S^A_t$$ and $$S^B_t$$) are passed through agent-specific encoders ($$E^A$$ and $$E^B$$) and aggregated to produce distinct latent vectors $$L^A$$ and $$L^B$$. These latents are subsequently combined into a single, unified shared representation space ($$L$$) via a randomly-weighted convex combination using a blending parameter $$p$$ sampled uniformly during training:

$$L = p \cdot L^A + (1-p) \cdot L^B \quad \text{where} \quad p \sim U(0,1)$$

*(Note: While the generalized framework supports $$n$$-way combinations for multiple morphologies, this two-agent derivation directly matches our experimental setup).*

Given a target query timestamp ($$t_{\text{target}}$$), the shared representation is processed by agent-specific decoders ($$Q^A$$ and $$Q^B$$) to predict the trajectory mean ($$\mu$$) and variance ($$\sigma$$). At inference time, task-level skill transfer is achieved symmetrically by forcing the blending weight of the source agent to 1 (and the target to 0). The shared representation is generated purely from the source's observations and decoded through the target agent's specific decoder.

While highly effective across simulated robot pairs, the baseline framework operates under a major limiting assumption: **all agent trajectories are assumed to be clean, high-frequency sensorimotor streams**. Extending this formulation to handle noisy, vision-tracked human demonstrations introduces severe data-distribution shifts that prevent latent convergence.

## 🛠️ Methodology & Core Contributions

### 1. Vision-Based Trajectory Capture
* **Hardware Setup:** Human arm-reaching movements were recorded in 3D Cartesian space using an Intel RealSense depth camera.
* **Keypoint Extraction:** Hand and wrist coordinates were tracked dynamically using MediaPipe, bypassing the need for intrusive motion-capture suits or manual kinesthetic teaching.

**Workspace & Task Layout:**
The experimental environment was mapped out systematically to test spatial interpolation and coordinate transfer:
* **The Trajectory Bounds:** The workspace consists of one shared **start position** (large green circle) and multiple **target positions** (small yellow circles) arranged in a **180° half-circle array**.
* **Training Data:** The network was trained on **7 distinct trajectories** spaced exactly **30° apart** across the full half-circle. 
* **Data Capture:** For human demonstrations, the tester moved their hand from the start position to a designated target while MediaPipe's real-time pose tracking extracted the Cartesian hand trajectory. For the robot side, matching Torobo trajectories were generated via inverse kinematics and logged directly in joint space.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/collection_data_collection_setup.png" alt="Data collection setup showing MediaPipe pose tracking with a start circle and target circles" style="width:85%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Figure: Human demonstration capture setup. The green circle marks the shared start position; yellow circles denote the 30°-spaced targets. Red dots and white skeleton lines represent the real-time MediaPipe keypoints used to extract Cartesian hand trajectories.</p>
</div>

### 2. Overcoming Low-Frequency Noise
Robot joint logs and vision-tracked human trajectories are noisy in qualitatively different ways. Robot streams carry high-frequency jitter around a correct nominal path, which the CNMP architecture inherently tolerates. MediaPipe trajectories, however, introduce **substantial low-frequency noise, slow spatial drift, and systematic tracking wobbles**. 

Because the CNMP encoder summarizes whole trajectory shapes, it proved highly sensitive to these low-frequency deviations. Initial training attempts using raw MediaPipe data failed to converge.
* **Conditioning Pipeline:** I developed a dedicated filtering and normalization pipeline that isolates and suppresses low-frequency drift.
* **Statistical Alignment:** This preprocessing stage reshapes raw Cartesian vision inputs into clean geometric trajectories that match the statistical properties of the robot encoder, allowing the shared latent space to converge successfully.

### 3. Deep Cartesian-to-Joint-Space Embodiment Mapping
The learned latent space was forced to bridge two distinct domain gaps simultaneously:
* **The Embodiment Gap:** Mapping a biological human arm structure to the rigid, highly articulated linkages of the Torobo manipulator.
* **The Kinematic Space Gap:** The human model operates entirely on **Cartesian wrist coordinates**, whereas the Torobo model trains and decodes **directly within its joint space**. The shared representation must therefore implicitly embed an inverse kinematics mapping natively within the cross-embodiment correspondence.

---

## Results

Trained on 7 trajectories at 30°-spaced targets, the model was evaluated on interpolated targets between trained angles — a genuine generalization test rather than a replay of a trained motion. Transfer succeeded in both directions on these held-out targets:

| Transfer Direction | Evaluation | Max End-Effector Error |
| :--- | :---: | :---: |
| Human → Torobo Robot | Video demo + trajectory comparison | ~3 cm |
| Torobo Robot → Human | Numerical comparison only | ~3 cm |

## Context

This project was completed during a summer research internship at **SISREC, Osaka University**, supervised by **Prof. Erhan Öztop**. The idea came from a discussion with **Prof. Minoru Asada** during a lab presentation, as a possible real-robot extension of the blending-CNMP paper's experiments. My internship ended before real-hardware trials were possible, and given the paper's already-substantial scope, we agreed not to add another contributor for a simulation-only result. This remains an independent project, not part of the publication.

## Citation

```bibtex
@article{aktas2023correspondence,
  title={Correspondence learning between morphologically different robots via task demonstrations},
  author={Aktas, Hakan and Nagai, Yukie and Asada, Minoru and Oztop, Erhan and Ugur, Emre},
  journal={arXiv preprint arXiv:2310.13458},
  year={2023}
}

@inproceedings{seker2019conditional,
  title={Conditional neural movement primitives},
  author={Seker, M. Yunus and Imre, Mert and Piater, Justus H. and Ugur, Emre},
  booktitle={Robotics: Science and Systems (RSS)},
  volume={10},
  year={2019}
}
```