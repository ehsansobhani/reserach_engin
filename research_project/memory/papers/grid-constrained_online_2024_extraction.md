# Extraction: Grid-constrained online scheduling of flexible electric vehicle charging

**Key:** grid-constrained_online_2024
**Authors:** Emily van Huffelen, Roel Brouwer, Marjan van den Akker
**Year:** 2024
**Category:** utilization_modeling

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** simulation
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

- **Gap 1 (Misaligned spatial units):** False
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** False
- **Gap 4 (Phased rollout):** False
- **Gap 5 (Meso-micro bridge):** False

## Limitations Detected

None detected in abstract.

## Abstract

We study Electric Vehicle (EV) charging from a scheduling perspective, aiming to minimize delays while respecting the grid constraints. A network of parking lots is considered, each with a given number of charging stations for electric vehicles. Some of the parking lots have a roof with solar panels. The demand that can be served at each parking lot is limited by the capacity of the cables connecting them to the grid. We assume that EVs arrive at the parking lots according to a known distribution. Upon arrival, we learn the desired departure time, the amount of electrical energy it needs to charge its battery, and the range of rates that it can be charged at. Vehicle arrival patterns, connection times, and charging volume are based on data collected in the city of Utrecht. The departure time of an EV is delayed if it has not finished charging in time for its desired departure. We aim to minimize the total delay. We present a novel approach, based on an online variant of well-known schedule generation schemes. We extend these schemes and include them in a destroy-and-repair heuristic. This resulted in several scheduling strategies. We show their effectiveness using a discrete event simulation. With this, we show that applying scheduling approaches increases the amount of EVs that can be charged at a site and reduces the average delay. Furthermore, we argue the importance of considering aspects of the grid layout in electricity networks and show the benefits of using flexible charging rates.
