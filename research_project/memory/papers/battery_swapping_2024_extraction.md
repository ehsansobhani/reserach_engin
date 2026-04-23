# Extraction: Battery swapping station location for electric vehicles: a simulation optimization approach

**Key:** battery_swapping_2024
**Authors:** Guangyuan Liu, Yu Zhang, Tianshi Ming, Chunlong Yu
**Year:** 2024
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** neighborhood
- **Spatial unit:** not specified

## Methodology

- **Approach:** mixed
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

- **Gap 1 (Misaligned spatial units):** True
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** False
- **Gap 4 (Phased rollout):** True
- **Gap 5 (Meso-micro bridge):** False

## Limitations Detected

None detected in abstract.

## Abstract

Electric vehicles face significant energy supply challenges due to long charging times and congestion at charging stations. Battery swapping stations (BSSs) offer a faster alternative for energy replenishment, but their deployment costs are considerably higher than those of charging stations. As a result, selecting optimal locations for BSSs is crucial to improve their accessibility and utilization. Most existing studies model the BSS location problem using deterministic and static approaches, often overlooking the impact of stochastic and dynamic factors on solution quality. This paper addresses the facility location problem for BSSs within a city network, considering stochastic battery swapping demand. The objective is to optimize the placement of a given set of BSSs to minimize demand loss. To achieve this, we first develop a mathematical programming model for the problem. Then, we propose a simulation optimization method based on a large neighborhood search framework to handle large-scale instances. To reduce the computational cost of simulations, Bayesian optimization is employed to solve the single-station allocation subproblem during the repair process. Numerical experiments demonstrate the efficiency of the proposed approach and highlight the importance of incorporating dynamic factors in decision-making.
