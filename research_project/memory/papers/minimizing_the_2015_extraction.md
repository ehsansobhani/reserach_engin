# Extraction: Minimizing the impact of EV charging on the electricity distribution network

**Key:** minimizing_the_2015
**Authors:** Olivier Beaude, Samson Lasaulce, Martin Hennebel, Jamal Daafouz
**Year:** 2015
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

The main objective of this paper is to design electric vehicle (EV) charging policies which minimize the impact of charging on the electricity distribution network (DN). More precisely, the considered cost function results from a linear combination of two parts: a cost with memory and a memoryless cost. In this paper, the first component is identified to be the transformer ageing while the second one corresponds to distribution Joule losses. First, we formulate the problem as a non-trivial discrete-time optimal control problem with finite time horizon. It is non-trivial because of the presence of saturation constraints and a non-quadratic cost. It turns out that the system state, which is the transformer hot-spot (HS) temperature here, can be expressed as a function of the sequence of control variables; the cost function is then seen to be convex in the control for typical values for the model parameters. The problem of interest thus becomes a standard optimization problem. While the corresponding problem can be solved by using available numerical routines, three distributed charging policies are provided. The motivation is threefold: to decrease the computational complexity; to model the important scenario where the charging profile is chosen by the EV itself; to circumvent the allocation problem which arises with the proposed formulation. Remarkably, the performance loss induced by decentralization is verified to be small through simulations. Numerical results show the importance of the choice of the charging policies. For instance, the gain in terms of transformer lifetime can be very significant when implementing advanced charging policies instead of plug-and-charge policies. The impact of the accuracy of the non-EV demand forecasting is equally assessed.
