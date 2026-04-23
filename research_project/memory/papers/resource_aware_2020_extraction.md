# Extraction: Resource Aware Pricing for Electric Vehicle Charging

**Key:** resource_aware_2020
**Authors:** Cesar Santoyo, Gustav Nilsson, Samuel Coogan
**Year:** 2020
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** mixed
- **Data source:** not specified
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

- Both parking availability and electric charge capacity are constrained resources, and as the demand for charging facilities grows with increasing electric vehicle adoption, so too does the potential for exceeding these resource limitations.

## Abstract

Electric vehicle charging facilities offer electric charge and parking to users for a fee. Both parking availability and electric charge capacity are constrained resources, and as the demand for charging facilities grows with increasing electric vehicle adoption, so too does the potential for exceeding these resource limitations. In this paper, we study how prices set by the charging facility impact the likelihood that resource constraints are exceeded. Specifically, we present probabilistic bounds on the number of charging spots and the total power supply needed at a facility based on the characteristics of the arriving vehicles. We assume the charging facility either offers a set of distinct and fixed charging rates to each user or allows the user to decide a charging deadline, from which a charging rate is determined. Users arrive randomly, requiring a random amount of charge. Additionally, each user has a random impatience factor that quantifies their value of time, and a random desired time to stay at a particular location. Assuming rational user behavior, and with knowledge of the probability distribution of the random parameters, we present high-confidence bounds on the total number of vehicles parked at the station and the aggregate power use of all vehicles actively charging. We demonstrate how these bounds can be used by a charging facility to determine appropriate prices and investigate through a Monte-Carlo simulation case study the tightness of the bounds.
