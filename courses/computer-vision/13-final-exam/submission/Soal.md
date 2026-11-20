# Soal

## Learning Outcome

- **LO1**: Describe various computational principles and standard image processing operators in computer vision
- **LO2**: Explain the local features with their detectors and descriptors in computer vision
- **LO3**: Employ various features to find the correspondence between images and perform recognition in computer vision

## Exam Instructions

You will receive a Jupyter notebook file named **vision_engine_v1.ipynb**, a *buggy and unstable image-matching pipeline*.

You must **analyze, fix, and improve** the system using your own captured images (see dataset rules below).

## Dataset Requirement

- You must capture **your own images** using any device.
- Minimum resolution: **960×720 (HD)**.
- Each pair must depict the same scene under different conditions.
  - *Pair A:* Illumination change (e.g., different lighting).
  - *Pair B:* Viewpoint change (e.g., slight rotation or shift).
  - *Optional Pair C:* Scale or rotation variation.
- Safe, original content only. Blur faces or private objects if needed.

## I. Case (100%)

You've just joined NeuraSight, a startup building an autonomous drone vision system to map environments using camera inputs. The team's existing notebook, `vision_engine_v1.ipynb`, was supposed to detect and match features between drone-captured images, but the engineer who wrote it left abruptly. The code runs, but its results are scientifically wrong:

- Corners drift randomly between runs.
- RANSAC fails to find consistent inliers.
- Illumination and viewpoint changes cause descriptor mismatches.
- Edge detection looks correct, yet downstream feature matching fails.

Your supervisor assigns you to stabilize, analyze, and justify the system using your own captured image pairs.

### 1. [LO1, 30 points] Algorithmic Instability and Theoretical Comprehension

You discover that several modules of the provided system are unstable:

- Gaussian smoothing (incorrect σ and normalization)
- Canny edge detection (reversed thresholds)
- Harris corner detection (unnormalized response)
- RANSAC (strict threshold and low iterations)

Tasks:

a. [LO1, 5 points] Identify and explain the mathematical or computational cause of each instability.
b. [LO1, 10 points] Visualize the impact of incorrect parameters (e.g., corner count, edge noise).
c. [LO1, 5 points] Propose and implement corrected versions, with quantitative comparison.
d. [LO1, 10 points] Provide theoretical justification for your corrections using equations and short commentary.

### 2. [LO2, 30 points] Local Feature Descriptor Redesign

The current system uses raw pixel patches as descriptors, which are highly sensitive to illumination and viewpoint changes.

Tasks:

a. [LO2, 5 points] Design and implement an improved classical descriptor (e.g., gradient-based HOG, LBP, or hybrid).
b. [LO2, 10 points] Explain the theoretical advantage of your descriptor in terms of invariance and distinctiveness.
c. [LO2, 5 points] Test your descriptor using your captured image pairs.
d. [LO2, 10 points] Show before-and-after matching visualizations and discuss improvements.

### 3. [LO3, 40 points] Image Correspondence and Recognition Application

Now that your pipeline is stable and robust, Tasks:

a. [LO3, 10 points] Compute image correspondences between your captured image pairs using your improved system.
b. [LO3, 10 points] Apply RANSAC-based geometric verification to refine matches.
c. [LO3, 10 points] Measure:
   - Number of matched inliers,
   - Average reprojection error,
   - Recognition success (e.g., correctly identifying the same scene).
d. [LO3, 10 points] Reflect on how your final pipeline demonstrates robustness to real-world variation (lighting, scale, angle).

### 4. [LO1, LO2, LO3, 10 pts Bonus] Comparative Experiment (Optional)

Run a controlled comparison between two different descriptors (e.g., your design vs. HOG/LBP). Present a short table of quantitative results and your interpretation.
