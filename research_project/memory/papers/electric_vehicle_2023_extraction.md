# Extraction: Electric Vehicle Fleet and Charging Infrastructure Planning

**Key:** electric_vehicle_2023
**Authors:** Sushil Mahavir Varma, Francisco Castro, Siva Theja Maguluri
**Year:** 2023
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** simulation
- **Data source:** not specified
- **Multi-objective:** False

## Thematic Flags

- **Equity measured:** False
- **Utilization measured:** True
- **Phased approach:** False
- **Zoning considered:** False
- **Meso-level:** True
- **Micro-level:** False

## Gap Mapping

- **Gap 1 (Misaligned spatial units):** True
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** False
- **Gap 4 (Phased rollout):** False
- **Gap 5 (Meso-micro bridge):** True

## Limitations Detected

None detected in abstract.

## Abstract

We study electric vehicle (EV) fleet and charging infrastructure planning in a spatial setting. With customer requests arriving continuously at rate $λ$ throughout the day, we determine the minimum number of vehicles and chargers for a target service level, along with matching and charging policies. While non-EV systems require extra $Θ(λ^{2/3})$ vehicles due to pickup times, EV systems differ. Charging increases nominal capacity, enabling pickup time reductions and allowing for an extra fleet requirement of only $Θ(λ^ν)$ for $ν\in (1/2, 2/3]$, depending on charging infrastructure and battery pack sizes. We propose the Power-of-$d$ dispatching policy, which achieves this performance by selecting the closest vehicle with the highest battery level from $d$ options. We extend our results to accommodate time-varying demand patterns and discuss conditions for transitioning between EV and non-EV capacity planning. Extensive simulations verify our scaling results, insights, and policy effectiveness while also showing the viability of low-range, low-cost fleets.
