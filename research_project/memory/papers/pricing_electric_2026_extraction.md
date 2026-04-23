# Extraction: Pricing Electric Vehicle Charging and Station Access via Copositive Duality

**Key:** pricing_electric_2026
**Authors:** Nanfei Jiang, Yi Zhou, Josh A. Taylor, Mahnoosh Alizadeh
**Year:** 2026
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

Optimized charging of electric vehicles (EVs) at public locations consists of two decisions: how much energy to deliver at what times, which is continuous, and where to plug in, which is binary. This makes optimizing EV charging a mixed-integer linear program (MILP). This discreteness undermines traditional marginal pricing methods. In this paper, we develop the first marginal-price-based mechanism for pricing EV charging with binary station access constraints. Using the result of Burer (2009), we express the EV charging as a completely positive program (CPP), whose dual is a copositive program (COP). This convex dual admits valid shadow prices even though the original allocation problem is discrete and nonconvex. By interpreting the COP dual variables as marginal prices, we construct a pricing mechanism that captures EV supply equipment (EVSE) congestion as well as charging-capacity limits. We prove that the resulting mechanism is revenue-adequate for the operator and individually rational for every EV user, in the strong sense that each user maximizes their own welfare by accepting their assigned charging plan rather than deviating to any alternative option. We further develop problem-specific inner-approximation and dimension-reduction techniques that substantially improve the computational tractability of solving the COP in our setting. Numerical experiments on both small and large scale charging instances demonstrate that our pricing mechanism captures discrete congestion effects and aligns user incentives with the system-optimal assignment, outperforming time-of-use (TOU) and convex relaxation benchmarks.
