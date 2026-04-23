# Extraction: Energy-optimal Design and Control of Electric Vehicles' Transmissions

**Key:** energy-optimal_design_2021
**Authors:** Juriaan van den Hurk, Mauro Salazar
**Year:** 2021
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

This paper presents models and optimization algorithms to jointly optimize the design and control of the transmission of electric vehicles equipped with one central electric motor (EM). First, considering the required traction power to be given, we identify a convex speed-dependent loss model for the EM. Second, we leverage such a model to devise computationally-efficient algorithms to determine the energy-optimal design and control strategies for the transmission. In particular, with the objective of minimizing the EM energy consumption on a given drive cycle, we analytically compute the optimal gear-ratio trajectory for a continuously variable transmission (CVT) and the optimal gear-ratio design for a fixed-gear transmission (FGT) in closed form, whilst efficiently solving the combinatorial joint gear-ratio design and control problem for a multiple-gear transmission (MGT), combining convex analysis and dynamic programming in an iterative fashion. Third, we validate our models with nonlinear simulations, and benchmark the optimality of our methods with mixed-integer quadratic programming. Finally, we showcase our framework in a case-study for a family vehicle, whereby we leverage the computational efficiency of our methods to jointly optimize the EM size via exhaustive search. Our numerical results show that by using a 2-speed MGT, the energy consumption of an electric vehicle can be reduced by 3% and 2.5% compared to an FGT and a CVT, respectively, whilst further increasing the number of gears may even be detrimental due to the additional weight
