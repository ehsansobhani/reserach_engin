# Extraction: Competitive EV charging station location with queues

**Key:** competitive_ev_2025
**Authors:** The Minh Nguyen, Nagisa Sugishita, Margarida Carvalho, Amira Dems
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
- **Utilization measured:** False
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

None detected in abstract.

## Abstract

Electric vehicle (EV) public charging infrastructure planning faces significant challenges in competitive markets, where multiple service providers affect congestion and user behavior. This work extends existing modeling frameworks by incorporating the presence of competitors' stations and more realistic queueing systems.
  First, we analyze three finite queueing systems, M/M/1/K, M/M/s/K, and M/Er/s/K, with varying numbers of servers (charging outlets) and service time distributions, deriving analytic expressions for user behavior metrics. Second, we embed the queueing-based user behavior model into a bilevel program, where the upper level locates new charging stations to maximize accessibility (throughput), and the lower level captures users' station choices via a user equilibrium. Third, we apply a reformulation from competitive congested user-choice facility location models to approximately solve the bilevel problem and introduce a surrogate-based heuristic to enhance scalability. Fourth, we showcase our methodology on a real-world case study of an urban area in Montreal (Canada), offering managerial insights into how user-choice behavior assumptions and competition affect throughput and location decisions. The results demonstrate that our model yields (re)location strategies that outperform the existing network. More broadly, this approach provides a tool for incorporating charging service quality-through queueing metrics-and existing competition into station planning.
