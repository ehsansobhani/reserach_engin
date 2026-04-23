# Extraction: Robust charging station location and routing-scheduling for electric modular autonomous units

**Key:** robust_charging_2025
**Authors:** Dongyang Xia, Lixing Yang, Yahan Lu, Shadi Sharif Azadeh
**Year:** 2025
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** corridor
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

- **Gap 1 (Misaligned spatial units):** True
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** False
- **Gap 4 (Phased rollout):** False
- **Gap 5 (Meso-micro bridge):** False

## Limitations Detected

None detected in abstract.

## Abstract

Problem definition: Motivated by global electrification targets and the advent of electric modular autonomous units (E-MAUs), this paper addresses a robust charging station location and routing-scheduling problem (E-RCRSP) in an inter-modal transit system, presenting a novel solution to traditional electric bus scheduling. The system integrates regular bus services, offering full-line or sectional coverage, and short-turning services. Considering the fast-charging technology with quick top-ups, we jointly optimize charging station locations and capacities, fleet sizing, as well as routing-scheduling for E-MAUs under demand uncertainty. E-MAUs can couple flexibly at different locations, and their routing-scheduling decisions include sequences of services, as well as charging times and locations. Methodology: The E-RCRSP is formulated as a path-based robust optimization model, incorporating the polyhedral uncertainty set. We develop a double-decomposition algorithm that combines column-and-constraint generation and column generation armed with a tailored label-correcting approach. To improve computational efficiency and scalability, we propose a novel method that introduces super travel arcs and network downsizing methodologies. Results: Computational results from real-life instances, based on operational data of advanced NExT E-MAUs with cutting-edge batteries provided by our industry partner, indicate that charging at both depots and en-route fast-charging stations is necessary during operations. Moreover, our algorithm effectively scales to large-scale operational cases involving entire-day operations, significantly outperforming state-of-the-art methods. Comparisons with fixed-composition buses under the same fleet investment suggest that our methods are able to achieve substantial reductions in passengers' costs by flexibly scheduling units.
