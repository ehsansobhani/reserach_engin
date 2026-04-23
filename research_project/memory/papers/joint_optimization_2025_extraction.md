# Extraction: Joint Optimization of Electric Vehicle Routes and Charging Locations Learning Charge Constraints Using QUBO Solver

**Key:** joint_optimization_2025
**Authors:** Akihisa Okada, Keisuke Otaki, Hiroaki Yoshida
**Year:** 2025
**Category:** spatial_optimization

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

Optimal routing problems of electric vehicles (EVs) have attracted much attention in recent years, and installation of charging stations is an important issue for EVs. Hence, we focus on the joint optimization of the location of charging stations and the routing of EVs. When routing problems are formulated in the form of quadratic unconstrained binary optimization (QUBO), specialized solvers such as quantum annealer are expected to provide optimal solutions with high speed and accuracy. However, battery capacity constraints make it hard to formulate into QUBO form without a large number of auxiliary qubits. Then, we propose a sequential optimization method utilizing the Bayesian inference and QUBO solvers, in which method the battery capacity constraints are automatically learned. This method enables us to optimize the number and location of charging stations and the routing of EVs with a small number of searches. Applying this method to a routing problem of 20 locations, we confirmed that the learning process works well and efficient searches find good solutions. This result enhances the possibility that the QUBO solver could be applied to the constraints contained problems which is difficult to formulate into QUBO form without a large number of ancilla qubits.
