# Extraction: Optimizing Electric Vehicle Charging Station Placement Using Reinforcement Learning and Agent-Based Simulations

**Key:** optimizing_electric_2025
**Authors:** Minh-Duc Nguyen, Dung D. Le, Phi Long Nguyen
**Year:** 2025
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** mixed
- **Data source:** real
- **Multi-objective:** False

## Thematic Flags

- **Equity measured:** False
- **Utilization measured:** True
- **Phased approach:** False
- **Zoning considered:** False
- **Meso-level:** False
- **Micro-level:** False

## Gap Mapping

- **Gap 1 (Misaligned spatial units):** True
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** False
- **Gap 4 (Phased rollout):** False
- **Gap 5 (Meso-micro bridge):** False

## Limitations Detected

- Because real-world conditions are dynamic and uncertain, a deterministic reward structure cannot fully capture the complexities of charging station placement.

## Abstract

The rapid growth of electric vehicles (EVs) necessitates the strategic placement of charging stations to optimize resource utilization and minimize user inconvenience. Reinforcement learning (RL) offers an innovative approach to identifying optimal charging station locations; however, existing methods face challenges due to their deterministic reward systems, which limit efficiency. Because real-world conditions are dynamic and uncertain, a deterministic reward structure cannot fully capture the complexities of charging station placement. As a result, evaluation becomes costly and time-consuming, and less reflective of real-world scenarios. To address this challenge, we propose a novel framework that integrates deep RL with agent-based simulations to model EV movement and estimate charging demand in real time. Our approach employs a hybrid RL agent with dual Q-networks to select optimal locations and configure charging ports, guided by a hybrid reward function that combines deterministic factors with simulation-derived feedback. Case studies in Hanoi, Vietnam, show that our method reduces average waiting times by 53.28% compared to the initial state, outperforming static baseline methods. This scalable and adaptive solution enhances EV infrastructure planning, effectively addressing real-world complexities and improving user experience.
