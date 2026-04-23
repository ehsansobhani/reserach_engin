# Paper Summary: An Exact Solution Algorithm for the Bi-Level Optimization Problem of Electric Vehicles Charging Station Placement

**Key:** an_exact_2025
**Authors:** Mobina Nankali, Michael W. Levin
**Year:** 2025
**Venue:** arXiv
**Category:** spatial_optimization
**Date summarized:** 2026-04-23

## Metadata

- **arXiv ID:** 2511.19884v2
- **DOI:** 
- **URL:** https://arxiv.org/abs/2511.19884v2

## Abstract

This work addresses electric vehicle (EV) charging station placement through a bi-level optimization model, where the upper-level planner maximizes net revenue by selecting station locations under budget constraints, while EV users at the lower level choose routes and charging stations to minimize travel and charging costs. To account for range anxiety, we construct a battery-expanded network and apply a shortest path algorithm with Frank-Wolfe traffic assignment. Our primary contribution is developing the first exact solution algorithm for large scale EV charging station placement problems. We propose a Branch-and-Price-and-Cut algorithm enhanced with value function cuts and column generation. While existing research relies on heuristic methods that provide no optimality guarantees or exact algorithms that require prohibitively long runtimes, our exact algorithm delivers globally optimal solutions with mathematical certainty under a reasonable runtime. Computational experiments on the Eastern Massachusetts network (74 nodes, 248 links), the Anaheim network (416 nodes, 914 links), and the Barcelona network (110 zones, 1,020 nodes, and 2,512 links) demonstrate exceptional performance. Our algorithm terminates within minutes rather than hours, while achieving optimality gaps below 1% across all instances. This result represents a computational speedup of over two orders of magnitude compared to existing methods. The algorithm successfully handles problems with over 300,000 feasible combinations, which transform EV charging infrastructure planning from a computationally prohibitive problem into a tractable optimization task suitable for practical decision making problem for real world networks.

## Key Findings

<!-- Synthesize key findings from full text below -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Methodology

<!-- Characterize approach: optimization, simulation, empirical, mixed -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Spatial and Planning Dimensions

<!-- Note planning scale, spatial units, zoning considerations -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Equity and Utilization Treatment

<!-- Note how equity and utilization are defined and measured -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Limitations

<!-- Note limitations stated by authors or evident from analysis -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Relevance to Dissertation

<!-- State how this paper connects to the dissertation's five gaps -->

<!-- [TO BE COMPLETED BY AGENT] -->
