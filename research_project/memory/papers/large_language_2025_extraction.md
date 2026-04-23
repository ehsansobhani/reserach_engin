# Extraction: Large Language Model-Assisted Planning of Electric Vehicle Charging Infrastructure with Real-World Case Study

**Key:** large_language_2025
**Authors:** Xinda Zheng, Canchen Jiang, Hao Wang
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
- **Phased approach:** True
- **Zoning considered:** False
- **Meso-level:** False
- **Micro-level:** False

## Gap Mapping

- **Gap 1 (Misaligned spatial units):** True
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** False
- **Gap 4 (Phased rollout):** True
- **Gap 5 (Meso-micro bridge):** False

## Limitations Detected

None detected in abstract.

## Abstract

The growing demand for electric vehicle (EV) charging infrastructure presents significant planning challenges, requiring efficient strategies for investment and operation to deliver cost-effective charging services. However, the potential benefits of EV charging assignment, particularly in response to varying spatial-temporal patterns of charging demand, remain under-explored in infrastructure planning. This paper proposes an integrated approach that jointly optimizes investment decisions and charging assignments while accounting for spatial-temporal demand dynamics and their interdependencies. To support efficient model development, we leverage a large language model (LLM) to assist in generating and refining the mathematical formulation from structured natural-language descriptions, significantly reducing the modeling burden. The resulting optimization model enables optimal joint decision-making for investment and operation. Additionally, we propose a distributed optimization algorithm based on the Alternating Direction Method of Multipliers (ADMM) to address computational complexity in high-dimensional scenarios, which can be executed on standard computing platforms. We validate our approach through a case study using 1.5 million real-world travel records from Chengdu, China, demonstrating a 30% reduction in total cost compared to a baseline without EV assignment.
