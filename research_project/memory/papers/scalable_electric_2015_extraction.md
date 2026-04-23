# Extraction: Scalable Electric Vehicle Charging Protocols

**Key:** scalable_electric_2015
**Authors:** Liang Zhang, Vassilis Kekatos, Georgios B. Giannakis
**Year:** 2015
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

- Nevertheless, the task of optimal electric vehicle charging scales unfavorably with the fleet size and the number of control periods, especially when distribution grid limitations are enforced.
- Leveraging a linearized model for unbalanced distribution grids, the goal is to minimize the power supply cost while respecting critical voltage regulation and substation capacity limitations.

## Abstract

Although electric vehicles are considered a viable solution to reduce greenhouse gas emissions, their uncoordinated charging could have adverse effects on power system operation. Nevertheless, the task of optimal electric vehicle charging scales unfavorably with the fleet size and the number of control periods, especially when distribution grid limitations are enforced. To this end, vehicle charging is first tackled using the recently revived Frank-Wolfe method. The novel decentralized charging protocol has minimal computational requirements from vehicle controllers, enjoys provable acceleration over existing alternatives, enhances the security of the pricing mechanism against data attacks, and protects user privacy. To comply with voltage limits, a network-constrained EV charging problem is subsequently formulated. Leveraging a linearized model for unbalanced distribution grids, the goal is to minimize the power supply cost while respecting critical voltage regulation and substation capacity limitations. Optimizing variables across grid nodes is accomplished by exchanging information only between neighboring buses via the alternating direction method of multipliers. Numerical tests corroborate the optimality and efficiency of the novel schemes.
