# Extraction: Electric Vehicle Scheduling with Capacitated Charging Stations and Partial Charging

**Key:** electric_vehicle_2022
**Authors:** Marelot de Vos, Rolf Nelson van Lieshout, Twan Dollevoet
**Year:** 2022
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

None detected in abstract.

## Abstract

This paper considers the scheduling of electric vehicles in a public transit system. Our main innovation is that we take into account that charging stations have limited capacity, while also considering partial charging. To solve the problem, we expand a connection-based network in order to track the state of charge of vehicles and model recharging actions. We then formulate the electric vehicle scheduling problem as a path-based binary program, whose linear relaxation we solve using column generation. We find integer feasible solutions using two heuristics: price-and-branch and truncated column generation, including acceleration strategies. We test the approach using data of the concession Gooi en Vechtstreek in the Netherlands, containing up to 816 trips. The truncated column generation outperforms the other heuristic, and solves the entire concession within 28 hours of computation time with an optimality gap less than 3.5 percent.
