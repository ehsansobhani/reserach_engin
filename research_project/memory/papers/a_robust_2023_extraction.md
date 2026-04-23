# Extraction: A Robust and Efficient Optimization Model for Electric Vehicle Charging Stations in Developing Countries under Electricity Uncertainty

**Key:** a_robust_2023
**Authors:** Mansur Arief, Yan Akhra, Iwan Vanany
**Year:** 2023
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** mixed
- **Data source:** not specified
- **Multi-objective:** False

## Thematic Flags

- **Equity measured:** True
- **Utilization measured:** True
- **Phased approach:** False
- **Zoning considered:** False
- **Meso-level:** False
- **Micro-level:** False

## Gap Mapping

- **Gap 1 (Misaligned spatial units):** True
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** True
- **Gap 4 (Phased rollout):** False
- **Gap 5 (Meso-micro bridge):** False

## Limitations Detected

None detected in abstract.

## Abstract

The rising demand for electric vehicles (EVs) worldwide necessitates the development of robust and accessible charging infrastructure, particularly in developing countries where electricity disruptions pose a significant challenge. Earlier charging infrastructure optimization studies do not rigorously address such service disruption characteristics, resulting in suboptimal infrastructure designs. To address this issue, we propose an efficient simulation-based optimization model that estimates candidate stations' service reliability and incorporates it into the objective function and constraints. We employ the control variates (CV) variance reduction technique to enhance simulation efficiency. Our model provides a highly robust solution that buffers against uncertain electricity disruptions, even when candidate station service reliability is subject to underestimation or overestimation. Using a dataset from Surabaya, Indonesia, our numerical experiment demonstrates that the proposed model achieves a 13% higher average objective value compared to the non-robust solution. Furthermore, the CV technique successfully reduces the simulation sample size up to 10 times compared to Monte Carlo, allowing the model to solve efficiently using a standard MIP solver. Our study provides a robust and efficient solution for designing EV charging infrastructure that can thrive even in developing countries with uncertain electricity disruptions.
