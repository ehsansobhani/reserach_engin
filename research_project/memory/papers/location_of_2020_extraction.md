# Extraction: Location of Charging Stations in Electric Car Sharing Systems

**Key:** location_of_2020
**Authors:** Georg Brandstätter, Markus Leitner, Ivana Ljubić
**Year:** 2020
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

<jats:p> Electric vehicles are prime candidates for use within urban car sharing systems, both from economic and environmental perspectives. However, their relatively short range necessitates frequent and rather time-consuming recharging throughout the day. Thus, charging stations must be built throughout the system’s operational area where cars can be charged between uses. In this work, we introduce and study an optimization problem that models the task of finding optimal locations and sizes for charging stations, using the number of expected trips that can be accepted (or their resulting revenue) as a gauge of quality. Integer linear programming formulations and construction heuristics are introduced, and the resulting algorithms are tested on grid-graph-based instances, as well as on real-world instances from Vienna. The results of our computational study show that the best-performing exact algorithm solves most of the benchmark instances to optimality and usually provides small optimality gaps for the remaining ones, whereas our heuristics provide high-quality solutions very quickly. Our algorithms also provide better solutions than a sequential approach that considers strategic and operational decisions separately. A cross-validation study analyzes the algorithms’ performance in cases where demand is uncertain and shows the advantage of combining individual solutions into a single consensus solution, and a simulation study investigates their behavior in car sharing systems that provide their customers with more flexibility regarding vehicle selection. </jats:p>
