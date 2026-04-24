# Extraction: A Spatially Aware Machine Learning Method for Locating Electric Vehicle Charging Stations

**Key:** a_spatially_2025
**Authors:** Yanyan Huang, Hangyi Ren, Xudong Jia, Xianyu Yu, Dong Xie, You Zou, Daoyuan Chen, Yi Yang
**Year:** 2025
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** grid cell

## Methodology

- **Approach:** mixed
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

- Previous methods for locating EVCSs rely on statistical and optimization models, but these methods have limitations in capturing complex nonlinear relationships and spatial dependencies among factors influencing EVCS locations.

## Abstract

<jats:p>The rapid adoption of electric vehicles (EVs) has driven a strong need for optimizing locations of electric vehicle charging stations (EVCSs). Previous methods for locating EVCSs rely on statistical and optimization models, but these methods have limitations in capturing complex nonlinear relationships and spatial dependencies among factors influencing EVCS locations. To address this research gap and better understand the spatial impacts of urban activities on EVCS placement, this study presents a spatially aware machine learning (SAML) method that combines a multi-layer perceptron (MLP) model with a spatial loss function to optimize EVCS sites. Additionally, the method uses the Shapley additive explanation (SHAP) technique to investigate nonlinear relationships embedded in EVCS placement. Using the city of Wuhan as a case study, the SAML method reveals that parking site (PS), road density (RD), population density (PD), and commercial residential (CR) areas are key factors in determining optimal EVCS sites. The SAML model classifies these grid cells into no EVCS demand (0 EVCS), low EVCS demand (from 1 to 3 EVCSs), and high EVCS demand (4+ EVCSs) classes. The model performs well in predicting EVCS demand. Findings from ablation tests also indicate that the inclusion of spatial correlations in the model’s loss function significantly enhances the model’s performance. Additionally, results from case studies validate that the model is effective in predicting EVCSs in other metropolitan cities.</jats:p>
