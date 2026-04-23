# Extraction: M-BEV: Masked BEV Perception for Robust Autonomous Driving

**Key:** m-bev_masked_2023
**Authors:** Siran Chen, Yue Ma, Yu Qiao, Yali Wang
**Year:** 2023
**Category:** utilization_modeling

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** optimization
- **Data source:** not specified
- **Multi-objective:** False

## Thematic Flags

- **Equity measured:** False
- **Utilization measured:** True
- **Phased approach:** True
- **Zoning considered:** False
- **Meso-level:** False
- **Micro-level:** False

## Gap Mapping

- **Gap 1 (Misaligned spatial units):** False
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** False
- **Gap 4 (Phased rollout):** True
- **Gap 5 (Meso-micro bridge):** False

## Limitations Detected

None detected in abstract.

## Abstract

3D perception is a critical problem in autonomous driving. Recently, the Bird-Eye-View (BEV) approach has attracted extensive attention, due to low-cost deployment and desirable vision detection capacity. However, the existing models ignore a realistic scenario during the driving procedure, i.e., one or more view cameras may be failed, which largely deteriorates the performance. To tackle this problem, we propose a generic Masked BEV (M-BEV) perception framework, which can effectively improve robustness to this challenging scenario, by random masking and reconstructing camera views in the end-to-end training. More specifically, we develop a novel Masked View Reconstruction (MVR) module for M-BEV. It mimics various missing cases by randomly masking features of different camera views, then leverages the original features of these views as self-supervision, and reconstructs the masked ones with the distinct spatio-temporal context across views. Via such a plug-and-play MVR, our M-BEV is capable of learning the missing views from the resting ones, and thus well generalized for robust view recovery and accurate perception in the testing. We perform extensive experiments on the popular NuScenes benchmark, where our framework can significantly boost 3D perception performance of the state-of-the-art models on various missing view cases, e.g., for the absence of back view, our M-BEV promotes the PETRv2 model with 10.3% mAP gain.
