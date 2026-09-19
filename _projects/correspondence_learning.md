---
title: "Human-to-Robot Skill Transfer through Correspondence Learning"
collection: projects
header:
    video_teaser: '/images/human_to_robot.mp4'
date: 2023-08-28
excerpt: "Extending the correspondence-learning framework of Aktaş et al. from robot-to-robot transfer to a human demonstrator tracked by camera. Seven demonstrations are enough to reach targets between the trained ones, with a largest observed end-effector error of 2.98 cm."
description: "Independent project at SISReC, Osaka University: transferring reaching skills from a camera-tracked human demonstrator to a simulated Torobo humanoid through a common latent representation, across a Cartesian-to-joint-space gap."
---

> Note: this is an independent project extending [Aktaş et al. (2024)](https://doi.org/10.1109/LRA.2024.3382534). I am not an author on that paper; see [Context](#context) below.

Independent project, carried out during a summer research internship at SISReC, Osaka University, supervised by Prof. Erhan Öztop.

## Abstract

Aktaş et al. learn task-level correspondences between robots with different bodies by blending the latent representations of each agent's Conditional Neural Movement Primitives into one common representation, from which either agent's trajectory can be decoded. Their conclusion names humans among the agents worth testing next. This project does that. A human reaching movement is captured with an Intel RealSense camera and MediaPipe, and the same architecture maps it onto joint trajectories for a simulated Torobo humanoid. Camera-tracked trajectories carry a slow drift that the encoder does not tolerate, and training on raw landmarks does not converge; a five-tap moving average and a per-trajectory geometric normalization condition them first. Trained on seven demonstrations at targets 30° apart, the model reaches targets lying between the trained ones, with a largest observed end-effector error of 2.98 cm.

<div class="archive__item-teaser" id="demo-video">
    <video autoplay loop muted playsinline width="100%" poster="/images/human_to_robot_poster.jpg" style="display:block; object-fit:cover;">
      <source src="/images/human_to_robot.mp4" type="video/mp4">
      Your browser cannot play this video. <a href="/images/human_to_robot.mp4">Download it here.</a>
    </video>
</div>

*Demonstration on the right, the simulated Torobo executing the decoded joint trajectory on the left. The ring around the hand follows the tracked keypoint and reports the state of the recording loop, turning green while a reach is being captured; the smaller rings are the seven training targets, drawn so that a reach can be aimed between them or past them. The targets shown lie between trained angles, so these are generalization cases rather than replays. [Full video on YouTube](https://www.youtube.com/watch?v=71mbbTE65yU).*

## Motivation

Aktaş et al. [\[1\]](#ref-1) learn task-level correspondences between robots whose bodies differ. Each agent's sensorimotor trajectories are encoded by a Conditional Neural Movement Primitives network [\[2\]](#ref-2). The resulting latent representations are combined by convex combination into a common latent representation, and each agent's own decoder reconstructs its own trajectory from it:

$$L = p \cdot L^{\text{A}} + (1-p) \cdot L^{\text{B}}, \qquad p \sim U(0,1)$$

Setting $$p$$ to 1 at inference makes that agent the source: its observations alone produce the common representation, and the other agent's trajectory is decoded from the same latent. The paper demonstrates this between manipulators and a differential-drive mobile robot.

Its conclusion names the next case as agents whose sensorimotor dimensions differ more widely, "such as humanoids, musculoskeletal robots, and even humans." A camera-tracked human is that case, and an extreme one. The demonstrator's trajectory is two image-plane coordinates; the Torobo's is five joint angles. Nothing in the architecture converts between them, so the common latent representation has to absorb an inverse-kinematics mapping along with the difference in bodies.

<div style="text-align: center; margin: 20px auto; max-width:100%;">
<img src="/images/blending_cnmp_arch.png" alt="Architecture diagram: sampled observations from each agent pass through separate encoders into per-agent latent vectors, which are combined by weighted sum into one common latent representation, and each agent's decoder reads that representation together with a query timestamp to output a trajectory mean and variance." style="width:95%; display:block; margin:20px auto;">
  <p style="font-style: italic; color: #666; margin-top: 8px;">Fig. 1: The correspondence-learning architecture. Sparse observations from each agent are encoded separately, combined into a common latent representation, and decoded through each agent's own decoder. Reproduced from <a href="https://arxiv.org/abs/2310.13458">Aktaş et al. (2024)</a>.</p>
</div>

## Method

**Capture.** Reaching movements are recorded with an Intel RealSense camera, and MediaPipe's pose model supplies the landmarks. The model consumes a single hand keypoint, which in practice sits near the base of the fingers rather than at the wrist or a fingertip, since the pose model estimates hand position from body context rather than running a dedicated hand model. The workspace is one shared start position with targets arranged along a 180° arc. Seven demonstrations are recorded, one per target, at 30° spacing. Matching Torobo trajectories are generated by inverse kinematics and logged in joint space; five of the arm's seven joints are used.

**Conditioning.** Robot joint logs and camera-tracked trajectories are noisy in different ways. Robot streams carry high-frequency jitter around a correct nominal path, which the encoder tolerates. MediaPipe trajectories drift slowly instead, and because the encoder summarizes whole trajectory shapes rather than individual samples, that drift changes the shape being encoded. Training on raw landmarks did not converge.

Two steps therefore precede encoding. A five-tap moving average is convolved along each trajectory, which suppresses the drift. Each trajectory is then translated so that its first sample lies at the origin and divided by its own maximum radius, placing its farthest point on the unit circle; at inference the scale factor is the average taken from the training set. This removes where the demonstrator sat and how far they reached, which is what makes a camera trajectory comparable with a joint-space one.

**Transfer.** A recorded reach is resampled to thirty timesteps and conditioned as above, and five of those timesteps are sampled at random as observations. The blending weight is set to 1 on the human side, so the common latent representation is formed from the human observations alone, and the Torobo decoder produces the joint trajectory the simulated arm then executes.

## Experiments

Evaluation is interactive rather than scripted. The demonstrator sits in front of the camera, a reach is recorded, and the simulated arm executes the decoded trajectory immediately afterwards. In [the video above](#demo-video), the ring around the hand follows the tracked keypoint and reports the state of that loop, turning green while a reach is being captured; the smaller rings are the seven training targets. Drawing the targets on screen is what allows a reach to be aimed deliberately between two of them, or past the end of the arc, which is how the results below were obtained.


Targets between the trained angles are reached. Across the validation points tried by hand, the largest deviation between the target and the Torobo end effector, computed by forward kinematics on the predicted joint trajectory, was 2.98 cm. Reaches ending a few centimetres outside the arc covered by training also produced sensible trajectories, although this was observed rather than measured.

## Limitations

Seven demonstrations from one demonstrator, one per target. No validation set was collected, so 2.98 cm is the largest error seen while trying targets by hand in an interactive session, not a statistic over held-out data. The extrapolation behaviour comes from the same sessions and is not quantified.

The reverse direction is implemented: decoding the common latent through the human decoder renders predicted landmarks. It was inspected on training trajectories only, never scored on held-out data, and those measurements no longer exist. A human also cannot be asked to execute a trajectory the way a robot can, so the reverse direction is a check on the latent representation rather than a transfer of skill.

The robot side is a PyBullet simulation throughout. The generated joint angles were never executed on the physical Torobo, so what the results support is that the model produces joint trajectories the simulator accepts, not that they are correct on hardware.

## Future work

Running the generated trajectories on the physical Torobo is the immediate step, and was the intended one before the internship ended. Beyond reaching, the architecture carries no information about objects: Aktaş et al. note that the geometric and visual properties of manipulated objects are not used by their model, and take that up separately in later work on affordance transfer [\[3\]](#ref-3). Transferring a grasp from a human hand to a gripper would need that addition rather than following from this one.

## Context

This project was completed during a summer research internship at SISReC, Osaka University, supervised by Prof. Erhan Öztop. The idea came from a discussion with Prof. Minoru Asada during a lab presentation, as a possible real-robot extension of the correspondence-learning experiments. The paper it builds on was posted to arXiv in October 2023 and published in RA-L in May 2024, both after this project's date, so I worked from the group's in-progress version while in the lab that summer. My internship ended before real-hardware trials were possible, and given the paper's already considerable scope, we agreed not to add another contributor for a simulation-only result. This remains an independent project, not part of the publication.

## Code

[github.com/mbatuhancelik/human2robot_cnmp](https://github.com/mbatuhancelik/human2robot_cnmp)

## References

<a id="ref-1"></a>[1] H. Aktaş, Y. Nagai, M. Asada, E. Öztop, and E. Uğur, "Correspondence Learning Between Morphologically Different Robots via Task Demonstrations," *IEEE Robotics and Automation Letters*, vol. 9, no. 5, pp. 4463–4470, May 2024. DOI: [10.1109/LRA.2024.3382534](https://doi.org/10.1109/LRA.2024.3382534)

<a id="ref-2"></a>[2] M. Y. Seker, M. Imre, J. H. Piater, and E. Uğur, "Conditional Neural Movement Primitives," in *Robotics: Science and Systems (RSS)*, vol. 10, 2019.

<a id="ref-3"></a>[3] H. Aktaş, Y. Nagai, M. Asada, M. Saveriano, E. Öztop, and E. Uğur, "Cross-Embodied Affordance Transfer through Learning Affordance Equivalences," arXiv:2404.15648, 2024.