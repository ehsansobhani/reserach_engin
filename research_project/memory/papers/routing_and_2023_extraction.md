# Extraction: Routing and charging game in ride-hailing service with electric vehicles

**Key:** routing_and_2023
**Authors:** Kenan Zhang, John Lygeros
**Year:** 2023
**Category:** general

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** optimization
- **Data source:** not specified
- **Multi-objective:** False

## Thematic Flags

- **Equity measured:** False
- **Utilization measured:** False
- **Phased approach:** False
- **Zoning considered:** False
- **Meso-level:** False
- **Micro-level:** False

## Gap Mapping

- **Gap 1 (Misaligned spatial units):** False
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** False
- **Gap 4 (Phased rollout):** False
- **Gap 5 (Meso-micro bridge):** False

## Limitations Detected

None detected in abstract.

## Abstract

This paper studies the routing and charging behaviors of electric vehicles in a competitive ride-hailing market. When the vehicles are idle, they can choose whether to continue cruising to search for passengers, or move a charging station to recharge. The behaviors of individual vehicles are then modeled by a Markov decision process (MDP). The state transitions in the MDP model, however, depend on the aggregate vehicle flows both in service zones and at charging stations. Accordingly, the value function of each vehicle is determined by the collective behaviors of all vehicles. With the assumption of the large population, we formulate the collective routing and charging behaviors as a mean-field Markov game. We characterize the equilibrium of such a game, prove its existence, and numerically show that the competition among vehicles leads to ``inefficient congestion" both in service zones and at charging stations.
