# Extraction: Reducing Waiting Times at Charging Stations with Adaptive Electric Vehicle Route Planning

**Key:** reducing_waiting_2021
**Authors:** Sven Schoenberg, Falko Dressler
**Year:** 2021
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** simulation
- **Data source:** not specified
- **Multi-objective:** True

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

Electric vehicles are becoming more popular all over the world. With increasing battery capacities and a growing fast-charging infrastructure, they are becoming suitable for long distance travel. However, queues at charging stations could lead to long waiting times, making efficient route planning even more important. In general, optimal multi-objective route planning is extremely computationally expensive. We propose an adaptive charging and routing strategy, which considers driving, waiting, and charging time. For this, we developed a multi-criterion shortest-path search algorithm using contraction hierarchies. To further reduce the computational effort, we precompute shortest-path trees between the known locations of the charging stations. We propose a central charging station database (CSDB) that helps estimating waiting times at charging stations ahead of time. This enables our adaptive charging and routing strategy to reduce these waiting times. In an extensive set of simulation experiments, we demonstrate the advantages of our concept, which reduces average waiting times at charging stations by up to 97 %. Even if only a subset of the cars uses the CSDB approach, we can substantially reduce waiting times and thereby the total travel time of electric vehicles.
