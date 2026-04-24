# Extraction: Predictive Energy Management Strategy for Range-Extended Electric Vehicles Based on ITS Information and Start–Stop Optimization with Vehicle Velocity Forecast

**Key:** predictive_energy_2022
**Authors:** Weiyi Lin, Han Zhao, Bingzhan Zhang, Ye Wang, Yan Xiao, Kang Xu, Rui Zhao
**Year:** 2022
**Category:** spatial_optimization

## Problem Scope

- **Geographic scope:** city
- **Spatial unit:** not specified

## Methodology

- **Approach:** mixed
- **Data source:** real
- **Multi-objective:** False

## Thematic Flags

- **Equity measured:** False
- **Utilization measured:** False
- **Phased approach:** False
- **Zoning considered:** False
- **Meso-level:** True
- **Micro-level:** False

## Gap Mapping

- **Gap 1 (Misaligned spatial units):** True
- **Gap 2 (Zoning impact analysis):** False
- **Gap 3 (Equity-utilization joint):** False
- **Gap 4 (Phased rollout):** False
- **Gap 5 (Meso-micro bridge):** True

## Limitations Detected

None detected in abstract.

## Abstract

<jats:p>Range-extended Electric Vehicles (REVs) have become popular due to their lack of emissions while driving in urban areas, and the elimination of range anxiety when traveling long distances with a combustion engine as the power source. The fuel consumption performance of REVs depends greatly on the energy management strategy (EMS). This article proposes a practical energy management solution for REVs based on an Adaptive Equivalent Fuel Consumption Minimization Strategy (A-ECMS), wherein the equivalent factor is dynamically optimized by the battery’s State of Charge (SoC) and traffic information provided by Intelligent Transportation Systems (ITS). Furthermore, a penalty function is incorporated with the A-ECMS strategy to achieve the quasi-optimal start–stop control of the range extender. The penalty function is designed based on more precise vehicle velocity forecasting through a nonlinear autoregressive network with exogeneous input (NARX). A model of the studied REV is established in the AVL Cruise environment and the proposed energy management strategy is set up in Matlab/Simulink. Lastly, the performance of the proposed strategy is evaluated over multiple Worldwide Light-duty Test Cycles (WLTC) and real-world driving cycles through model simulation. The simulation conditions are preset such that the range extender must be switched on to finish the planned route. Compared with the basic Charge-Depleting and Charge-Sustaining (CD-CS) strategy, the proposed A-ECMS strategy achieves a fuel-consumption benefit of up to 9%. With the implementation of range extender start–stop optimization, which is based on velocity forecasting, the fuel saving rate can be further improved by 6.7% to 18.2% compared to the base A-ECMS. The proposed strategy is energy efficient, with a simple structure, and it is intended to be implemented on the studied vehicle, which will be available on the market at the end of October 2022.</jats:p>
