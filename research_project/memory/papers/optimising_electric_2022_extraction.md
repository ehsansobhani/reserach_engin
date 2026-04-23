# Extraction: Optimising Electric Vehicle Charging Station Placement using Advanced Discrete Choice Models

**Key:** optimising_electric_2022
**Authors:** Steven Lamontagne, Margarida Carvalho, Emma Frejinger, Bernard Gendron, Miguel F. Anjos, Ribal Atallah
**Year:** 2022
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

We present a new model for finding the optimal placement of electric vehicle charging stations across a multi-period time frame so as to maximise electric vehicle adoption. Via the use of advanced discrete choice models and user classes, this work allows for a granular modelling of user attributes and their preferences in regard to charging station characteristics. Instead of embedding an analytical probability model in the formulation, we adopt a simulation approach and pre-compute error terms for each option available to users for a given number of scenarios. This results in a bilevel optimisation model that is, however, intractable for all but the simplest instances. Using the pre-computed error terms to calculate the users covered by each charging station allows for a maximum covering model, for which solutions can be found more efficiently than for the bilevel formulation. The maximum covering formulation remains intractable in some instances, so we propose rolling horizon, greedy, and GRASP heuristics to obtain good quality solutions more efficiently. Extensive computational results are provided, which compare the maximum covering formulation with the current state-of-the-art, both for exact solutions and the heuristic methods.
  Keywords: Electric vehicle charging stations, facility location, integer programming, discrete choice models, maximum covering
