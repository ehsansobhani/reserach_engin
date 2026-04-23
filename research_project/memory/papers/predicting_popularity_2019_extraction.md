# Extraction: Predicting popularity of EV charging infrastructure from GIS data

**Key:** predicting_popularity_2019
**Authors:** Milan Straka, Pasquale De Falco, Gabriella Ferruzzi, Daniela Proto, Gijs van der Poel, Shahab Khormali, Ľuboš Buzna
**Year:** 2019
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** optimization
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

The availability of charging infrastructure is essential for large-scale adoption of electric vehicles (EV). Charging patterns and the utilization of infrastructure have consequences not only for the energy demand, loading local power grids but influence the economic returns, parking policies and further adoption of EVs. We develop a data-driven approach that is exploiting predictors compiled from GIS data describing the urban context and urban activities near charging infrastructure to explore correlations with a comprehensive set of indicators measuring the performance of charging infrastructure. The best fit was identified for the size of the unique group of visitors (popularity) attracted by the charging infrastructure. Consecutively, charging infrastructure is ranked by popularity. The question of whether or not a given charging spot belongs to the top tier is posed as a binary classification problem and predictive performance of logistic regression regularized with an l-1 penalty, random forests and gradient boosted regression trees is evaluated. Obtained results indicate that the collected predictors contain information that can be used to predict the popularity of charging infrastructure. The significance of predictors and how they are linked with the popularity are explored as well. The proposed methodology can be used to inform charging infrastructure deployment strategies.
