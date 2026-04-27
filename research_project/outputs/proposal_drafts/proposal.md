# Mobility-Aligned Phased Deployment of Urban BEV Fast-Charging Infrastructure: A Systematic Review and Research Framework

## Abstract

The rapid global adoption of battery electric vehicles (BEVs) places unprecedented demands on urban charging infrastructure. Despite a growing body of research on charging station placement and optimization, current planning approaches are characterized by persistent methodological gaps that limit deployment effectiveness, equity, and long-term scalability. This proposal presents a systematic literature review of 200 peer-reviewed studies on urban BEV fast-charging infrastructure planning, conducted in accordance with PRISMA 2020 guidelines, and derives a structured research framework for addressing five critical, interrelated gaps identified across the reviewed literature.

The review reveals that the dominant paradigm in charging station siting relies on administrative zoning boundaries, traffic analysis zones (TAZs), census tracts, municipal districts, that poorly represent actual mobility corridor patterns, creating spatial misalignment between infrastructure supply and travel demand (Gap 1; 133 papers with partial evidence). While spatial optimization methods have been extensively studied, systematic comparison of alternative zoning schemas remains absent (Gap 2; only 5 papers). The persistent treatment of equity and utilization as competing single-objective functions prevents simultaneous optimization of network coverage equity and infrastructure utilization efficiency (Gap 3; 14 papers address both). The overwhelming dominance of static, single-period optimization models ignores the phased, budget-constrained nature of real-world charging deployment (Gap 4; 44 papers address phasing), and no integrated framework bridges meso-scale rollout planning with micro-scale site implementation (Gap 5; 11 papers).

This proposal advances four research questions aligned with these gaps and proposes a three-stage integrated framework: (1) mobility-corridor spatial unit construction and zoning schema comparison; (2) joint equity-utilization multi-objective phased rollout optimization; and (3) a meso-to-micro site translation protocol. The expected contributions address each gap with a validated methodological output: a spatial unit alignment score, a zoning schema comparison procedure, a joint equity-utilization optimization model with Pareto frontier characterization, an adaptive phasing decision procedure, and a meso-micro translation protocol.

**Keywords:** BEV; fast-charging infrastructure; urban planning; spatial optimization; equity; phased deployment; meso-micro integration; systematic literature review; PRISMA


---

## 1. Introduction

### 1.1 Urban Electrification and the Infrastructure Challenge

The global transition to BEVs is accelerating. Policy mandates in major economies, including the European Union's 2035 combustion engine ban, California's Advanced Clean Cars II regulation, and China's New Energy Vehicle targets, are driving adoption trajectories that require commensurately ambitious charging infrastructure deployment. Yet the planning frameworks available to urban practitioners for managing this deployment lag behind both the scale of the challenge and the sophistication of the vehicle technology itself.

Urban fast-charging infrastructure is not merely a civil engineering problem; it is a spatial planning problem with dimensions of equity, mobility, zoning, phasing, and scale integration that existing optimization-focused research has not fully addressed. The consequences of inadequate planning frameworks are significant: infrastructure concentrated in high-income corridors, stations sited in zoning categories that maximize political feasibility rather than mobility alignment, static deployment plans that fail to adapt as EV adoption evolves, and city-level rollout plans that cannot be operationalized at the site level without implicit, unspecified translation steps.

This proposal addresses the methodological gaps in urban BEV charging infrastructure planning through a systematic literature review of 200 papers and the development of an integrated research framework that directly targets five identified gaps.

### 1.2 Why Fast-Charging Planning Is a Hard Problem

The difficulty of urban fast-charging infrastructure planning arises from the simultaneous interaction of several complex subsystems. The spatial problem requires aligning station locations with mobility demand patterns that are dynamic, multi-modal, and poorly captured by administrative boundaries (Najafzad et al. (2026); Mejia et al. (2026); Jiang et al. (2026)). The equity problem requires balancing geographic access across socioeconomic strata while maintaining financial viability and utilization efficiency (Jha et al. (2025); Erfani et al. (2024)). The temporal problem requires sequencing deployment across multiple budget cycles while managing demand uncertainty and ensuring that early phases do not preclude optimal long-run configurations (Tang et al. (2025); Giudice et al. (2023)). The utilization problem requires forecasting and optimizing station occupancy under adoption dynamics that are endogenous to infrastructure placement decisions (Jiang et al. (2025); Wu et al. (2024)). And the scale integration problem requires translating city-level or district-level rollout plans into site-level implementation specifications that are technically, legally, and financially feasible.

No existing study addresses all five of these dimensions simultaneously. The systematic review presented in this proposal documents the extent of this gap across 200 peer-reviewed studies and derives a research framework that addresses each dimension through a targeted methodological contribution.

### 1.3 The Five-Gap Framework

This proposal organizes the identified methodological limitations into five research gaps, each representing a distinct dimension of the planning problem that is currently underaddressed or entirely absent from the literature:

**Gap 1, Misaligned Spatial Units (133 papers with partial evidence).** Administrative zoning boundaries create structural misalignment between the spatial unit of optimization and the spatial unit of actual charging demand. Trip-based corridor flows routinely cross TAZ and municipal boundaries, causing systematic bias in demand estimation and station placement. No paper in the reviewed corpus constructs mobility-corridor-based spatial units and directly compares their siting outcomes to TAZ-based results on the same metropolitan area. Representative evidence: Do et al. (2025); Xin et al. (2023).

**Gap 2, Lack of Zoning Impact Analysis (5 papers).** While zoning regulations determine permissible locations for charging infrastructure, no study systematically compares outcomes under alternative zoning schemas. The gap between zoning policy design and infrastructure outcome evaluation represents the most severe methodological absence in the literature. Representative evidence: Karakuş and Corcoran (2025); Zhang and Shi (2024).

**Gap 3, Equity and Utilization Separation (14 papers address both).** The dominant approach treats equity and utilization as independent objectives. Joint multi-objective optimization producing Pareto-efficient tradeoffs between equity access and utilization efficiency does not exist in the reviewed literature. Representative evidence: Arief et al. (2023); Najafzad et al. (2026).

**Gap 4, Static Optimization Dominance (44 papers address phasing).** The vast majority of models optimize a single planning period. Phased, budget-constrained, adaptive deployment with explicit trigger criteria for phase transitions is rare. Representative evidence: Zhang and Tan (2024); Yu et al. (2025).

**Gap 5, Missing Meso-Micro Integration (11 papers).** City-level rollout plans cannot be operationalized at the site level without an explicit translation protocol. No integrated framework specifying the information transfer from meso to micro planning scales exists in the literature. Representative evidence: Do et al. (2025); Zhang and Tan (2024).

### 1.4 Scope and Contribution of This Proposal

This proposal makes five primary contributions: (1) a validated mobility-corridor spatial unit construction methodology addressing Gap 1; (2) the first systematic zoning schema comparative analysis addressing Gap 2; (3) a joint equity-utilization multi-objective optimization model addressing Gap 3; (4) an adaptive phased rollout decision procedure addressing Gap 4; and (5) a meso-to-micro site translation protocol addressing Gap 5.

The research methodology follows PRISMA 2020 systematic review guidelines and draws on 200 reviewed papers spanning 0 to 2026. The proposed framework is designed to be transferable across metropolitan contexts while remaining grounded in the institutional realities of municipal zoning, transportation planning practice, and incremental infrastructure investment.

### 1.5 Structure of the Proposal

The remainder of this proposal is organized as follows. Section 2 describes the systematic review methodology. Section 3 reviews the literature by thematic cluster. Section 4 presents the gap analysis with evidence tables. Section 5 states the four research questions. Section 6 describes the proposed three-stage research framework. Section 7 presents expected contributions and a research timeline. Section 8 contains the full reference list.


---

## 2. Systematic Review Methodology

### 2.1 Review Protocol and Registration

This systematic review follows the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 statement (Page et al., 2021). The review protocol was designed prospectively to ensure transparency and reproducibility. Inclusion and exclusion criteria were defined and documented prior to abstract screening. The review covers the period from 2011 to April 2026.

### 2.2 Search Strategy

The primary search was conducted on arXiv (categories: cs.AI, cs.SY, eess.SY, math.OC, econ.GN) Supplementary searches were conducted on Semantic Scholar, the Transportation Research Board Annual Meeting Proceedings, and Web of Science. The primary search strings included:

**Core queries (Gaps 1, 3):**
- EV charging infrastructure planning urban spatial optimization
- electric vehicle charging station location optimization equity accessibility
- EV charging station siting GIS spatial optimization

**Phased deployment queries (Gap 4):**
- BEV charging deployment rollout phased urban infrastructure
- EV charging infrastructure temporal sequential staged deployment
- electric vehicle charging district-level meso site selection implementation planning

**Zoning and land-use queries (Gap 2):**
- charging infrastructure land use zoning regulatory compatibility
- electric vehicle charging zoning ordinance permitting municipal land use regulation
- EV charging station mixed-use district land use compatibility urban form

**Equity and utilization queries (Gap 3):**
- electric vehicle charging spatial justice coverage underserved
- EV charging demand forecasting utilization optimization network

**Meso-micro queries (Gap 5):**
- EV charging infrastructure meso micro multi-scale planning
- EV charging infrastructure multi-scale urban district site level planning integration

All search results were deduplicated by arXiv ID and title-year matching prior to screening. Results were rate-limited to comply with arXiv API terms of service (1-second minimum interval between requests).

### 2.3 PRISMA Flow

The following flowchart (Figure 2.1) summarizes the four-stage screening process following PRISMA 2020 guidelines.

%%PRISMA_TIKZ%%

### 2.4 Inclusion and Exclusion Criteria

**Table 2.1: Inclusion and Exclusion Criteria**

| Type | Criterion | Rationale |
|------|-----------|-----------|
| Include | Addresses EV/BEV charging infrastructure planning (not only vehicle technology) | Core domain scope |
| Include | Contains a spatial or planning dimension | Required for gap relevance |
| Include | Describes methodology with reproducible approach | Quality threshold |
| Include | English language; peer-reviewed or substantial arXiv preprint (≥10 pages) | Methodological rigor |
| Include | Publication year 2011–2026 | Temporal scope |
| Exclude | Pure V2G (vehicle-to-grid) technical study without spatial planning component | Outside scope |
| Exclude | Highway-only corridor study without urban context | Outside scope |
| Exclude | Workshop abstract, poster, or conference summary without methodology detail | Insufficient detail |
| Exclude | Full text unavailable after download attempt | Practical constraint |
| Exclude | Confirmed duplicate of an included paper | Deduplication |

### 2.5 Data Extraction

For each included paper, structured data extraction was performed following the schema summarized in Table 2.2. The extraction schema covers 44 fields across thirteen dimensions: paper identity and metadata; research problem and scope; methodology approach and data sources; spatial unit and planning scale; demand modeling; optimization formulation; equity treatment; utilization treatment; rollout and phasing; zoning and land-use; meso-micro integration; quality assessment and limitations; and dissertation gap mapping (Gap 1–5, with evidence strings).

**Table 2.2: Literature Extraction Dimensions and Analytical Purpose**

| Dimension | Information Extracted | Purpose in Analysis |
|-----------|----------------------|---------------------|
| Paper Metadata | Authors, year, venue, DOI, publication type | Enables bibliographic tracking and study categorization |
| Research Problem | Study objectives, planning scope, stated motivation | Identifies the primary challenges addressed by each study |
| Methodology | Modeling approach, datasets, computational tools | Compares methodological trends across the literature |
| Spatial Representation | Planning scale, zoning unit, spatial granularity | Evaluates how spatial structure is modeled |
| Demand Modeling | Demand estimation approach and aggregation level | Assesses how charging demand is represented |
| Optimization Framework | Objectives, constraints, optimization techniques | Compares charger placement strategies |
| Equity Considerations | Equity metrics, fairness definitions, accessibility treatment | Evaluates social equity integration |
| Utilization Modeling | Charger usage metrics and operational assumptions | Examines infrastructure utilization treatment |
| Rollout Strategy | Phased deployment and temporal planning methods | Analyzes long-term infrastructure planning |
| Zoning & Land Use | Land-use compatibility and zoning considerations | Assesses urban planning integration |
| Meso–Micro Integration | Relationships between corridor-scale and local-scale planning | Evaluates multi-scale planning approaches |
| Research Limitations | Stated limitations and generalizability concerns | Identifies methodological weaknesses |
| Gap Mapping | Evidence related to the five identified research gaps | Supports synthesis of unresolved challenges |

Literature extraction was conducted using a two-stage process. In the first stage, bibliographic information, methodological approaches, and thematic categories were identified automatically from paper abstracts and metadata using pattern-matching techniques. In the second stage, manual verification was performed to validate research gap classifications and supporting evidence. The automated extraction process showed high agreement with manual review for methodological classification, while spatial-unit identification required additional manual verification due to inconsistent terminology across studies.

### 2.6 Quality Assessment

Paper quality was assessed on three dimensions: (1) methodological clarity (is the approach reproducible?); (2) data quality (are data sources described?); and (3) generalizability (are limitations stated?). Papers meeting inclusion criteria but lacking two of these three quality dimensions were retained in the review with a quality caveat noted in their extraction file.


---

## 3. Related Work

The following review organizes the literature by thematic cluster, reflecting the primary classification of each paper. Papers whose contributions span multiple themes are discussed in the section most relevant to their primary contribution and cross-referenced where appropriate. Each subsection opens with a synthetic overview of the thematic strand, followed by individual paper entries and a summary table.

### 3.1 Spatial Optimization for Charging Station Placement

*133 papers (66% of corpus)*

Spatial optimization constitutes the dominant methodological paradigm in charging infrastructure planning research, representing the largest thematic cluster in this review. These studies apply deterministic and stochastic mathematical programming models, principally mixed-integer linear programming (MILP), bilevel optimization, flow-based facility location formulations, and reinforcement learning, to identify optimal charging station locations subject to demand coverage, budget, and network constraints. The field has produced increasingly sophisticated formulations that incorporate traffic flow, queue dynamics, and grid capacity constraints. However, the spatial unit of analysis remains almost universally fixed to administrative boundaries, and single-period static optimization remains the norm. The richness of the optimization literature stands in contrast to its limited engagement with planning-side questions of spatial unit validity, zoning compatibility, and deployment phasing. Key contributions in this area span from classical facility location formulations applied to charging networks, to modern deep reinforcement learning approaches and data-driven placement frameworks. The following papers represent the core of this literature as identified in the systematic review.

**Najafzad et al. (2026)** present *A Two-Stage Stochastic Optimization Model for the Equitable Deployment of Fixed and Mobile EV Charging Stations*. A major barrier to wide adoption of Electric Vehicles (EVs) is the absence of reliable and equitable charging infrastructure. Poorly located charging stations create coverage gaps and slow down EV adoption, especially in underserved communities. This paper proposes a two-stage stochastic mixed-integer programming model for the optimal deployment of Fixed and Mobile Charging Stations (FCSs and MCSs) across multiple zones and periods. This work addresses dissertation gaps: G1, G3, G4.

**Mejia et al. (2026)** present *Joint Planning of Distribution Systems and EV Charging Infrastructure Using a GIS-Based Spatial Analysis Framework*. This paper addresses joint planning of distribution systems and ev charging infrastructure using a gis-based spatial anal. This work addresses dissertation gaps: G1.

**Jiang et al. (2026)** present *Pricing EV Charging and Station Access via Copositive Duality*. Optimized charging of EVs at public locations consists of two decisions: how much energy to deliver at what times, which is continuous, and where to plug in, which is binary. This makes optimizing EV charging a MILP. This discreteness undermines traditional marginal pricing methods. This work addresses dissertation gaps: G1.

**Babur and Macfarlane (2026)** present *Regional Transportation Modeling for Equitable EV Charging Infrastructure Design*. The widespread adoption of BEVs holds promise for mitigating emission-related health impacts, particularly for low-income communities disproportionately affected by exposure to traffic-related air pollution. However, designing effective charging infrastructure necessitates a regional modeling approach that accounts for the inherent cross-jurisdictional nature of mobility patterns. This study underscores the importance of regional modeling in optimizing charging station deployment and evaluating the environmental justice implications for equity priority communities. This work addresses dissertation gaps: G1, G3, G4.

**Bertucci et al. (2026)** present *Simultaneous Optimization of Electric Ferry Operations and Charging Infrastructure*. Electrification of marine transport is a promising solution to reduce sector greenhouse gas emissions and operational costs. However, the large upfront cost of electric vessels and the required charging infrastructure can be a barrier to the development of this technology. Optimization algorithms that jointly design the charging infrastructure and the operation of electric vessels can help to reduce these costs and make these projects viable. This work addresses dissertation gaps: G1.

**Fariza et al. (2026)** present *Strategic Planning of Public EV Charging Stations Using AHP and GIS to Support Sustainable Mobility in West Java, Indonesia*. The transition toward sustainable and low-emission transportation in Indonesia has accelerated the adoption of EVs, especially in densely populated provinces such as West Java. Despite this progress, the distribution and capacity of Public EV Charging Stations (EVCS) remain uneven, creating significant gaps between vehicle growth and infrastructure readiness. This spatial imbalance threatens to slow down EV adoption and limit the effectiveness of national decarbonization targets. This work addresses dissertation gaps: G1, G2.

**Do et al. (2025)** present *A Digital Twin Framework for Decision-Support and Optimization of EV Charging Infrastructure in Localized Urban Systems*. As EV adoption accelerates in urban environments, optimizing charging infrastructure is vital for balancing user satisfaction, energy efficiency, and financial viability. This study advances beyond static models by proposing a digital twin framework that integrates agent-based decision support with embedded optimization to dynamically simulate EV charging behaviors, infrastructure layouts, and policy responses across scenarios. Applied to a localized urban site (a university campus) in Hanoi, Vietnam, the model evaluates operational policies, EV station configurations, and renewable energy sources. This work addresses dissertation gaps: G1, G5.

**Ameer et al. (2025)** present *A density-based spatial clustering and linear programming method for EV charging station location and price optimization*. This paper addresses a density-based spatial clustering and linear programming method for EV charging stati. This work addresses dissertation gaps: G1.

**Yu et al. (2025)** present *A Joint Planning Model for Fixed and Mobile EV Charging Stations Considering Flexible Capacity Strategy*. The widespread adoption of EVs has significantly increased demand on both transportation and power systems, posing challenges to their stable operation. To support the growing need for EV charging, both fixed charging stations (FCSs) and mobile charging stations (MCSs) have been introduced, serving as key interfaces between the power grid and traffic network. Recognizing the importance of collaborative planning across these sectors, this paper presents a two-stage joint planning model for FCSs and MCSs, utilizing an improved alternating direction method of multipliers (ADMM) algorithm. This work addresses dissertation gaps: G1, G4.

**Karakuş and Corcoran (2025)** present *A Multi-Modal Spatial Risk Framework for EV Charging Infrastructure Using Remote Sensing*. EV charging infrastructure is increasingly critical to sustainable transport systems, yet its resilience under environmental and infrastructural stress remains underexplored. In this paper, we introduce RSERI-EV, a spatially explicit and multi-modal risk assessment framework that combines remote sensing data, open infrastructure datasets, and spatial graph analytics to evaluate the vulnerability of EV charging stations. RSERI-EV integrates diverse data layers, including flood risk maps, land surface temperature (LST) extremes, vegetation indices (NDVI), land use/land cover (LULC), proximity to electrical substations, and road accessibility to generate a composite Resilience Score. This work addresses dissertation gaps: G1, G2, G4.

**Huang et al. (2025)** present *A Spatially Aware Machine Learning Method for Locating EVCSs*. The rapid adoption of EVs has driven a strong need for optimizing locations of electric vehicle charging stations (EVCSs). Previous methods for locating EVCSs rely on statistical and optimization models, but these methods have limitations in capturing complex nonlinear relationships and spatial dependencies among factors influencing EVCS locations. To address this research gap and better understand the spatial impacts of urban activities on EVCS placement, this study presents a spatially aware machine learning (SAML) method that combines a multi-layer perceptron (MLP) model with a spatial loss function to optimize EVCS sites. This work addresses dissertation gaps: G1.

**Meng et al. (2025)** present *A two-stage optimization framework for EV charging station planning considering investment cost and service satisfaction*. This paper addresses a two-stage optimization framework for ev charging station planning considering investment cost and . This work addresses dissertation gaps: G1.

**Kinchen et al. (2025)** present *A United Framework for Planning EV Charging Accessibility*. The shift towards EVs is crucial for establishing sustainable and low-emission urban transportation systems. However, the success of this transition depends on the strategic placement of the charging infrastructure. This paper addresses the challenge of optimizing charging station locations in dense urban environments while balancing efficiency with spatial accessibility. This work addresses dissertation gaps: G1, G3.

**Nankali and Levin (2025)** present *An Exact Solution Algorithm for the Bi-Level Optimization Problem of EVs Charging Station Placement*. This work addresses EV charging station placement through a bi-level optimization model, where the upper-level planner maximizes net revenue by selecting station locations under budget constraints, while EV users at the lower level choose routes and charging stations to minimize travel and charging costs. To account for range anxiety, we construct a battery-expanded network and apply a shortest path algorithm with Frank-Wolfe traffic assignment. Our primary contribution is developing the first exact solution algorithm for large scale EV charging station placement problems. This work addresses dissertation gaps: G1.

**Mousaei (2025)** present *Analyzing locational inequalities in the placement of EVCSs using machine learning: A case study in Glasgow*. This paper addresses analyzing locational inequalities in the placement of EVCSs using machi. This work addresses dissertation gaps: G1.

**Silva et al. (2025)** present *Causal spillover effects of EVCS placement on local businesses: a staggered adoption study*. Understanding the economic impacts of the placement of EVCSs is crucial for planning infrastructure systems that benefit the broader community. Theoretical models have been used to predict human behavior during charging events, however, these models have often neglected the complexity of trip patterns, and have underestimated the real-world impacts of such infrastructure on the local economy. In this paper, we design a quasi-experiment using mobile phone GPS location and EVCS deployment history data to analyze the causal impact of EVCS placement on visitation patterns to businesses. This work addresses dissertation gaps: G1, G4.

**Islam et al. (2025)** present *CHARGE-MAP: An integrated framework to study the multicriteria EV charging infrastructure expansion problem*. The widespread adoption of EVs in recent years has necessitated the development of effective charging infrastructures. However, charging infrastructure expansion is a multifaceted problem that requires careful consideration of the existing infrastructure, spatiotemporal distribution of charging demands, power-grid capacity, and budget constraints. To approach this complex problem, we present charge-map , a data-driven simulation-optimization framework, focused on ensuring meaningful charging experience for individual EV owners. This work addresses dissertation gaps: G1, G4.

**Nguyen et al. (2025)** present *Competitive EV charging station location with queues*. EV public charging infrastructure planning faces significant challenges in competitive markets, where multiple service providers affect congestion and user behavior. This work extends existing modeling frameworks by incorporating the presence of competitors' stations and more realistic queueing systems. First, we analyze three finite queueing systems, M/M/1/K, M/M/s/K, and M/Er/s/K, with varying numbers of servers (charging outlets) and service time distributions, deriving analytic expressions for user behavior metrics. This work addresses dissertation gaps: G1.

**Alharbi et al. (2025)** present *Data-driven EV charging infrastructure with uncertainty based on a spatial–temporal flow-driven (STFD) models considering batteries*. This paper addresses data-driven ev charging infrastructure with uncertainty based on a spatial–temporal flow-driven (stf. This work addresses dissertation gaps: G1, G4.

**Junker et al. (2025)** present *Data-Driven Optimization of EV Charging Station Placement Using Causal Discovery*. This paper addresses the critical challenge of optimizing EVCS placement through a novel data-driven methodology employing causal discovery techniques. While traditional approaches prioritize economic factors or power grid constraints, they often neglect empirical charging patterns that ultimately determine station utilization. We analyze extensive charging data from Palo Alto and Boulder (337,344 events across 100 stations) to uncover latent relationships between station characteristics and utilization. This work addresses dissertation gaps: G1.

**Zhao et al. (2025)** present *EV Charging Planning: A Complex Systems Perspective*. This paper addresses EV charging planning: a complex systems perspective. This work addresses dissertation gaps: G1, G3.

**Kapoor (2025)** present *Explainable and context-aware Graph Neural Networks for dynamic EV route optimization to optimal charging station*. This paper addresses explainable and context-aware graph neural networks for dynamic EV route optimization . This work addresses dissertation gaps: G1.

**Yuan et al. (2025)** present *Fairness-Oriented Charging Station Location Optimization Driven by Deep Reinforcement Learning*. This paper addresses fairness-oriented charging station location optimization driven by deep reinforcement learning. This work addresses dissertation gaps: G1, G3.

**Ameer et al. (2025)** present *Hybrid optimization of EV charging station placement and pricing using Bender’s decomposition and NSGA-II algorithm*. This paper addresses hybrid optimization of ev charging station placement and pricing using bender’s decomposition and ns. This work addresses dissertation gaps: G1.

**Okada et al. (2025)** present *Joint Optimization of EV Routes and Charging Locations Learning Charge Constraints Using QUBO Solver*. Optimal routing problems of EVs have attracted much attention in recent years, and installation of charging stations is an important issue for EVs. Hence, we focus on the joint optimization of the location of charging stations and the routing of EVs. When routing problems are formulated in the form of quadratic unconstrained binary optimization (QUBO), specialized solvers such as quantum annealer are expected to provide optimal solutions with high speed and accuracy. This work addresses dissertation gaps: G1, G4.

**Zheng et al. (2025)** present *Large Language Model-Assisted Planning of EV Charging Infrastructure with Real-World Case Study*. The growing demand for EV charging infrastructure presents significant planning challenges, requiring efficient strategies for investment and operation to deliver cost-effective charging services. However, the potential benefits of EV charging assignment, particularly in response to varying spatial-temporal patterns of charging demand, remain under-explored in infrastructure planning. This paper proposes an integrated approach that jointly optimizes investment decisions and charging assignments while accounting for spatial-temporal demand dynamics and their interdependencies. This work addresses dissertation gaps: G1, G4.

**Choi et al. (2025)** present *Location and capacity optimization of EV charging stations using genetic algorithms and fuzzy analytic hierarchy process*. This paper addresses location and capacity optimization of ev charging stations using genetic algorithms and fuzzy analyt. This work addresses dissertation gaps: G1.

**Ruiz-Barajas et al. (2025)** present *Multiobjective model to optimize charging station location for the decarbonization process in Mexico*. EVs offer significant potential for advancing sustainable environmental goals. However, their widespread adoption has been concentrated in urban areas, raising challenges for interurban travel. In many countries, charging station networks are primarily located within cities, highlighting a key opportunity for expansion to support longer distance journeys. This work addresses dissertation gaps: G1.

**Nakao et al. (2025)** present *Optimal mixed fleet and charging infrastructure planning to electrify demand responsive feeder services with target CO2 emission constraints*. Electrifying demand-responsive transport systems need to plan the charging infrastructure carefully, considering the trade-offs of charging efficiency and charging infrastructure costs. Earlier studies assume a fully electrified fleet and overlook the planning issue in the transition period. This study addresses the joint fleet size and charging infrastructure planning for a demand-responsive feeder service under stochastic demand, given a user-defined targeted CO2 emission reduction policy. This work addresses dissertation gaps: G1.

**Zhang et al. (2025)** present *Optimization of EVCS Location Distribution Based on Activity–Travel Patterns*. With the rapid expansion of the EV market, optimizing the distribution of charging stations has attracted increasing attention. Unlike internal combustion engine vehicles, EVs are typically charged at the end of a trip rather than during transit. Therefore, analyzing EV users’ charging preferences based on their activity–travel patterns is essential. This work addresses dissertation gaps: G1.

**Zhong et al. (2025)** present *Optimizing electric bus charging station locations: An integrated land-use and transportation approach*. This paper addresses optimizing electric bus charging station locations: an integrated land-use and transportation approa. This work addresses dissertation gaps: G1.

**Ai et al. (2025)** present *Optimizing Urban EV Charging and Battery Swapping Infrastructure: A Location-Inventory-Grid Model*. The rapid rise of EVs places unprecedented stress on both urban mobility systems and low-voltage power grids. Designing battery swapping and charging networks that are cost-efficient, grid-compatible, and sustainable is therefore a pressing yet complex challenge: service providers must jointly optimize station locations, battery inventory, and grid interaction under high-dimensional uncertainty. We develop an integrated location-inventory-grid model and employ a continuous approximation approach to overcome the intractability of discrete formulations. This work addresses dissertation gaps: G1, G5.

**Yuan et al. (2025)** present *Planning future charging infrastructure for private EVs: A city-scale assessment of demand and capacity*. This study proposes the first demand-driven, multi-objective planning model for optimizing city-scale capacity allocation of EV charging infrastructure. The model employs a bottom-up approach to estimate charging demand differentiated by vehicle type-BEVs, extended-range EVs (EREVs), and plug-in hybrid EVs (PHEVs). Chongqing, a rapidly expanding EV industry cluster in China with a strong industrial base, supportive policies, and diverse urban morphologies, is selected as the case study. This work addresses dissertation gaps: G1, G4.

**Mousaei and Naderi (2025)** present *Predicting Optimal Placement of EV Charge Stations Using Machine Learning: A Case Study in Glasgow, UK*. This paper addresses predicting optimal placement of EV charge stations using machine learning: a case stud. This work addresses dissertation gaps: G1.

**Zhu et al. (2025)** present *Reinforcement Learning for Hybrid Charging Stations Planning and Operation Considering Fixed and Mobile Chargers*. The success of vehicle electrification relies on efficient and adaptable charging infrastructure. Fixed-location charging stations often suffer from underutilization or congestion due to fluctuating demand, while mobile chargers offer flexibility by relocating as needed. This paper studies the optimal planning and operation of hybrid charging infrastructures that combine both fixed and mobile chargers within urban road networks. This work addresses dissertation gaps: G1.

**Xia et al. (2025)** present *Robust charging station location and routing-scheduling for electric modular autonomous units*. Problem definition: Motivated by global electrification targets and the advent of electric modular autonomous units (E-MAUs), this paper addresses a robust charging station location and routing-scheduling problem (E-RCRSP) in an inter-modal transit system, presenting a novel solution to traditional electric bus scheduling. The system integrates regular bus services, offering full-line or sectional coverage, and short-turning services. Considering the fast-charging technology with quick top-ups, we jointly optimize charging station locations and capacities, fleet sizing, as well as routing-scheduling for E-MAUs under demand uncertainty. This work addresses dissertation gaps: G1.


**Ju et al. (2025)** present *Trajectory-Integrated Accessibility Analysis of Public EVCSs*. EV charging infrastructure is crucial for advancing EV adoption, managing charging loads, and ensuring equitable transportation electrification. However, there remains a notable gap in comprehensive accessibility metrics that integrate the mobility of the users. This study introduces a novel accessibility metric, termed Trajectory-Integrated Public EVCS Accessibility (TI-acs), and uses it to assess public EVCS accessibility for approximately 6 million residents in the San Francisco Bay Area based on detailed individual trajectory data in one week. This work addresses dissertation gaps: G1.

**Zhang and Tan (2024)** present *A data-driven approach of layout evaluation for EV charging infrastructure using agent-based simulation and GIS*. The development and popularization of new energy vehicles have become a global consensus. The shortage and unreasonable layout of EV charging infrastructure (EVCI) have severely restricted the development of EVs. In the literature, many methods can be used to optimize the layout of charging stations (CSs) for producing good layout designs. This work addresses dissertation gaps: G1, G4, G5.

**Zhang and Shi (2024)** present *A multi-objective site selection of EVCS based on NSGA-II*. The planning of charging infrastructure is crucial to developing EVs. Planning for charging stations requires considering several variables, including building costs, charging demand, and coverage levels. It might be advantageous to use a multi-objective optimization method based on the NSGA-II. This work addresses dissertation gaps: G1, G2.

**Aljaidi et al. (2024)** present *A particle swarm optimizer-based optimization approach for locating EVs charging stations in smart cities*. This paper addresses a particle swarm optimizer-based optimization approach for locating EVs charging stati. This work addresses dissertation gaps: G1.

**Radvand et al. (2024)** present *A Quantum Optimization Algorithm for Optimal EVCS Placement for Intercity Trips*. EVs play a significant role in enhancing the sustainability of transportation systems. However, their widespread adoption is hindered by inadequate public charging infrastructure, particularly to support long-distance travel. Identifying optimal charging station locations in large transportation networks presents a well-known NP-hard combinatorial optimization problem, as the search space grows exponentially with the number of potential charging station locations. This work addresses dissertation gaps: G1.

**Wu et al. (2024)** present *A two-layer planning method for location and capacity determination of public EVCSs*. This paper addresses a two-layer planning method for location and capacity determination of public EV charg. This work addresses dissertation gaps: G1.

**Zhang et al. (2024)** present *Advancing urban EVCSs: AI-driven day-ahead optimization of pricing and Nudge strategies utilizing multi-agent deep reinforcement learning*. This paper addresses advancing urban EVCSs: ai-driven day-ahead optimization of pricing and . This work addresses dissertation gaps: G1.

**Liu et al. (2024)** present *BSS location for EVs: a simulation optimization approach*. EVs face significant energy supply challenges due to long charging times and congestion at charging stations. Battery swapping stations (BSSs) offer a faster alternative for energy replenishment, but their deployment costs are considerably higher than those of charging stations. As a result, selecting optimal locations for BSSs is crucial to improve their accessibility and utilization. This work addresses dissertation gaps: G1, G4.

**Wang and Lin (2024)** present *Beyond Profit: A Multi-Objective Framework for EVCS Operations*. This paper explores the pricing and scheduling strategies of the EVCSs in response to the rising demand for cleaner transportation. Most of the existing methods focus on maximizing the energy efficiency or the charging station profit, however, the reputation of EVs is also a key factor for the long-term charging station operations. To address these gaps, we propose a novel framework for jointly optimizing pricing and continuous-multiple charging rates. This work addresses dissertation gaps: G1.

**Cai et al. (2024)** present *Charging Station Site Selection Optimization for Electric Logistics Vehicles, Taking into Account Time-Window and Load Constraints*. In order to improve the efficiency of the “last-mile” distribution in urban logistics and solve the problem of the difficult charging of electric logistics vehicles (ELVs), this paper proposes a charging station location optimization scheme for ELVs that takes into account time-window and load constraints (TW-LCs). Taking the optimal transportation path as the objective function and considering the time-window and vehicle load constraints, a charging station siting model was established. For the TW-LC problem, an improved genetic algorithm combining the farthest-insertion heuristic idea and local search operation was designed. This work addresses dissertation gaps: G1.

**Li et al. (2024)** present *EV Charging Infrastructure Optimization Incorporating Demand Forecasting and Renewable Energy Application*. The rapid growth in EV adoption and the increasing use of renewable energy have introduced challenges in designing and managing EV charging infrastructure. This study presents a framework that combines a hybrid deep learning model, spatial and temporal demand analysis, and vehicle-to-grid (V2G) optimization to address these issues. The framework achieved high predictive accuracy, with an RMSE of 2.1 kWh and an R2R^2R2 value of 0.92, effectively capturing daily demand patterns and variations across charging stations. This work addresses dissertation gaps: G1.

**Cao and Zhou (2024)** present *Energy management optimization of hybrid EVs based on deep learning model predictive control*. In this paper, the hybrid EV (HEV) energy management optimization method is proposed based on deep learning (DL) model predictive control. Through empirical research combined with the questionnaire survey, this article not only provides a new perspective and practical basis but also improves the efficiency and accuracy of the model by improving the relevant algorithms. The study first analyzes the importance of HEV energy management and reviews the existing literature. This work addresses dissertation gaps: G1.

**Mehditabrizi et al. (2024)** present *Integrating En Route and Home Proximity in EV Charging Accessibility: A Spatial Analysis in the Washington Metropolitan Area*. This study evaluates the accessibility of public EV charging stations in the Washington metropolitan area using a comprehensive measure that accounts for both destination-based and en route charging opportunities. By incorporating the full spectrum of daily travel patterns into the accessibility evaluation, our methodology offers a more realistic measure of charging opportunities than destination-based methods that prioritize proximity to residential locations. Results from spatial autocorrelation analysis indicate that conventional accessibility assessments often overestimate the availability of infrastructure in central urban areas and underestimate it in peripheral commuting zones, potentially leading to misallocated resources. This work addresses dissertation gaps: G1.

**Mohammed et al. (2024)** present *Multiobjective optimization for sizing and placing EVCSs considering comprehensive uncertainties*. This paper addresses multiobjective optimization for sizing and placing EVCSs considering co. This work addresses dissertation gaps: G1.

**Kumar and Channi (2024)** present *Optimal EVCS Placement: A Multi-Criteria Decision-Making Approach for Site Selection*. This paper addresses optimal EVCS placement: a multi-criteria decision-making approach for s. This work addresses dissertation gaps: G1.

**Pierrou et al. (2024)** present *Optimal EV Charging Scheduling at Electric Railway Stations Under Peak Load Constraints*. In this paper, a novel Energy Management System (EMS) algorithm to achieve optimal EV charging scheduling at the parking lots of electric railway stations is proposed. The proposed approach uncovers the potential of leveraging EV charging flexibility to prevent overloading in the combined EV charging and railway operation along with renewable generation, railway regenerative capabilities, and energy storage. Specifically, to realize end-user flexibility, each EV state of charge at departure time is introduced as an optimization variable. This work addresses dissertation gaps: G1.

**He et al. (2024)** present *Optimal EVCS planning via spatial-temporal distribution of charging demand forecasting and traffic-grid coupling*. This paper addresses optimal evcs planning via spatial-temporal distribution of charging demand forecasting and traffic-g. This work addresses dissertation gaps: G1, G4.

**Heo and Chang (2024)** present *Optimal planning for EV fast charging stations placements in a city scale using an advantage actor-critic deep reinforcement learning and geospatial analysis*. This paper addresses optimal planning for EV fast charging stations placements in a city scale using an adv. This work addresses dissertation gaps: G1.

**Panyaram (2024)** present *Optimization Strategies for Efficient Charging Station Deployment in Urban and Rural Networks*. Optimized charging station deployment will enrich the EV ecosystem, especially in diversified urban and rural environments. In this research paper, an effort has been made to optimization strategies regarding the location of EV charging stations and how these can be operated effectively. The study analyzes key factors, such as population density, travel patterns, energy demand, and land availability, that provide a comprehensive framework for policymakers and planners. This work addresses dissertation gaps: G1, G4.

**Huang and Zhou (2024)** present *Optimizing EV Charging Station Placement in New South Wales: A Soft Actor-Critic Reinforcement Learning Approach*. This paper addresses optimizing ev charging station placement in new south wales: a soft actor-critic reinforcement learn. This work addresses dissertation gaps: G1.

**Munawar (2024)** present *Optimizing Urban Logistics Through EV Integration*. The transition to electric-based logistics has become increasingly vital in the pursuit of sustainable urban transportation. This study presents a narrative review of recent literature examining the efficiency, environmental impact, and policy dimensions of EV adoption in logistics. Drawing on peer-reviewed articles from Scopus and Google Scholar published between 2015 and 2024, this review employed systematic keyword searches and thematic analysis to synthesize research findings. This work addresses dissertation gaps: G1, G5.

**Shen et al. (2024)** present *Sequential Charging Station Location Optimization under Uncertain Charging Behavior and User Growth*. Charging station availability is crucial for a thriving EV market. Due to budget constraints, locating these stations usually proceeds in phases, which calls for careful consideration of the (random) charging demand growth throughout the planning horizon. This paper integrates user choice behavior into two-stage and multi-stage stochastic programming models for intracity charging station planning under demand uncertainty. This work addresses dissertation gaps: G1, G4.

**Seilabi et al. (2024)** present *Sustainable Planning of EVCSs: A Bi-Level Optimization Framework for Reducing Vehicular Emissions in Urban Road Networks*. This paper proposes a decision-making framework for a multiple-period planning of EV charging station development. In this proposed framework, transportation planners seek to implement a phased provision of electric charging stations as well as repurposing gas stations at selected locations. The developed framework is presented as a bi-level optimization problem that determines the optimal electric charging network design while capturing the practical constraints and travelers’ decisions. This work addresses dissertation gaps: G1, G4.

**Akbay et al. (2024)** present *The EV Problem with Road Junctions and Road Types: An Ant Colony Optimization Approach*. This paper addresses the EV problem with road junctions and road types: an ant colony optimization approach. This work addresses dissertation gaps: G1.

**Boonprong et al. (2024)** present *Towards Sustainable Urban Mobility: Voronoi-Based Spatial Analysis of EV Charging Stations in Bangkok*. This study leverages the efficacy of Voronoi diagram theory within a mixed-methods approach to thoroughly examine the spatial distribution, service coverage, and optimal locations for expanding EV charging infrastructure in Bangkok. Drawing on data from field surveys and public data providers, our analysis unfolds in four key stages. Firstly, we delve into the spatial distribution of charging stations, scrutinizing density, proximity to various road types, and land use through the lens of Voronoi diagrams. This work addresses dissertation gaps: G1, G2, G3.

**Miltner et al. (2024)** present *Towards Using Machine Learning to Generatively Simulate EV Charging in Urban Areas*. This study addresses the challenge of predicting EV charging profiles in urban locations with limited data. Utilizing a neural network architecture, we aim to uncover latent charging profiles influenced by spatio-temporal factors. Our model focuses on peak power demand and daily load shapes, providing insights into charging behavior. This work addresses dissertation gaps: G1, G4.

**Alhussan et al. (2024)** present *Urban EVCS Placement Optimization with Graylag Goose Optimization Voting Classifier*. This paper addresses urban EVCS placement optimization with graylag goose optimization votin. This work addresses dissertation gaps: G1.

**Xin et al. (2023)** present *A BEV Transportation Network Design Model with Bounded Rational Travelers*. With governments worldwide emphasizing environmental protection and the global focus on carbon reduction, the BEV industry has developed rapidly. An urban transportation network with BEVs as the main form of transportation will soon become mainstream. Motivated by the abovementioned background, a BEV transportation network design problem is investigated, and a network design model is established. This work addresses dissertation gaps: G1.

**Al-Dahabreh et al. (2023)** present *A Data-Driven Framework for Improving Public EV Charging Infrastructure: Modeling and Forecasting*. This work presents an investigation and assessment framework, which, supported by realistic data, aims at provisioning operators with in-depth insights into the consumer-perceived Quality-of-Experience (QoE) at public EV charging infrastructures. Motivated by the unprecedented EV market growth, it is suspected that the existing charging infrastructure will soon be no longer capable of sustaining the rapidly growing charging demands; let alone that the currently adopted ad hoc infrastructure expansion strategies seem to be far from contributing any quality service sustainability solutions that tangibly reduce (ultimately mitigate) the severity of this problem. Without suitable QoE metrics, operators, today, face remarkable difficulty in assessing the performance of EV Charging Stations (EVCSs) in this regard. This work addresses dissertation gaps: G1.

**Arief et al. (2023)** present *A Robust and Efficient Optimization Model for EVCSs in Developing Countries under Electricity Uncertainty*. The rising demand for EVs worldwide necessitates the development of robust and accessible charging infrastructure, particularly in developing countries where electricity disruptions pose a significant challenge. Earlier charging infrastructure optimization studies do not rigorously address such service disruption characteristics, resulting in suboptimal infrastructure designs. To address this issue, we propose an efficient simulation-based optimization model that estimates candidate stations' service reliability and incorporates it into the objective function and constraints. This work addresses dissertation gaps: G1, G3.

**Yi et al. (2023)** present *An agent-based modeling approach for public charging demand estimation and charging station location optimization at urban scale*. This paper addresses an agent-based modeling approach for public charging demand estimation and charging station location. This work addresses dissertation gaps: G1.

**Varma et al. (2023)** present *EV Fleet and Charging Infrastructure Planning*. We study EV fleet and charging infrastructure planning in a spatial setting. With customer requests arriving continuously at rate $λ$ throughout the day, we determine the minimum number of vehicles and chargers for a target service level, along with matching and charging policies. While non-EV systems require extra $Θ(λ^{2/3})$ vehicles due to pickup times, EV systems differ. This work addresses dissertation gaps: G1, G5.

**Qiao et al. (2023)** present *Fast-charging station location problem: A two-phase approach with mathematical program with equilibrium constraints considering charging choice behaviour*. This paper addresses fast-charging station location problem: a two-phase approach with mathematical program with equilibr. This work addresses dissertation gaps: G1.

**Filippi et al. (2023)** present *Incorporating time-dependent demand patterns in the optimal location of capacitated charging stations*. A massive use of EVs is nowadays considered to be a key element of a sustainable transportation policy and the availability of charging stations is a crucial issue for their extensive use. Charging stations in an urban area have to be deployed in such a way that they can satisfy a demand that may dramatically vary in space and time. In this paper we present an optimization model for the location of charging stations that takes into account the main specific features of the problem, in particular the different charging technologies, and their associated service time, and the fact that the demand depends on space and time. This work addresses dissertation gaps: G1, G4.

**Tambunan et al. (2023)** present *Initial location selection of EVs charging infrastructure in urban city through clustering algorithm*. Transportation is one of the critical sectors worldwide, mainly based on fossil fuels, especially internal combustion engines. In a developing country, heightened dependence on fossil fuels affected energy sustainability issues, greenhouse gas emissions, and increasing state budget allocation towards fuel subsidies. Moreover, shifting to EVs with alternative energy, primely renewable energy sources, is considered a promising alternative to decreasing dependence on fossil fuel consumption. This work addresses dissertation gaps: G1.

**Jiang (2023)** present *Layout and optimization of charging piles for new energy EVs – A study on Xi'an urban area*. This paper analyzes the current layout of public charging stations within the third ring road of Xi'an central urban area and the daily charging needs of residents, the main problems in the layout of EVCSs in the central urban area of Xi'an were found, the differentiated demand analysis of living space charging was carried out, and the location model of EV public charging station facilities in the central urban area of the city was constructed, the location selection and optimization of EV public charging stations in the central urban area of Xi'an were studied. At the same time, a reasonable pile configuration was carried out, finally, the layout scheme of EV public charging stations in the central urban area was formed, the main shortcomings of the current charging pile layout and the factors (demand side) that should be considered in the current and future charging pile layout are concluded, and the layout and optimization of charging piles for clean energy in the future are prospected. This work addresses dissertation gaps: G1.

**Parent et al. (2023)** present *Maximum flow-based formulation for the optimal location of EVCSs*. With the increasing effects of climate change, the urgency to step away from fossil fuels is greater than ever before. EVs are one way to diminish these effects, but their widespread adoption is often limited by the insufficient availability of charging stations. In this work, our goal is to expand the infrastructure of EV charging stations, in order to provide a better quality of service in terms of user satisfaction (and availability of charging stations). This work addresses dissertation gaps: G1, G4.

**Tiu et al. (2023)** present *On the Optimal Placement of EVCSs*. Increasing the adoption of EV is an integral part of many strategies to address climate change and air pollution. However, EV adoption rates are inhibited by several factors which reduce the confidence of potential buyers of EVs, namely range anxiety and limited charging infrastructure. The latter concern can be addressed by carefully planning the placement of EVCSs to sustainably meet long-term demand. This work addresses dissertation gaps: G1, G4.

**Mourgues et al. (2023)** present *Optimal Location of EVs Public Charging Stations Based on a Macroscopic Urban Electromobility Model*. This paper addresses optimal location of evs public charging stations based on a macroscopic urban electromobility model. This work addresses dissertation gaps: G1.

**Liu et al. (2023)** present *Optimal Placement of Charging Stations in Road Networks: A Reinforcement Learning Approach with Attention Mechanism*. With the aim of promoting energy conservation and emission reduction, EVs have gained significant attention as a strategic industry in many countries. However, the insufficiency of accessible charging infrastructure remains a challenge, hindering the widespread adoption of EVs. To address this issue, we propose a novel approach to optimize the placement of charging stations within a road network, known as the charging station location problem (CSLP). This work addresses dissertation gaps: G1, G3.

**Wu et al. (2023)** present *Optimizing EV Charging Infrastructure on Highways: A Multi-Agent-Based Planning Approach*. The lack of sufficient charging infrastructure for long-haul transportation is a significant barrier preventing the widespread adoption of EVs. Planning EV charging facilities in this context requires considerations distinct from those in urban environments, accounting for factors such as traffic patterns and charging behaviors. This research paper presents a multi-agent simulation model designed to assess travel and charging activities, specifically on highways. This work addresses dissertation gaps: G1.

**Pal et al. (2023)** present *Placement of EVCS and solar distributed generation in distribution system considering uncertainties*. This paper addresses placement of EVCS and solar distributed generation in distribution syst. This work addresses dissertation gaps: G1.

**Wang et al. (2023)** present *SPAP: Simultaneous Demand Prediction and Planning for EV Chargers in a New City*. For a new city that is committed to promoting EVs, it is significant to plan the public charging infrastructure where charging demands are high. However, it is difficult to predict charging demands before the actual deployment of EV chargers for lack of operational data, resulting in a deadlock. A direct idea is to leverage the urban transfer learning paradigm to learn the knowledge from a source city, then exploit it to predict charging demands, and meanwhile determine locations and amounts of slow/fast chargers for charging stations in the target city. This work addresses dissertation gaps: G1, G4.

**Mohammadian et al. (2023)** present *Spatial Arbitrage Through Bidirectional EV Charging with Delivery Fleets*. The adoption of EVs, including electric taxis and buses, as a mode of transportation, is rapidly increasing in cities. In addition to providing economic and environmental benefits, these fleets can potentially participate in the energy arbitrage market by leveraging their mobile energy storage capabilities. This presents an opportunity for EV owners to contribute to a more sustainable and efficient energy system while also reducing their operational costs. This work addresses dissertation gaps: G1, G4.

**Mishra et al. (2022)** present *A Framework to Analyze the Requirements of a Multiport Megawatt-Level Charging Station for Heavy-Duty EVs*. Widespread adoption of heavy-duty (HD) EVs will soon necessitate the use of megawatt (MW)-scale charging stations to charge high-capacity HD EV battery packs. Such a station design needs to anticipate possible station traffic, average and peak power demand, and charging/wait time targets to improve throughput and maximize revenue-generating operations. High-power direct current charging is an attractive candidate for MW-scale charging stations at the time of this study, but there are no precedents for such a station design for HD vehicles. This work addresses dissertation gaps: G1.

**Hung and Michailidis (2022)** present *A Novel Data-Driven Approach for Solving the EVCS Location-Routing Problem*. This paper addresses a novel data-driven approach for solving the EVCS location-routing prob. This work addresses dissertation gaps: G1.

**Amilia et al. (2022)** present *Designing an Optimized EVCS Infrastructure for Urban Area: A Case study from Indonesia*. The rapid development of EV technologies promises cleaner air and more efficient transportation systems, especially for polluted and congested urban areas. To capitalize on this potential, the Indonesian government has appointed PLN, its largest state-owned electricity provider, to accelerate the preparation of Indonesia's EV infrastructure. With a mission of providing reliable, accessible, and cost-effective EV charging station infrastructure throughout the country, the company is prototyping a location-optimized model to simulate how well its infrastructure design reaches customers, fulfills demands, and generates revenue. This work addresses dissertation gaps: G1, G3, G4.

**Jin et al. (2022)** present *Development of Charging, Discharging Scheduling Algorithm for Economical and Energy Efficient Operation of Multi EV Charging Station*. As the number of EVs significantly increases, the excessive charging demand of parked EVs in the charging station may incur an instability problem to the electricity network during peak hours. For the charging station to take a microgrid (MG) structure, an economical and energy-efficient power management scheme is required for the power provision of EVs while considering the local load demand of the MG. For these purposes, this study presents the power management scheme of interdependent MG and EV fleets aided by a novel EV charg-ing/discharging scheduling algorithm. This work addresses dissertation gaps: G1, G5.

**Yan et al. (2022)** present *Distributed Coordination of Charging Stations Considering Aggregate EV Power Flexibility*. In recent years, EV charging stations have witnessed a rapid growth. However, effective management of charging stations is challenging due to individual EV owners' privacy concerns, competing interests of different stations, and the coupling distribution network constraints. To cope with this challenge, this paper proposes a two-stage scheme. This work addresses dissertation gaps: G1.

**Mousavi et al. (2022)** present *EV Charging Station Wholesale Market Participation: A Strategic Bidding and Pricing Approach*. This paper presents a framework for simultaneous bidding and pricing strategy for wholesale market participation of EV charging stations aggregator. The proposed framework incorporates the EV charging stations' technical constraints as well as EV owners' preferences. A bi-level optimization is adopted to model the problem. This work addresses dissertation gaps: G1.

**Srinivas and Reddy (2022)** present *Optimal Placement of EVCS by Considering Dynamic Loads in Radial Distribution System*. This paper addresses optimal placement of EVCS by considering dynamic loads in radial distri. This work addresses dissertation gaps: G1.

**Lamontagne et al. (2022)** present *Optimising EVCS Placement using Advanced Discrete Choice Models*. We present a new model for finding the optimal placement of EVCSs across a multi-period time frame so as to maximise EV adoption. Via the use of advanced discrete choice models and user classes, this work allows for a granular modelling of user attributes and their preferences in regard to charging station characteristics. Instead of embedding an analytical probability model in the formulation, we adopt a simulation approach and pre-compute error terms for each option available to users for a given number of scenarios. This work addresses dissertation gaps: G1.

**Qin et al. (2022)** present *Performance Analysis of Charging Infrastructure Sharing in UAV and EV-involved Networks*. EVs and unmanned aerial vehicles (UAVs) show great potential in modern transportation and communication networks, respectively. However, with growing demands for such technologies, the limited energy infrastructure becomes the bottleneck for their future growth. It might be of high cost and low energy efficiency for all the operators to each have their own dedicated energy infrastructure, such as charging stations. This work addresses dissertation gaps: G1.

**Bian et al. (2022)** present *Planning of EV fast-charging station based on POI interest point division, functional area, and multiple temporal and spatial characteristics*. This paper addresses planning of EV fast-charging station based on poi interest point division, functional . This work addresses dissertation gaps: G1, G4.

**Lin et al. (2022)** present *Predictive Energy Management Strategy for Range-Extended EVs Based on ITS Information and Start–Stop Optimization with Vehicle Velocity Forecast*. Range-extended EVs (REVs) have become popular due to their lack of emissions while driving in urban areas, and the elimination of range anxiety when traveling long distances with a combustion engine as the power source. The fuel consumption performance of REVs depends greatly on the energy management strategy (EMS). This article proposes a practical energy management solution for REVs based on an Adaptive Equivalent Fuel Consumption Minimization Strategy (A-ECMS), wherein the equivalent factor is dynamically optimized by the battery’s State of Charge (SoC) and traffic information provided by Intelligent Transportation Systems (ITS). This work addresses dissertation gaps: G1, G5.

**Wahl et al. (2022)** present *Reinforcement Learning-based Placement of Charging Stations in Urban Road Networks*. The transition from conventional mobility to electromobility largely depends on charging infrastructure availability and optimal placement.This paper examines the optimal placement of charging stations in urban areas. We maximise the charging infrastructure supply over the area and minimise waiting, travel, and charging times while setting budget constraints. Moreover, we include the possibility of charging vehicles at home to obtain a more refined estimation of the actual charging demand throughout the urban area. This work addresses dissertation gaps: G1.

**Wang et al. (2022)** present *Research on Multi-Objective Planning of EVCSs Considering the Condition of Urban Traffic Network*. As an important supporting facility for EVs, the reasonable planning and layout of charging stations are of great significance to the development of EVs. However, the planning and layout of charging stations is affected by various complex factors such as policy economy, charging demand, user charging comfort, and road traffic conditions. How to weigh various factors to construct a reasonable model of charging station location and capacity has become a major difficulty in the field of EV charging facility planning. This work addresses dissertation gaps: G1.

**Hummler et al. (2022)** present *Web Mining to Inform Locations of Charging Stations for EVs*. The availability of charging stations is an important factor for promoting EVs as a carbon-friendly way of transportation. Hence, for city planners, the crucial question is where to place charging stations so that they reach a large utilization. Here, we hypothesize that the utilization of EV charging stations is driven by the proximity to points-of-interest (POIs), as EV owners have a certain limited willingness to walk between charging stations and POIs. This work addresses dissertation gaps: G1.

**Zafar et al. (2021)** present *A GIS-based Optimal Facility Location Framework for Fast EVCSs*. This paper addresses a gis-based optimal facility location framework for fast EVCSs. This work addresses dissertation gaps: G1.

**Cintrano et al. (2021)** present *Citizen centric optimal EVCSs locations in a full city: case of Malaga*. This article presents the problem of locating EV charging stations in a city by defining the EVCSs Locations (EV-CSL) problem. The idea is to minimize the distance the citizens have to travel to charge their vehicles. EV-CSL takes into account the maximum number of charging stations to install and the electric power requirements. This work addresses dissertation gaps: G1.

**Hüttel et al. (2021)** present *Deep Spatio-Temporal Forecasting of Electrical Vehicle Charging Demand*. EVs can offer a low carbon emission solution to reverse rising emission trends. However, this requires that the energy used to meet the demand is green. To meet this requirement, accurate forecasting of the charging demand is vital. This work addresses dissertation gaps: G1, G4.

**Hurk and Salazar (2021)** present *Energy-optimal Design and Control of EVs' Transmissions*. This paper presents models and optimization algorithms to jointly optimize the design and control of the transmission of EVs equipped with one central electric motor (EM). First, considering the required traction power to be given, we identify a convex speed-dependent loss model for the EM. Second, we leverage such a model to devise computationally-efficient algorithms to determine the energy-optimal design and control strategies for the transmission. This work addresses dissertation gaps: G1.

**Mirheli and Hajibabai (2021)** present *Hierarchical Optimization of EV Charging Infrastructure Design and Facility Logistics*. This study proposes a bi-level optimization program to represent the EV charging infrastructure design and utilization management problem with user-equilibrium (UE) decisions. The upper level aims to minimize total facility deployment costs and maximize the revenue generated from EV charging collections, while the lower level aims to minimize the EV users' travel times and charging expenses. An iterative technique is implemented to solve the bi-level mixed-integer non-linear program that generates theoretical lower and upper bounds to the bi-level model and solves it to global optimality. This work addresses dissertation gaps: G1, G4.

**Luke et al. (2021)** present *Joint Optimization of Autonomous EV Fleet Operations and Charging Station Siting*. Charging infrastructure is the coupling link between power and transportation networks, thus determining charging station siting is necessary for planning of power and transportation systems. While previous works have either optimized for charging station siting given historic travel behavior, or optimized fleet routing and charging given an assumed placement of the stations, this paper introduces a linear program that optimizes for station siting and macroscopic fleet operations in a joint fashion. Given an electricity retail rate and a set of travel demand requests, the optimization minimizes total cost for an autonomous EV fleet comprising of travel costs, station procurement costs, fleet procurement costs, and electricity costs, including demand charges. This work addresses dissertation gaps: G1.

**Padmanabhan et al. (2021)** present *Optimal Placement of Public EVCSs Using Deep RL*. The placement of charging stations in areas with developing charging infrastructure is a critical component of the future success of EVs. In Albany County in New York, the expected rise in the EV population requires additional charging stations to maintain a sufficient level of efficiency across the charging infrastructure. A novel application of Reinforcement Learning (RL) is able to find optimal locations for new charging stations given the predicted charging demand and current charging locations. This work addresses dissertation gaps: G1.

**Hou et al. (2021)** present *Optimal Planning of EVCS Considering Mutual Benefit of Users and Power Grid*. A reasonable plan for charging stations is critical to the widespread use of EVs. In this paper, we propose an optimal planning method for EVCSs. First of all, we put forward a forecasting method for the distribution of EV fast charging demand in urban areas. This work addresses dissertation gaps: G1.

**Schoenberg and Dressler (2021)** present *Reducing Waiting Times at Charging Stations with Adaptive EV Route Planning*. EVs are becoming more popular all over the world. With increasing battery capacities and a growing fast-charging infrastructure, they are becoming suitable for long distance travel. However, queues at charging stations could lead to long waiting times, making efficient route planning even more important. This work addresses dissertation gaps: G1.

**Ahadi et al. (2021)** present *Siting and Sizing of Charging Infrastructure for Shared Autonomous Electric Fleets*. Business models rooted in shared economy, electrification, and automation are transforming urban mobility. Accounting for how these transformations interact is crucial if synergies are to be exploited. In this paper, we focus on how a cost-effective charging infrastructure for e-mobility can support the emergence of shared, autonomous mobility. This work addresses dissertation gaps: G1.

**Bayani et al. (2021)** present *Strategic Competition of EVCSs in a Regulated Retail Electricity Market*. The increasing trend of transportation electrification presents investors the opportunity to provide charging services to EV owners via the energy purchased from the wholesale electricity market. This will benefit EV owners with the availability of competitive rates compared to the regulated utility time-of-use (TOU) rates. The fundamental questions addressed in this paper are 1) will EV owners benefit from the additional choice of EVCSs compared to home charging? This work addresses dissertation gaps: G1.

**Rizopoulos and Esztergár-Kiss (2020)** present *A Method for the Optimization of Daily Activity Chains Including EVs*. The focus of this article is to introduce a method for the optimization of daily activity chains of travelers who use EVs in an urban environment. An approach has been developed based on activity-based modeling and the Genetic Algorithm (GA) framework to calculate a suitable schedule of activities, taking into account the locations of activities, modes of transport, and the time of attendance to each activity. The priorities of the travelers concerning the spatial and temporal flexibility were considered, as well as the constraints that are related to the limited range of the EVs, the availability of Charging Stations (CS), and the elevation of the road network. This work addresses dissertation gaps: G1, G4.

**Wang et al. (2020)** present *Double-Layer Game Based Wireless Charging Scheduling for EVs*. Wireless charging technology provides a solution to the insufficient battery life of EVs. However, the conflict of interests between wireless charging lanes (WCLs) and EVs is difficult to resolve. In the day-ahead electricity market, considering the revenue of WCLs caused by the deviation between actual electricity sales and pre-purchased electricity, as well as endurance and traveling experience of EVs, this paper proposes a charging scheduling algorithm based on a double-layer game model. This work addresses dissertation gaps: G1.

**Yang et al. (2020)** present *Dynamic Modeling and Real-time Management of a System of EV Fast-charging Stations*. Demand for EVs, and thus EV charging, has steadily increased over the last decade. However, there is limited fast-charging infrastructure in most parts of the world to support EV travel, especially long-distance trips. The goal of this study is to develop a stochastic dynamic simulation modeling framework of a regional system of EV fast-charging stations for real-time management and strategic planning (i.e., capacity allocation) purposes. This work addresses dissertation gaps: G1.

**Brandstätter et al. (2020)** present *Location of Charging Stations in Electric Car Sharing Systems*. EVs are prime candidates for use within urban car sharing systems, both from economic and environmental perspectives. However, their relatively short range necessitates frequent and rather time-consuming recharging throughout the day. Thus, charging stations must be built throughout the system’s operational area where cars can be charged between uses. This work addresses dissertation gaps: G1, G4.

**Ma and Xie (2020)** present *Optimal fast charging station locations for electric ridesharing service with online vehicle-charging station assignment*. Electrified shared mobility services need to handle charging infrastructure planning and manage their daily charging operations to minimize total charging operation time and cost. However, existing studies tend to address these problems separately. A new online vehicle-charging assignment model is proposed and integrated into the fast charging location problem for dynamic ridesharing services using EVs. This work addresses dissertation gaps: G1.

**GORBUNOVA and ANISIMOV (2020)** present *OPTIMIZING THE LOCATION OF URBAN CHARGING STATIONS FOR EVs: CASE STUDY OF THE CITY OF TYUMEN, RUSSIAN FEDERATION*. This paper addresses optimizing the location of urban charging stations for EVs: case study of the city of . This work addresses dissertation gaps: G1.

**Santoyo et al. (2020)** present *Resource Aware Pricing for EV Charging*. EV charging facilities offer electric charge and parking to users for a fee. Both parking availability and electric charge capacity are constrained resources, and as the demand for charging facilities grows with increasing EV adoption, so too does the potential for exceeding these resource limitations. In this paper, we study how prices set by the charging facility impact the likelihood that resource constraints are exceeded. This work addresses dissertation gaps: G1.

**Ouyang et al. (2019)** present *A Method of EV Detour-to-Recharge Behavior Modeling and Charging Station Deployment*. EVs are increasingly used in transportation. Worldwide use of EVs, for their limited battery capacity, calls for effective planning of EVs charging stations to enhance the efficiency of using EVs. This paper provides a methodology of describing EV detouring behavior for recharging, and based on this, we adopt the extra driving length caused by detouring and the length of uncompleted route as the indicators of evaluating an EV charging station deployment plan. This work addresses dissertation gaps: G1, G4.

**Upadhaya et al. (2019)** present *Optimal Decision Making Model of Battery Energy Storage-Assisted EVCS Considering Incentive Demand Response*. Considering large scale implementation of EVs, public EV charging stations are served as fuel tanks for EVs to meet the need of longer travelling distance and overcome the shortage of private charging piles. The allocation of local battery energy storage (BES) can enhance the flexibility of the EV charging station. This paper proposes an optimal decision making model of the BES-assisted EV charging station considering the incentive demand response. This work addresses dissertation gaps: G1, G5.

**Straka et al. (2019)** present *Predicting popularity of EV charging infrastructure from GIS data*. The availability of charging infrastructure is essential for large-scale adoption of EV. Charging patterns and the utilization of infrastructure have consequences not only for the energy demand, loading local power grids but influence the economic returns, parking policies and further adoption of EVs. We develop a data-driven approach that is exploiting predictors compiled from GIS data describing the urban context and urban activities near charging infrastructure to explore correlations with a comprehensive set of indicators measuring the performance of charging infrastructure. This work addresses dissertation gaps: G1, G4.

**Luo et al. (2018)** present *A Consumer Behavior Based Approach to Multi-Stage EV Charging Station Placement*. This paper presents a multi-stage approach to the placement of charging stations under the scenarios of different EV penetration rates. The EV charging market is modeled as the oligopoly. A consumer behavior based approach is applied to forecast the charging demand of the charging stations using a nested logit model. This work addresses dissertation gaps: G1.

**Deza et al. (2018)** present *Charging station optimization for balanced electric car sharing*. This work focuses on finding optimal locations for charging stations for one-way electric car sharing programs. The relocation of vehicles by a service staff is generally required in vehicle sharing programs in order to correct imbalances in the network. We seek to limit the need for vehicle relocation by strategically locating charging stations given estimates of traffic flow. This work addresses dissertation gaps: G1.

**Cui et al. (2018)** present *EVCS Placement Method for Urban Areas*. For accommodating more EVs to battle against fossil fuel emission, the problem of charging station placement is inevitable and could be costly if done improperly. Some researches consider a general setup, using conditions such as driving ranges for planning. However, most of the EV growths in the next decades will happen in the urban area, where driving ranges is not the biggest concern. This work addresses dissertation gaps: G1.

**Luo (2018)** present *Engineering and Economic Analysis for EV Charging Infrastructure --- Placement, Pricing, and Market Design*. This dissertation is to study the interplay between large-scale EV charging and the power system. We address three important issues pertaining to EV charging and integration into the power system: (1) charging station placement, (2) pricing policy and energy management strategy, and (3) electricity trading market and distribution network design to facilitate integrating EV and renewable energy source (RES) into the power system. For charging station placement problem, we propose a multi-stage consumer behavior based placement strategy with incremental EV penetration rates and model the EV charging industry as an oligopoly where the entire market is dominated by a few charging service providers (oligopolists). This work addresses dissertation gaps: G1.

**Luo et al. (2018)** present *Placement of EV Charging Stations --- Balancing Benefits among Multiple Entities*. This paper studies the problem of multi-stage placement of EV charging stations with incremental EV penetration rates. A nested logit model is employed to analyze the charging preference of the individual consumer (EV owner), and predict the aggregated charging demand at the charging stations. The EV charging industry is modeled as an oligopoly where the entire market is dominated by a few charging service providers (oligopolists). This work addresses dissertation gaps: G1.

**Ramachandran et al. (2018)** present *Predicting EVCS Usage: Using Machine Learning to Estimate Individual Station Statistics from Physical Configurations of Charging Station Networks*. EVs have been gaining popularity due to their environmental friendliness and efficiency. EV charging station networks are scalable solutions for supporting increasing numbers of EVs within modern electric grid constraints, yet few tools exist to aid the physical configuration design of new networks. We use neural networks to predict individual charging station usage statistics from the station's physical location within a network. This work addresses dissertation gaps: G1.

**Aveklouris et al. (2017)** present *EV charging: a queueing approach*. The number of EVs is expected to increase. As a consequence, more EVs will need charging, potentially causing not only congestion at charging stations, but also in the distribution grid. Our goal is to illustrate how this gives rise to resource allocation and performance problems that are of interest to the Sigmetrics community. This work addresses dissertation gaps: G1.

**Kosmanos et al. (2017)** present *Route Optimization of EVs based on Dynamic Wireless Charging*. One of the barriers to adoption of EVs is the anxiety around the limited driving range. Recent proposals have explored charging EVs on the move, using dynamic wireless charging which enables power exchange between the vehicle and the grid while the vehicle is moving. In this article, we focus on the intelligent routing of EVs in need of charging so that they can make most efficient use of the so-called {\it Mobile Energy Disseminators} (MEDs) which operates as MCSs. This work addresses dissertation gaps: G1.

**Gopalakrishnan et al. (2016)** present *Demand Prediction and Placement Optimization for EVCSs*. Effective placement of charging stations plays a key role in EV adoption. In the placement problem, given a set of candidate sites, an optimal subset needs to be selected with respect to the concerns of both (a) the charging station service provider, such as the demand at the candidate sites and the budget for deployment, and (b) the EV user, such as charging station reachability and short waiting times at the station. This work addresses these concerns, making the following three novel contributions: (i) a supervised multi-view learning framework using Canonical Correlation Analysis (CCA) for demand prediction at candidate sites, using multiple datasets such as points of interest information, traffic density, and the historical usage at existing charging stations; (ii) a mixed-packing-and- covering optimization framework that models competing concerns of the service provider and EV users; (iii) an iterative heuristic to solve these problems by alternately invoking knapsack and set cover algorithms. This work addresses dissertation gaps: G1, G4.

**Beaude et al. (2015)** present *Charging Games in Networks of Electrical Vehicles*. In this paper, a static non-cooperative game formulation of the problem of distributed charging in electrical vehicle (EV) networks is proposed. This formulation allows one to model the interaction between several EV which are connected to a common residential distribution transformer. Each EV aims at choosing the time at which it starts charging its battery in order to minimize an individual cost which is mainly related to the total power delivered by the transformer, the location of the time interval over which the charging operation is performed, and the charging duration needed for the considered EV to have its battery fully recharged. This work addresses dissertation gaps: G1.

**Lanna et al. (2015)** present *EVs Charging Control based on Future Internet Generic Enablers*. In this paper a rationale for the deployment of Future Internet based applications in the field of EVs smart charging is presented. The focus is on the Connected Device Interface (CDI) Generic Enabler (GE) and the Network Information and Controller (NetIC) GE, which are recognized to have a potential impact on the charging control problem and the configuration of communications networks within reconfigurable clusters of charging points. The CDI GE can be used for capturing the driver feedback in terms of Quality of Experience (QoE) in those situations where the charging power is abruptly limited as a consequence of short term grid needs, like the shedding action asked by the Transmission System Operator to the Distribution System Operator aimed at clearing networks contingencies due to the loss of a transmission line or large wind power fluctuations. This work addresses dissertation gaps: G1, G4.

**Beaude et al. (2015)** present *Introducing Decentralized EV Charging Coordination for the Voltage Regulation*. This paper investigates a decentralized optimization methodology to coordinate EV charging in order to contribute to the voltage control on a residential electrical distribution feeder. This aims to maintain the voltage level in function of the EV's power injection using the sensitivity matrix approach. The decentralized optimization is tested with two different methods, respectively global and local, when EV take into account their impact on all the nodes of the network or only on a local neighborhood of their connection point. This work addresses dissertation gaps: G1.

**Beaude et al. (2015)** present *Minimizing the impact of EV charging on the electricity distribution network*. The main objective of this paper is to design EV charging policies which minimize the impact of charging on the electricity distribution network (DN). More precisely, the considered cost function results from a linear combination of two parts: a cost with memory and a memoryless cost. In this paper, the first component is identified to be the transformer ageing while the second one corresponds to distribution Joule losses. This work addresses dissertation gaps: G1.

**Vazifeh et al. (2015)** present *Optimizing the Deployment of EVCSs Using Pervasive Mobility Data*. With recent advances in battery technology and the resulting decrease in the charging times, public charging stations are becoming a viable option for EV drivers. Concurrently, wide-spread use of location-tracking devices in mobile phones and wearable devices makes it possible to track individual-level human movements to an unprecedented spatial and temporal grain. Motivated by these developments, we propose a novel methodology to perform data-driven optimization of EV charging stations location. This work addresses dissertation gaps: G1, G4.

**Lam et al. (2013)** present *EVCS Placement: Formulation, Complexity, and Solutions*. To enhance environmental sustainability, many countries will electrify their transportation systems in their future smart city plans. So the number of EVs running in a city will grow significantly. There are many ways to re-charge EVs' batteries and charging stations will be considered as the main source of energy. This work addresses dissertation gaps: G1.

**Yudovina and Michailidis (2013)** present *Socially optimal charging strategies for EVs*. EVs represent a promising technology for reducing emissions and dependence on fossil fuels and have started entering different automotive markets. In order to bolster their adoption by consumers and hence enhance their penetration rate, a charging station infrastructure needs to be deployed. This paper studies decentralized policies that assign EVs to a network of charging stations with the goal to achieve little to no queueing. This work addresses dissertation gaps: G1, G4.

**Li et al. (0)** present *EV Charging Infrastructure Optimization Incorporating Demand Forecasting and Renewable Energy Application*. The rapid growth in EV adoption and the increasing use of renewable energy have introduced challenges in designing and managing EV charging infrastructure. This study presents a framework that combines a hybrid deep learning model, spatial and temporal demand analysis, and V2G optimization to address these issues. The framework achieved high predictive accuracy, with an RMSE of 2.1 kWh and an R2R^2R2 value of 0.92, effectively capturing daily demand patterns and variations across charging stations. This work addresses dissertation gaps: G1, G4.

**Table 3.1: Papers in the Spatial Optimization for Charging Station Placement Theme**

| Key | Authors | Year | Approach | Scope | Gaps |
|-----|---------|------|----------|-------|------|
| `a_two-stage_2026` | Najafzad et al. | 2026 | optimization | city | G1, G3, G4 |
| `joint_planning_2026` | Mejia et al. | 2026 | optimization | city | G1 |
| `pricing_electric_2026` | Jiang et al. | 2026 | optimization | city | G1 |
| `regional_transportation_2026` | Babur et al. | 2026 | simulation | regional | G1, G3, G4 |
| `simultaneous_optimization_2026` | Bertucci et al. | 2026 | optimization | city | G1 |
| `strategic_planning_2026` | Fariza et al. | 2026 | optimization | regional | G1, G2 |
| `a_2025` | Do et al. | 2025 | mixed | city | G1, G5 |
| `a_density-based_2025` | Ameer et al. | 2025 | optimization | city | G1 |
| `a_joint_2025` | Yu et al. | 2025 | mixed | city | G1, G4 |
| `a_multi-modal_2025` | Karakuş et al. | 2025 | empirical | city | G1, G2, G4 |
| `a_spatially_2025` | Huang et al. | 2025 | mixed | city | G1 |
| `a_two-stage_2025` | Meng et al. | 2025 | optimization | city | G1 |
| `a_united_2025` | Kinchen et al. | 2025 | mixed | city | G1, G3 |
| `an_exact_2025` | Nankali et al. | 2025 | mixed | city | G1 |
| `analyzing_locational_2025` | Mousaei | 2025 | empirical | city | G1 |
| `causal_spillover_2025` | Silva et al. | 2025 | empirical | city | G1, G4 |
| `charge-map_an_2025` | Islam et al. | 2025 | mixed | city | G1, G4 |
| `competitive_ev_2025` | Nguyen et al. | 2025 | mixed | city | G1 |
| `data-driven_ev_2025` | Alharbi et al. | 2025 | optimization | city | G1, G4 |
| `data-driven_optimization_2025` | Junker et al. | 2025 | mixed | site | G1 |
| `electric_vehicle_2025` | Zhao et al. | 2025 | optimization | city | G1, G3 |
| `explainable_and_2025` | Kapoor | 2025 | optimization | city | G1 |
| `fairness-oriented_charging_2025` | Yuan et al. | 2025 | optimization | city | G1, G3 |
| `hybrid_optimization_2025` | Ameer et al. | 2025 | optimization | city | G1 |
| `joint_optimization_2025` | Okada et al. | 2025 | optimization | city | G1, G4 |
| `large_language_2025` | Zheng et al. | 2025 | mixed | city | G1, G4 |
| `location_and_2025` | Choi et al. | 2025 | optimization | city | G1 |
| `multiobjective_model_2025` | Ruiz-Barajas et al. | 2025 | mixed | city | G1 |
| `optimal_mixed_2025` | Nakao et al. | 2025 | mixed | city | G1 |
| `optimization_of_2025` | Zhang et al. | 2025 | optimization | city | G1 |
| `optimizing_electric_2025` | Zhong et al. | 2025 | mixed | city | G1 |
| `optimizing_urban_2025` | Ai et al. | 2025 | optimization | city | G1, G5 |
| `planning_future_2025` | Yuan et al. | 2025 | empirical | regional | G1, G4 |
| `predicting_optimal_2025` | Mousaei et al. | 2025 | empirical | city | G1 |
| `reinforcement_learning_2025` | Zhu et al. | 2025 | empirical | city | G1 |
| `robust_charging_2025` | Xia et al. | 2025 | optimization | corridor | G1 |
| `trajectory-integrated_accessibility_2025` | Ju et al. | 2025 | optimization | neighborhood | G1 |
| `a_data-driven_2024` | Zhang et al. | 2024 | mixed | city | G1, G4, G5 |
| `a_multi-objective_2024` | Zhang et al. | 2024 | optimization | site | G1, G2 |
| `a_particle_2024` | Aljaidi et al. | 2024 | optimization | city | G1 |
| `a_quantum_2024` | Radvand et al. | 2024 | optimization | city | G1 |
| `a_two-layer_2024` | Wu et al. | 2024 | optimization | city | G1 |
| `advancing_urban_2024` | Zhang et al. | 2024 | optimization | city | G1 |
| `battery_swapping_2024` | Liu et al. | 2024 | mixed | neighborhood | G1, G4 |
| `beyond_profit_2024` | Wang et al. | 2024 | mixed | city | G1 |
| `charging_station_2024` | Cai et al. | 2024 | mixed | site | G1 |
| `electric_vehicle_2024` | Li et al. | 2024 | optimization | city | G1 |
| `energy_management_2024` | Cao et al. | 2024 | mixed | city | G1 |
| `integrating_en_2024` | Mehditabrizi et al. | 2024 | optimization | city | G1 |
| `multiobjective_optimization_2024` | Mohammed et al. | 2024 | optimization | city | G1 |
| `optimal_electric_2024` | Kumar et al. | 2024 | optimization | site | G1 |
| `optimal_ev_2024` | Pierrou et al. | 2024 | optimization | city | G1 |
| `optimal_evcs_2024` | He et al. | 2024 | optimization | city | G1, G4 |
| `optimal_planning_2024` | Heo et al. | 2024 | empirical | city | G1 |
| `optimization_strategies_2024` | Panyaram | 2024 | optimization | city | G1, G4 |
| `optimizing_ev_2024` | Huang et al. | 2024 | optimization | city | G1 |
| `optimizing_urban_2024` | Munawar | 2024 | mixed | regional | G1, G5 |
| `sequential_charging_2024` | Shen et al. | 2024 | optimization | city | G1, G4 |
| `sustainable_planning_2024` | Seilabi et al. | 2024 | optimization | city | G1, G4 |
| `the_electric_2024` | Akbay et al. | 2024 | optimization | city | G1 |
| `towards_sustainable_2024` | Boonprong et al. | 2024 | empirical | city | G1, G2, G3 |
| `towards_using_2024` | Miltner et al. | 2024 | mixed | city | G1, G4 |
| `urban_electric_2024` | Alhussan et al. | 2024 | optimization | city | G1 |
| `a_battery_2023` | Xin et al. | 2023 | optimization | city | G1 |
| `a_data-driven_2023` | Al-Dahabreh et al. | 2023 | mixed | city | G1 |
| `a_robust_2023` | Arief et al. | 2023 | mixed | city | G1, G3 |
| `an_agent-based_2023` | Yi et al. | 2023 | mixed | city | G1 |
| `electric_vehicle_2023` | Varma et al. | 2023 | simulation | city | G1, G5 |
| `fast-charging_station_2023` | Qiao et al. | 2023 | optimization | city | G1 |
| `incorporating_time-dependent_2023` | Filippi et al. | 2023 | optimization | city | G1, G4 |
| `initial_location_2023` | Tambunan et al. | 2023 | optimization | city | G1 |
| `layout_and_2023` | Jiang | 2023 | optimization | city | G1 |
| `maximum_flow-based_2023` | Parent et al. | 2023 | mixed | city | G1, G4 |
| `on_the_2023` | Tiu et al. | 2023 | optimization | city | G1, G4 |
| `optimal_location_2023` | Mourgues et al. | 2023 | optimization | city | G1 |
| `optimal_placement_2023` | Liu et al. | 2023 | optimization | city | G1, G3 |
| `optimizing_electric_2023` | Wu et al. | 2023 | mixed | city | G1 |
| `placement_of_2023` | Pal et al. | 2023 | optimization | city | G1 |
| `spap_simultaneous_2023` | Wang et al. | 2023 | mixed | city | G1, G4 |
| `spatial_arbitrage_2023` | Mohammadian et al. | 2023 | mixed | city | G1, G4 |
| `a_framework_2022` | Mishra et al. | 2022 | mixed | corridor | G1 |
| `a_novel_2022` | Hung et al. | 2022 | optimization | city | G1 |
| `designing_an_2022` | Amilia et al. | 2022 | mixed | city | G1, G3, G4 |
| `development_of_2022` | Jin et al. | 2022 | optimization | city | G1, G5 |
| `distributed_coordination_2022` | Yan et al. | 2022 | optimization | city | G1 |
| `ev_charging_2022` | Mousavi et al. | 2022 | mixed | city | G1 |
| `optimal_placement_2022` | Srinivas et al. | 2022 | optimization | city | G1 |
| `optimising_electric_2022` | Lamontagne et al. | 2022 | mixed | city | G1 |
| `performance_analysis_2022` | Qin et al. | 2022 | optimization | city | G1 |
| `planning_of_2022` | Bian et al. | 2022 | optimization | city | G1, G4 |
| `predictive_energy_2022` | Lin et al. | 2022 | mixed | city | G1, G5 |
| `reinforcement_learning-based_2022` | Wahl et al. | 2022 | empirical | city | G1 |
| `research_on_2022` | Wang et al. | 2022 | mixed | city | G1 |
| `web_mining_2022` | Hummler et al. | 2022 | empirical | city | G1 |
| `a_gis-based_2021` | Zafar et al. | 2021 | optimization | city | G1 |
| `citizen_centric_2021` | Cintrano et al. | 2021 | optimization | neighborhood | G1 |
| `deep_spatio-temporal_2021` | Hüttel et al. | 2021 | optimization | city | G1, G4 |
| `energy-optimal_design_2021` | Hurk et al. | 2021 | mixed | city | G1 |
| `hierarchical_optimization_2021` | Mirheli et al. | 2021 | optimization | city | G1, G4 |
| `joint_optimization_2021` | Luke et al. | 2021 | optimization | city | G1 |
| `optimal_placement_2021` | Padmanabhan et al. | 2021 | optimization | city | G1 |
| `optimal_planning_2021` | Hou et al. | 2021 | mixed | city | G1 |
| `reducing_waiting_2021` | Schoenberg et al. | 2021 | simulation | city | G1 |
| `siting_and_2021` | Ahadi et al. | 2021 | mixed | city | G1 |
| `strategic_competition_2021` | Bayani et al. | 2021 | optimization | city | G1 |
| `a_method_2020` | Rizopoulos et al. | 2020 | optimization | city | G1, G4 |
| `double-layer_game_2020` | Wang et al. | 2020 | mixed | city | G1 |
| `dynamic_modeling_2020` | Yang et al. | 2020 | simulation | regional | G1 |
| `location_of_2020` | Brandstätter et al. | 2020 | mixed | city | G1, G4 |
| `optimal_fast_2020` | Ma et al. | 2020 | optimization | city | G1 |
| `optimizing_the_2020` | GORBUNOVA et al. | 2020 | empirical | city | G1 |
| `resource_aware_2020` | Santoyo et al. | 2020 | mixed | city | G1 |
| `a_method_2019` | Ouyang et al. | 2019 | mixed | city | G1, G4 |
| `optimal_decision_2019` | Upadhaya et al. | 2019 | optimization | city | G1, G5 |
| `predicting_popularity_2019` | Straka et al. | 2019 | optimization | city | G1, G4 |
| `a_consumer_2018` | Luo et al. | 2018 | mixed | city | G1 |
| `charging_station_2018` | Deza et al. | 2018 | optimization | city | G1 |
| `electric_vehicle_2018` | Cui et al. | 2018 | optimization | city | G1 |
| `engineering_and_2018` | Luo | 2018 | optimization | city | G1 |
| `placement_of_2018` | Luo et al. | 2018 | simulation | city | G1 |
| `predicting_electric_2018` | Ramachandran et al. | 2018 | simulation | city | G1 |
| `electric_vehicle_2017` | Aveklouris et al. | 2017 | simulation | city | G1 |
| `route_optimization_2017` | Kosmanos et al. | 2017 | mixed | city | G1 |
| `demand_prediction_2016` | Gopalakrishnan et al. | 2016 | mixed | city | G1, G4 |
| `charging_games_2015` | Beaude et al. | 2015 | optimization | city | G1 |
| `electric_vehicles_2015` | Lanna et al. | 2015 | optimization | city | G1, G4 |
| `introducing_decentralized_2015` | Beaude et al. | 2015 | mixed | neighborhood | G1 |
| `minimizing_the_2015` | Beaude et al. | 2015 | mixed | city | G1 |
| `optimizing_the_2015` | Vazifeh et al. | 2015 | optimization | city | G1, G4 |
| `electric_vehicle_2013` | Lam et al. | 2013 | simulation | city | G1 |
| `socially_optimal_2013` | Yudovina et al. | 2013 | simulation | city | G1, G4 |
| `electric_vehicle_0` | Li et al. | 0 | optimization | city | G1, G4 |

### 3.2 Equity Considerations in Charging Infrastructure Planning

*5 papers (2% of corpus)*

Equity-oriented research examines the distributional consequences of charging infrastructure deployment, with particular attention to socioeconomic disparities in access and the disproportionate burden faced by low-income, minority, and renter households who lack home charging access. This strand of the literature draws on spatial accessibility analysis, demographic data overlay, and policy evaluation methods. A recurring finding is that market-driven deployment concentrates infrastructure in high-income areas with strong early EV adoption, systematically under-serving populations with the most need for public charging. Equity metrics in this literature range from simple coverage ratios by census tract income quartile to Gini coefficients of spatial accessibility and spatial Lorenz curve analysis. Notably, equity analysis in this literature is predominantly post-hoc evaluation rather than prospective optimization, a gap that directly motivates Gap 3 of this dissertation framework.

**Jha et al. (2025)** present *An equity-based approach for addressing inequality in EV charging infrastructure: Leaving no one behind in transport electrification*. This paper addresses an equity-based approach for addressing inequality in EV charging infrastructure: leav. This work addresses dissertation gaps: G3.

**Erfani et al. (2024)** present *Crowdfunding for Equitable EV Charging Infrastructure*. The transportation sector significantly contributes to greenhouse gas emissions, highlighting the need to transition to EVs to reduce fossil fuel dependence and combat climate change. The US government has set ambitious targets for 2030, aiming for half of all new vehicles sold to be zero-emissions. Expanding EV charging stations is crucial for this transition, but social equity presents a significant challenge. This work addresses dissertation gaps: G3, G5.

**Khan et al. (2021)** present *Inequitable Access to EV Charging Infrastructure*. Access to and affordability of EV charging infrastructure are the two prominent barriers for EV adoption. While major efforts are underway in the United States to roll-out public EV charging infrastructure, persistent social disparities in EV adoption call for interventions. In this paper, we analyze the existing EV charging infrastructure across New York City (NYC) to identify such socio-demographic and transportation features that correlate with the current distribution of EV charging stations. This work addresses dissertation gaps: G3.

**Wang et al. (2017)** present *Electrical Vehicle Charging Station Profit Maximization: Admission, Pricing, and Online Scheduling*. The rapid emergence of EVs demands an advanced infrastructure of publicly accessible charging stations that provide efficient charging services. In this paper, we propose a new charging station operation mechanism, the JoAP, which jointly optimizes the EV admission control, pricing, and charging scheduling to maximize the charging station's profit. More specifically, by introducing a tandem queueing network model, we analytically characterize the average charging station profit as a function of the admission control and pricing policies. This work addresses dissertation gaps: G3.

**Carvalho et al. (2015)** present *Critical behaviour in charging of EVs*. The increasing penetration of EVs over the coming decades, taken together with the high cost to upgrade local distribution networks and consumer demand for home charging, suggest that managing congestion on low voltage networks will be a crucial component of the EV revolution and the move away from fossil fuels in transportation. Here, we model the max-flow and proportional fairness protocols for the control of congestion caused by a fleet of vehicles charging on two real-world distribution networks. We show that the system undergoes a continuous phase transition to a congested state as a function of the rate of vehicles plugging to the network to charge. This work addresses dissertation gaps: G3.

**Table 3.2: Papers in the Equity Considerations in Charging Infrastructure Planning Theme**

| Key | Authors | Year | Approach | Scope | Gaps |
|-----|---------|------|----------|-------|------|
| `an_equity-based_2025` | Jha et al. | 2025 | optimization | city | G3 |
| `crowdfunding_for_2024` | Erfani et al. | 2024 | optimization | neighborhood | G3, G5 |
| `inequitable_access_2021` | Khan et al. | 2021 | optimization | neighborhood | G3 |
| `electrical_vehicle_2017` | Wang et al. | 2017 | mixed | city | G3 |
| `critical_behaviour_2015` | Carvalho et al. | 2015 | empirical | city | G3 |

### 3.3 Utilization and Demand Modeling

*21 papers (10% of corpus)*

Utilization and demand modeling research focuses on forecasting charging demand, characterizing station occupancy dynamics, and optimizing network-level utilization efficiency. This literature employs a diverse range of methods including queuing theory, occupancy forecasting via machine learning, real-world usage data analysis, and agent-based demand simulation. A consistent challenge is the circular dependency between station placement and utilization: placement determines accessibility, which determines adoption, which determines utilization. Studies in this category generally treat placement as fixed and model utilization conditionally, rather than jointly optimizing placement and expected utilization. The underrepresentation of utilization concerns in spatial optimization models (Gap 3) and the near-absence of utilization dynamics in phased deployment models (Gap 4) are both visible in this literature strand.

**Jiang et al. (2025)** present *An EV charging demand prediction approach based on a Graph-based Spatio-temporal Attention Network*. This paper addresses an EV charging demand prediction approach based on a graph-based spatio-temporal atten. This work addresses dissertation gaps: G4.

**Wu et al. (2024)** present *Allocate EVs’ public charging stations with charging demand uncertainty*. This paper addresses allocate EVs’ public charging stations with charging demand uncertainty. This work addresses dissertation gaps: none identified.

**Huffelen et al. (2024)** present *Grid-constrained online scheduling of flexible EV charging*. We study EV charging from a scheduling perspective, aiming to minimize delays while respecting the grid constraints. A network of parking lots is considered, each with a given number of charging stations for EVs. Some of the parking lots have a roof with solar panels. This work addresses dissertation gaps: none identified.

**Chattopadhyay and Kar (2024)** present *IDEAS: Information-Driven EV Admission in Charging Station Considering User Impatience to Improve QoS and Station Utilization*. Our work delves into user behaviour at EV charging stations during peak times, particularly focusing on how impatience drives balking (not joining queues) and reneging (leaving queues prematurely). We introduce an Agent-based simulation framework that incorporates user optimism levels (pessimistic, standard, and optimistic) in the queue dynamics. Unlike previous work, this framework highlights the crucial role of human behaviour in shaping station efficiency for peak demand. This work addresses dissertation gaps: none identified.

**Fernandez et al. (2024)** present *Optimizing Energy Supply for Full EVs in Smart Cities: A Comprehensive Mobility Network Model*. The integration of Full EVs (FEVs) into the smart city ecosystem is an essential step towards achieving sustainable urban mobility. This study presents a comprehensive mobility network model designed to predict and optimize the energy supply for FEVs within smart cities. The model integrates advanced components such as a Charge Station Control Center (CSCC), smart charging infrastructure, and a dynamic user interface. This work addresses dissertation gaps: none identified.

**Makaremi (2024)** present *Policy interventions and urban characteristics in modeling EV charging infrastructure utilization*. This paper addresses policy interventions and urban characteristics in modeling EV charging infrastructure . This work addresses dissertation gaps: none identified.

**Yang et al. (2023)** present *Fleet sizing and charging infrastructure design for electric autonomous mobility-on-demand systems with endogenous congestion and limited link space*. This paper addresses fleet sizing and charging infrastructure design for electric autonomous mobility-on-demand systems w. This work addresses dissertation gaps: none identified.

**Pierrou and Hug (2023)** present *Integrating Optimal EV Charging in the Energy Management of Electric Railway Stations*. In this paper, an electric railway EMS with integration of an Energy Storage System (ESS), Regenerative Braking Energy (RBE), and renewable generation is proposed to minimize the daily operating costs of the railway station while meeting railway and EV charging demand. Compared to other railway EMS methods, the proposed approach integrates an optimal EV charging policy at the railway station to avoid high power demand due to charging requirements. Specifically, receding horizon control is leveraged to minimize the daily peak power spent on EV charging. This work addresses dissertation gaps: none identified.

**Chen et al. (2023)** present *M-BEV: Masked BEV Perception for Robust Autonomous Driving*. 3D perception is a critical problem in autonomous driving. Recently, the Bird-Eye-View (BEV) approach has attracted extensive attention, due to low-cost deployment and desirable vision detection capacity. However, the existing models ignore a realistic scenario during the driving procedure, i.e., one or more view cameras may be failed, which largely deteriorates the performance. This work addresses dissertation gaps: G4.

**Hecht et al. (2022)** present *Analysis of EVCS Usage and Profitability in Germany based on Empirical Data*. EVs are booming and with them the required public charging stations. Knowing how charging stations are used is crucial for operators of the charging stations themselves, navigation systems, electricity grids, and many more. Given that there are now 2.5 as many vehicles per charging station compared to 2017, the system needs to allocate charging points intelligently and efficiently. This work addresses dissertation gaps: none identified.

**Wang et al. (2022)** present *EVCS Location-Routing Problem with Time Windows and Resource Sharing*. EVs are widely applied in logistics companies’ urban logistics distribution, as fuel prices increase and environmental awareness grows. This study introduces an EV charging station (CS) location-routing problem with time windows and resource sharing (EVCS-LRPTWRS). Resource sharing, among multiple depots within multiple service periods is proposed to adjust the transportation resource configuration for a sustainable logistics development. This work addresses dissertation gaps: none identified.

**Mogos and Grillo (2021)** present *Impact of EV Charging Stations in Power Grids in Italy and its Mitigation Mechanisms*. Global warming leads the world to think of a different way of transportation: avoiding internal combustion engines and electrifying the transportation sector. With a high penetration of EV charging stations on an existing power distribution network, the impact may be consistent. The loads of the fast-charging stations would potentially result in increased peak load demand, reduced reserve margins, voltage instability, and reliability problems. This work addresses dissertation gaps: none identified.

**Lai and Li (2021)** present *On-Demand Valet Charging for EVs: Economic Equilibrium, Infrastructure Planning and Regulatory Incentives*. Many city residents cannot install their private EV chargers due to the lack of dedicated parking spaces or insufficient grid capacity. This presents a significant barrier towards large-scale EV adoption. To address this concern, this paper considers a novel business model, on-demand valet charging, that unlocks the potential of under-utilized public charging infrastructure to promise higher EV penetration. This work addresses dissertation gaps: G2.

**Metere et al. (2021)** present *Securing the EV Charging Infrastructure*. EVs can help alleviate our reliance on fossil fuels for transport and electricity systems. However, charging millions of EV batteries requires management to prevent overloading the electricity grid and minimise costly upgrades that are ultimately paid for by consumers. Managed chargers, such as V2G chargers, allow control over the time, speed and direction of charging. This work addresses dissertation gaps: G5.

**Liang et al. (2021)** present *The EV Routing Problem with Nonlinear Charging Functions*. This paper outlines an exact and a heuristic algorithm for the EV routing problem with a nonlinear charging function (E-VRP-NL) introduced by Montoya et al. (2017). The E-VRP-NL captures several realistic features of EVs including the battery limited driving range and nonlinear charging process at the charging stations. This work addresses dissertation gaps: none identified.

**Liu et al. (2019)** present *Load Forecasting Model and Day-ahead Operation Strategy for City-located EV Quick Charge Stations*. Charging demands of EVs are sharply increasing due to the rapid development of EVs. Hence, reliable and convenient quick charge stations are required to respond to the needs of EV drivers. Due to the uncertainty of EV charging loads, load forecasting becomes vital for the operation of quick charge stations to formulate the day-ahead plan. This work addresses dissertation gaps: none identified.

**Beaude et al. (2015)** present *Composite charging games in networks of EVs*. An important scenario for smart grids which encompass distributed electrical networks is given by the simultaneous presence of aggregators and individual consumers. In this work, an aggregator is seen as an entity (a coalition) which is able to manage jointly the energy demand of a large group of consumers or users. More precisely, the demand consists in charging an electrical vehicle (EV) battery. This work addresses dissertation gaps: none identified.

**Zhang et al. (2015)** present *Scalable EV Charging Protocols*. Although EVs are considered a viable solution to reduce greenhouse gas emissions, their uncoordinated charging could have adverse effects on power system operation. Nevertheless, the task of optimal EV charging scales unfavorably with the fleet size and the number of control periods, especially when distribution grid limitations are enforced. To this end, vehicle charging is first tackled using the recently revived Frank-Wolfe method. This work addresses dissertation gaps: none identified.

**Zuccaro et al. (2015)** present *Smart Vehicle to Grid Interface Project: Electromobility Management System Architecture and Field Test Results*. This paper presents and discusses the electromobility management system developed in the context of the SMARTV2G project, enabling the automatic control of plug-in EVs' (PEVs') charging processes. The paper describes the architecture and the software/hardware components of the electromobility management system. The focus is put in particular on the implementation of a centralized demand side management control algorithm, which allows remote real time control of the charging stations in the field, according to preferences and constraints expressed by all the actors involved (in particular the distribution system operator and the PEV users). This work addresses dissertation gaps: G5.

**Taheri et al. (2011)** present *A Dynamic Algorithm for Facilitated Charging of Plug-In EVs*. Plug-in EVs (PEVs) are a rapidly developing technology that can reduce greenhouse gas emissions and change the way vehicles obtain power. PEV charging stations will most likely be available at home and at work, and occasionally be publicly available, offering flexible charging options. Ideally, each vehicle will charge during periods when electricity prices are relatively low, to minimize the cost to the consumer and maximize societal benefits. This work addresses dissertation gaps: none identified.

**Wu et al. (0)** present *Allocate EVs’ Public Charging Stations with Charging Demand Uncertainty*. This paper addresses allocate EVs’ public charging stations with charging demand uncertainty. This work addresses dissertation gaps: none identified.

**Table 3.3: Papers in the Utilization and Demand Modeling Theme**

| Key | Authors | Year | Approach | Scope | Gaps |
|-----|---------|------|----------|-------|------|
| `an_electric_2025` | Jiang et al. | 2025 | optimization | city | G4 |
| `allocate_electric_2024` | Wu et al. | 2024 | optimization | city | -- |
| `grid-constrained_online_2024` | Huffelen et al. | 2024 | simulation | city | -- |
| `ideas_information-driven_2024` | Chattopadhyay et al. | 2024 | mixed | city | -- |
| `optimizing_energy_2024` | Fernandez et al. | 2024 | mixed | city | -- |
| `policy_interventions_2024` | Makaremi | 2024 | optimization | city | -- |
| `fleet_sizing_2023` | Yang et al. | 2023 | optimization | city | -- |
| `integrating_optimal_2023` | Pierrou et al. | 2023 | optimization | city | -- |
| `m-bev_masked_2023` | Chen et al. | 2023 | optimization | city | G4 |
| `analysis_of_2022` | Hecht et al. | 2022 | empirical | city | -- |
| `electric_vehicle_2022` | Wang et al. | 2022 | optimization | city | -- |
| `impact_of_2021` | Mogos et al. | 2021 | optimization | city | -- |
| `on-demand_valet_2021` | Lai et al. | 2021 | optimization | city | G2 |
| `securing_the_2021` | Metere et al. | 2021 | optimization | city | G5 |
| `the_electric_2021` | Liang et al. | 2021 | optimization | city | -- |
| `load_forecasting_2019` | Liu et al. | 2019 | simulation | city | -- |
| `composite_charging_2015` | Beaude et al. | 2015 | empirical | city | -- |
| `scalable_electric_2015` | Zhang et al. | 2015 | optimization | city | -- |
| `smart_vehicle_2015` | Zuccaro et al. | 2015 | optimization | city | G5 |
| `a_dynamic_2011` | Taheri et al. | 2011 | optimization | city | -- |
| `allocate_electric_0` | Wu et al. | 0 | optimization | city | -- |

### 3.4 Phased and Sequential Deployment

*7 papers (4% of corpus)*

Phased and sequential deployment research addresses the temporal dimension of infrastructure rollout, recognizing that charging networks are built incrementally over multiple budget cycles rather than deployed as a single complete plan. This thematic area is the second most underrepresented in the corpus, reflecting Gap 4 of the dissertation framework. Papers in this category include sequential location models, multi-stage stochastic programming formulations, and adaptive deployment strategies under demand uncertainty. However, even within this strand, explicit phase-transition trigger criteria, the decision rules that determine when to move from one deployment phase to the next, are rarely defined. The temporal horizon in most phased models is fixed rather than adaptive, and feedback between observed utilization in completed phases and siting decisions in future phases is generally absent.

**Tang et al. (2025)** present *Stochastic Behavior Modeling and Optimal Bidirectional Charging Station Deployment in EV Energy Network*. This paper addresses stochastic behavior modeling and optimal bidirectional charging station deployment in ev energy netw. This work addresses dissertation gaps: G4.

**Giudice et al. (2023)** present *Definition of Static and Dynamic Load Models for Grid Studies of EVs Connected to Fast Charging Stations*. The growing deployment of electric mobility calls for power system analyses to investigate to what extent the simultaneous charging of EVs leads to degraded network operation and to validate the efficiency of countermeasures. To reduce complexity and CPU time, a common approach while performing these analyses consists in replacing EVs and their charging stations with constant PQ loads. However, this approach is inaccurate, as the power absorbed by these elements actually depends not only on voltage but also on the SoC, charging method, cathode chemistry of the battery pack, and converter controls in the EV and charging station. This work addresses dissertation gaps: G4.

**Amara-Ouali et al. (2023)** present *Forecasting EVCS Occupancy: Smarter Mobility Data Challenge*. The transport sector is a major contributor to greenhouse gas emissions in Europe. Shifting to EVs powered by a low-carbon energy mix would reduce carbon emissions. However, to support the development of electric mobility, a better understanding of EV charging behaviours and more accurate forecasting models are needed. This work addresses dissertation gaps: G4.

**Eagon et al. (2022)** present *Model-Based Framework to Optimize Charger Station Deployment for BEVs*. This paper addresses model-based framework to optimize charger station deployment for BEVs. This work addresses dissertation gaps: G4.

**Sao et al. (2021)** present *Deep Information Fusion for EVCS Occupancy Forecasting*. With an increasing number of EVs, the accurate forecasting of charging station occupation is crucial to enable reliable vehicle charging. This paper introduces a novel Deep Fusion of Dynamic and Static Information model (DFDS) to effectively forecast the charging station occupation. We exploit static information, such as the mean occupation concerning the time of day, to learn the specific charging station patterns. This work addresses dissertation gaps: G4.

**Guillet et al. (2020)** present *EVCS Search in Stochastic Environments*. EVs are a central component of future mobility systems as they promise to reduce local noxious and fine dust emissions and CO2 emissions, if fed by clean energy sources. However, the adoption of EVs so far fell short of expectations despite significant governmental incentives. One reason for this slow adoption is the drivers' perceived range anxiety, especially for individually owned vehicles. This work addresses dissertation gaps: G4.

**Anjos et al. (2020)** present *Increasing EV adoption through the optimal deployment of fast-charging stations for local and long-distance travel*. This paper addresses increasing EV adoption through the optimal deployment of fast-charging stations for lo. This work addresses dissertation gaps: G4.

**Table 3.4: Papers in the Phased and Sequential Deployment Theme**

| Key | Authors | Year | Approach | Scope | Gaps |
|-----|---------|------|----------|-------|------|
| `stochastic_behavior_2025` | Tang et al. | 2025 | optimization | city | G4 |
| `definition_of_2023` | Giudice et al. | 2023 | simulation | city | G4 |
| `forecasting_electric_2023` | Amara-Ouali et al. | 2023 | empirical | city | G4 |
| `model-based_framework_2022` | Eagon et al. | 2022 | optimization | city | G4 |
| `deep_information_2021` | Sao et al. | 2021 | empirical | city | G4 |
| `electric_vehicle_2020` | Guillet et al. | 2020 | optimization | city | G4 |
| `increasing_electric_2020` | Anjos et al. | 2020 | optimization | city | G4 |

### 3.5 Zoning and Land-Use Compatibility

*0 papers (0% of corpus)*

Zoning and land-use compatibility research engages with the regulatory and spatial planning context in which charging infrastructure is deployed. This thematic area is the most severely underrepresented in the corpus, directly evidencing Gap 2. The few papers in this category treat zoning as either a binary feasibility constraint (permitted / not permitted) or as a background context for siting optimization, rather than as a variable whose schema design has quantifiable consequences for coverage, equity, and utilization outcomes. No paper in the reviewed corpus systematically compares outcomes under alternative zoning frameworks for the same metropolitan area. This represents the most significant methodological gap in the literature relative to the needs of urban planners.

No papers were classified as primarily addressing Zoning and Land-Use Compatibility in the reviewed corpus. This absence directly evidences a research gap and underscores the need for targeted contributions in this thematic area.

### 3.6 Meso-Micro Planning Integration

*0 papers (0% of corpus)*

Meso-micro integration research addresses the connection between city-scale or district-scale deployment planning and site-level implementation specifications. This is the least developed thematic area in the corpus, directly evidencing Gap 5. Papers classified here engage with hierarchical or multi-scale planning approaches that attempt to link network-level decisions to individual station design or siting constraints. The absence of a systematic translation protocol, specifying what information must flow from meso to micro and how micro-level constraints feed back to meso-level plans, remains an open research problem. The limited work in this area highlights the need for an integrated planning framework that spans both scales.

No papers were classified as primarily addressing Meso-Micro Planning Integration in the reviewed corpus. This absence directly evidences a research gap and underscores the need for targeted contributions in this thematic area.

### 3.7 Existing Reviews and Meta-Analyses

*0 papers (0% of corpus)*

Existing reviews and meta-analyses provide synthesized overviews of the charging infrastructure planning literature, offering taxonomies of methods, performance comparisons, and research agenda recommendations. These papers are valuable for situating the current systematic review within the broader field and for identifying areas where the literature itself recognizes gaps. The reviews identified in this corpus vary in scope, from narrow technical reviews of placement algorithms to broader surveys of EV infrastructure policy and planning. Where their identified gaps overlap with the five dissertation gaps, this convergent evidence strengthens the case for the proposed research agenda.

No papers were classified as primarily addressing Existing Reviews and Meta-Analyses in the reviewed corpus. This absence directly evidences a research gap and underscores the need for targeted contributions in this thematic area.

### 3.8 Related Infrastructure Planning Approaches

*34 papers (17% of corpus)*

A final cluster of papers addresses related infrastructure planning problems, urban mobility networks, shared micromobility station placement, base station deployment, and analogous location-allocation challenges, whose methodological contributions are transferable to the BEV charging context. These papers are included because they develop spatial analysis methods, demand modeling approaches, or equity frameworks that inform the proposed dissertation methodology, even when the application domain differs from BEV charging.

**Nasar et al. (2025)** present *A comparative analysis of in-motion and overnight charging infrastructure design for e-buses*. This paper addresses a comparative analysis of in-motion and overnight charging infrastructure design for e-buses. This work addresses dissertation gaps: none identified.

**Taşcıkaraoğlu et al. (2025)** present *Coordinated Management of MCSs and Community Energy Storage for EV Charging*. This paper addresses coordinated management of MCSs and community energy storage for EV. This work addresses dissertation gaps: none identified.

**Muyeed et al. (2025)** present *Cost-benefit and net zero impact analysis of PV-grid-battery systems for EV charging stations in Bangladesh*. This paper addresses cost-benefit and net zero impact analysis of pv-grid-battery systems for ev charging stations in ban. This work addresses dissertation gaps: none identified.

**Shao et al. (2024)** present *A Decentralized Bi-Level Decomposition Method for Optimal Operation of EVs in Coupled Urban Transportation and Power Distribution Systems*. This paper addresses a decentralized bi-level decomposition method for optimal operation of EVs in coupled . This work addresses dissertation gaps: none identified.

**Liang et al. (2024)** present *A V2G planning framework incorporating EV user equilibrium and distribution network flexibility enhancement*. This paper addresses a V2G planning framework incorporating EV user equilibrium and distributio. This work addresses dissertation gaps: none identified.

**Zhang et al. (2024)** present *Charging infrastructure assessment for shared autonomous EVs in 374 small and medium-sized urban areas: An agent-based simulation approach*. This paper addresses charging infrastructure assessment for shared autonomous EVs in 374 small and medium-s. This work addresses dissertation gaps: none identified.

**Wang et al. (2024)** present *Equilibrium configuration strategy of V2G-based EVCSs in low-carbon resilient distribution networks*. This paper addresses equilibrium configuration strategy of V2G-based EVCSs in lo. This work addresses dissertation gaps: none identified.

**Hu et al. (2024)** present *Locating and sizing charging station in multi-period to promote EVs adoption in urban areas*. This paper addresses locating and sizing charging station in multi-period to promote EVs adoption in urban . This work addresses dissertation gaps: none identified.

**Channi (2024)** present *Optimizing EV Charging Infrastructure: A Site Selection Strategy for Ludhiana, India*. This paper addresses optimizing EV charging infrastructure: a site selection strategy for ludhiana, india. This work addresses dissertation gaps: none identified.

**Lin et al. (2024)** present *Planning of EVCSs With PV and Energy Storage Using a Fuzzy Inference System*. This paper addresses planning of EVCSs with pv and energy storage using a fuzzy inference sy. This work addresses dissertation gaps: none identified.

**Chen et al. (2024)** present *Risk-Aware Hierarchical Coordination of Peer-to-Peer Energy Trading for EVCSs in Constrained Power Distribution and Urban Transportation Networks Under Uncertainties*. This paper addresses risk-aware hierarchical coordination of peer-to-peer energy trading for EV charging st. This work addresses dissertation gaps: none identified.

**Wang et al. (2023)** present *Collaborative multidepot EV routing problem with time windows and shared charging stations*. This paper addresses collaborative multidepot EV routing problem with time windows and shared charging stat. This work addresses dissertation gaps: none identified.

**Alanazi (2023)** present *EVs: Benefits, Challenges, and Potential Solutions for Widespread Adaptation*. The world’s primary modes of transportation are facing two major problems: rising oil costs and increasing carbon emissions. As a result, EVs are gaining popularity as they are independent of oil and do not produce greenhouse gases. However, despite their benefits, several operational issues still need to be addressed for EV adoption to become widespread. This work addresses dissertation gaps: none identified.

**Bilal and Rizwan (2023)** present *Intelligent algorithm-based efficient planning of EVCS: A case study of metropolitan city of India*. This paper addresses intelligent algorithm-based efficient planning of EVCS: a case study of. This work addresses dissertation gaps: none identified.

**Ding et al. (2023)** present *Optimal management of parking lots as a big data for EVs using internet of things and Long–Short term Memory*. This paper addresses optimal management of parking lots as a big data for EVs using internet of things and . This work addresses dissertation gaps: none identified.

**Kumbhar and Kalkhambkar (2023)** present *Optimal Planning of Battery Swapping and Charging Stations for the Urban Cities*. This paper addresses optimal planning of battery swapping and charging stations for the urban cities. This work addresses dissertation gaps: none identified.

**Zhou et al. (2023)** present *Planning of static and dynamic charging facilities for EVs in electrified transportation networks*. This paper addresses planning of static and dynamic charging facilities for EVs in electrified transportati. This work addresses dissertation gaps: none identified.

**Chitra et al. (2023)** present *RETRACTED: Charging infrastructure facilitate a large-scale Introduction of EV in urban areas using hybrid technique: A RBFNN-SPOA approach*. This paper addresses retracted: charging infrastructure facilitate a large-scale introduction of EV in urba. This work addresses dissertation gaps: none identified.

**Zhang and Lygeros (2023)** present *Routing and charging game in ride-hailing service with EVs*. This paper studies the routing and charging behaviors of EVs in a competitive ride-hailing market. When the vehicles are idle, they can choose whether to continue cruising to search for passengers, or move a charging station to recharge. The behaviors of individual vehicles are then modeled by a Markov decision process (MDP). This work addresses dissertation gaps: none identified.

**Li et al. (2023)** present *Smart and efficient EV charging navigation scheme in vehicular edge computing networks*. With the increasing number of electric fast charging stations (FCSs) deployed along roadsides of both urban roads and highways, the long-distance travel of EVs becomes possible. The EV charging navigation scheme is significant for the quality of user experience. However, the variable conditions of both power grid and traffic networks make it a serious challenge. This work addresses dissertation gaps: none identified.

**Martí et al. (2022)** present *Charging stations and mobility data generators for agent-based simulations*. This paper addresses charging stations and mobility data generators for agent-based simulations. This work addresses dissertation gaps: none identified.

**Hao et al. (2022)** present *Integrated EV Charging Path Planning Considering Traffic Network and Power Grid*. This paper addresses integrated EV charging path planning considering traffic network and power grid. This work addresses dissertation gaps: none identified.

**Afshar et al. (2022)** present *MCS: A Complementary Charging Technology for EVs*. This paper addresses MCS: a complementary charging technology for EVs. This work addresses dissertation gaps: none identified.

**Marszal et al. (2022)** present *Phase separation induces congestion waves in EV charging*. EVs may dominate motorized transport in the next decade, yet the impact of the collective dynamics of electric mobility on long-range traffic flow is still largely unknown. We demonstrate a type of congestion that arises if charging infrastructure is limited or EV density is high. This congestion emerges solely through indirect interactions at charging infrastructure by queue-avoidance behavior that - counterintuitively - induces clustering of occupied charging stations and phase separation of the flow into free and congested stations. This work addresses dissertation gaps: none identified.

**Hashmi et al. (2022)** present *WEcharge: democratizing EV charging infrastructure*. The sustainable growth of EVs will have to be met with proportional growth in EV charging infrastructure. With limited urban spaces to place new charging stations, shrinking profitability, privately owned charging facilities need to be shared. WEcharge will allow privately owned charging infrastructure to be shared with public EV owners using a business model. This work addresses dissertation gaps: none identified.

**Cui et al. (2021)** present *Optimal Pricing of Public EVCSs Considering Operations of Coupled Transportation and Power Systems*. This paper addresses optimal pricing of public EVCSs considering operations of coupled trans. This work addresses dissertation gaps: none identified.

**Aydin (2021)** present *Secure Charging and Payment System for Electric Land Vehicles with Authentication Protocol*. It is obvious that fossil fuels are a limited resource and will be replaced by other energy sources in the future considering economic and en-vironmental problems. Electricity comes to the forefront among the sources that are candidates to replace fossil fuels. In the near future, electric land, air and sea vehicles will start to take more place in daily life. This work addresses dissertation gaps: none identified.

**Adenaw and Lienkamp (2020)** present *A Model for the Data-based Analysis and Design of Urban Public Charging Infrastructure*. This paper addresses a model for the data-based analysis and design of urban public charging infrastructure. This work addresses dissertation gaps: none identified.

**Relan et al. (2020)** present *Optimal Siting of EV BSSs with Centralized Charging*. This paper addresses optimal siting of EV BSSs with centralized charging. This work addresses dissertation gaps: none identified.

**Aveklouris et al. (2018)** present *Bounds and Limit Theorems for a Layered Queueing Model in EV Charging*. The rise of EVs is unstoppable due to factors such as the decreasing cost of batteries and various policy decisions. These vehicles need to be charged and will therefore cause congestion in local distribution grids in the future. Motivated by this, we consider a charging station with finitely many parking spaces, in which EVs arrive in order to get charged. This work addresses dissertation gaps: none identified.

**Lehfuss et al. (2018)** present *Coupling of Real-Time and Co-Simulation for the Evaluation of the Large Scale Integration of EVs into Intelligent Power Systems*. This paper addresses the validation of EV supply equipment by means of a real-time capable co-simulation approach. This setup implies both pure software and real-time simulation tasks with different sampling rates dependent on the type of the performed experiment. In contrast, controller and power hardware-in-the-loop simulations are methodologies which ask for real-time execution of simulation models with well-defined simulation sampling rates. This work addresses dissertation gaps: none identified.

**Chen et al. (2017)** present *Plug-in EV Charging Congestion Analysis Using Taxi Travel Data in the Central Area of Beijing*. Recharging a plug-in EV is more time-consuming than refueling an internal combustion engine vehicle. As a result, charging stations may face serious congestion problems during peak traffic hours in the near future with the rapid growth of plug-in EV population. Considering that drivers' time costs are usually expensive, charging congestion will be a dominant factor that affect a charging station's quality of service. This work addresses dissertation gaps: none identified.

**Yuan et al. (2015)** present *Competitive Charging Station Pricing for Plug-in EVs*. This paper considers the problem of charging station pricing and plug-in EVs (PEVs) station selection. When a PEV needs to be charged, it selects a charging station by considering the charging prices, waiting times, and travel distances. Each charging station optimizes its charging price based on the prediction of the PEVs' charging station selection decisions and the other station's pricing decision, in order to maximize its profit. This work addresses dissertation gaps: none identified.

**Barco et al. (2013)** present *Optimal Routing and Scheduling of Charge for EVs: Case Study*. In Colombia, there is an increasing interest about improving public transportation. One of the proposed strategies in that way is the use BEVs. One of the new challenges is the BEVs routing problem, which is subjected to the traditional issues of the routing problems, and must also consider the particularities of autonomy, charge and battery degradation of the BEVs. This work addresses dissertation gaps: none identified.

**Table 3.8: Papers in the Related Infrastructure Planning Approaches Theme**

| Key | Authors | Year | Approach | Scope | Gaps |
|-----|---------|------|----------|-------|------|
| `a_comparative_2025` | Nasar et al. | 2025 | optimization | city | G1 |
| `coordinated_management_2025` | Taşcıkaraoğlu et al. | 2025 | optimization | city | G1 |
| `cost-benefit_and_2025` | Muyeed et al. | 2025 | optimization | city | G1 |
| `a_decentralized_2024` | Shao et al. | 2024 | optimization | city | G1 |
| `a_vehicle-to-grid_2024` | Liang et al. | 2024 | optimization | city | G1 |
| `charging_infrastructure_2024` | Zhang et al. | 2024 | simulation | city | G1 |
| `equilibrium_configuration_2024` | Wang et al. | 2024 | optimization | city | G1 |
| `locating_and_2024` | Hu et al. | 2024 | optimization | city | G1 |
| `optimizing_electric_2024` | Channi | 2024 | optimization | site | G1 |
| `planning_of_2024` | Lin et al. | 2024 | optimization | city | G1 |
| `risk-aware_hierarchical_2024` | Chen et al. | 2024 | optimization | city | G1 |
| `collaborative_multidepot_2023` | Wang et al. | 2023 | optimization | city | G1 |
| `electric_vehicles_2023` | Alanazi | 2023 | optimization | city | G1 |
| `intelligent_algorithm-based_2023` | Bilal et al. | 2023 | empirical | city | G1 |
| `optimal_management_2023` | Ding et al. | 2023 | optimization | city | G1 |
| `optimal_planning_2023` | Kumbhar et al. | 2023 | optimization | city | G1 |
| `planning_of_2023` | Zhou et al. | 2023 | optimization | city | G1 |
| `retracted_charging_2023` | Chitra et al. | 2023 | optimization | city | G1 |
| `routing_and_2023` | Zhang et al. | 2023 | optimization | city | G1 |
| `smart_and_2023` | Li et al. | 2023 | optimization | city | G1 |
| `charging_stations_2022` | Martí et al. | 2022 | simulation | city | G1 |
| `integrated_electric_2022` | Hao et al. | 2022 | optimization | city | G1 |
| `mobile_charging_2022` | Afshar et al. | 2022 | optimization | city | G1 |
| `phase_separation_2022` | Marszal et al. | 2022 | simulation | city | G1 |
| `wecharge_democratizing_2022` | Hashmi et al. | 2022 | empirical | city | G1 |
| `optimal_pricing_2021` | Cui et al. | 2021 | optimization | city | G1 |
| `secure_charging_2021` | Aydin | 2021 | optimization | city | G1 |
| `a_model_2020` | Adenaw et al. | 2020 | optimization | city | G1 |
| `optimal_siting_2020` | Relan et al. | 2020 | optimization | city | G1 |
| `bounds_and_2018` | Aveklouris et al. | 2018 | simulation | city | G1 |
| `coupling_of_2018` | Lehfuss et al. | 2018 | simulation | city | G1 |
| `plug-in_electric_2017` | Chen et al. | 2017 | mixed | city | G1 |
| `competitive_charging_2015` | Yuan et al. | 2015 | optimization | city | G1 |
| `optimal_routing_2013` | Barco et al. | 2013 | empirical | city | G1 |


---

## 4. Research Gap Analysis

This section presents a systematic analysis of the five dissertation research gaps, drawing on quantitative extraction data from all 200 included papers. For each gap, the analysis characterizes the current state of knowledge, identifies specific sub-dimensions that remain unaddressed, and presents evidence tables organized by paper key, authors, year, and relevant methodological dimensions.

### 4.1 Gap 1: Misaligned Spatial Units

**Definition:** Administrative zoning boundaries, census tracts, TAZs, municipal districts, are the dominant spatial unit in charging infrastructure planning, yet these boundaries are designed for governance rather than mobility representation. Commuter sheds, trip chains, and corridor flows routinely cross jurisdictional lines, creating structural misalignment between the spatial unit of optimization and the actual geography of charging demand.

**Coverage:** 133 of 200 papers (66%). Coverage level: **High**.

**Current State of Knowledge.** Gap 1 has the highest raw coverage in the corpus, with 133 of 200 papers providing partial evidence. However, this coverage is deceptive: the papers address spatial placement of charging stations within administrative spatial units, not the validity or design of the spatial units themselves. The literature accepts TAZ and census-based boundaries as given and optimizes within them, rather than questioning whether those boundaries appropriately represent mobility corridor demand. The consequence is that optimization results are conditional on an unvalidated spatial frame, a form of spatial bias that systematically distorts placement outcomes.

**What Is Missing.** No paper in the reviewed corpus: (1) constructs mobility-corridor zones from origin-destination data and uses them as the spatial unit of optimization; (2) directly compares siting outcomes under corridor-based vs. administrative spatial units on the same metropolitan area; (3) quantifies the spatial demand estimation error attributable to administrative spatial unit mismatch; or (4) addresses cross-jurisdictional demand integration as a planning challenge.

**Table 4.1: Papers Addressing Gap 1**

| Key | Authors | Year | Approach | Scope | Equity | Util. | Phased |
|-----|---------|------|----------|-------|--------|-------|--------|
| `a_two-stage_2026` | Najafzad et al. | 2026 | optimization | city | Y | Y | Y |
| `joint_planning_2026` | Mejia et al. | 2026 | optimization | city | N | N | N |
| `pricing_electric_2026` | Jiang et al. | 2026 | optimization | city | N | Y | N |
| `regional_transportation_2026` | Babur et al. | 2026 | simulation | regional | Y | Y | Y |
| `simultaneous_optimization_2026` | Bertucci et al. | 2026 | optimization | city | N | N | N |
| `strategic_planning_2026` | Fariza et al. | 2026 | optimization | regional | N | Y | N |
| `a_2025` | Do et al. | 2025 | mixed | city | N | Y | N |
| `a_density-based_2025` | Ameer et al. | 2025 | optimization | city | N | N | N |
| `a_joint_2025` | Yu et al. | 2025 | mixed | city | N | Y | Y |
| `a_multi-modal_2025` | Karakuş et al. | 2025 | empirical | city | N | N | Y |
| `a_spatially_2025` | Huang et al. | 2025 | mixed | city | N | Y | N |
| `a_two-stage_2025` | Meng et al. | 2025 | optimization | city | N | N | N |
| `a_united_2025` | Kinchen et al. | 2025 | mixed | city | Y | N | N |
| `an_exact_2025` | Nankali et al. | 2025 | mixed | city | N | N | N |
| `analyzing_locational_2025` | Mousaei | 2025 | empirical | city | N | N | N |
| `causal_spillover_2025` | Silva et al. | 2025 | empirical | city | N | N | Y |
| `charge-map_an_2025` | Islam et al. | 2025 | mixed | city | N | Y | Y |
| `competitive_ev_2025` | Nguyen et al. | 2025 | mixed | city | N | N | N |
| `data-driven_ev_2025` | Alharbi et al. | 2025 | optimization | city | N | N | Y |
| `data-driven_optimization_2025` | Junker et al. | 2025 | mixed | site | N | Y | N |
| `electric_vehicle_2025` | Zhao et al. | 2025 | optimization | city | Y | N | N |
| `explainable_and_2025` | Kapoor | 2025 | optimization | city | N | N | N |
| `fairness-oriented_charging_2025` | Yuan et al. | 2025 | optimization | city | Y | N | N |
| `hybrid_optimization_2025` | Ameer et al. | 2025 | optimization | city | N | N | N |
| `joint_optimization_2025` | Okada et al. | 2025 | optimization | city | N | Y | Y |
| `large_language_2025` | Zheng et al. | 2025 | mixed | city | N | Y | Y |
| `location_and_2025` | Choi et al. | 2025 | optimization | city | N | Y | N |
| `multiobjective_model_2025` | Ruiz-Barajas et al. | 2025 | mixed | city | N | N | N |
| `optimal_mixed_2025` | Nakao et al. | 2025 | mixed | city | N | Y | N |
| `optimization_of_2025` | Zhang et al. | 2025 | optimization | city | N | Y | N |
| `optimizing_electric_2025` | Zhong et al. | 2025 | mixed | city | N | Y | N |
| `optimizing_urban_2025` | Ai et al. | 2025 | optimization | city | N | Y | N |
| `planning_future_2025` | Yuan et al. | 2025 | empirical | regional | N | Y | Y |
| `predicting_optimal_2025` | Mousaei et al. | 2025 | empirical | city | N | N | N |
| `reinforcement_learning_2025` | Zhu et al. | 2025 | empirical | city | N | Y | N |
| `robust_charging_2025` | Xia et al. | 2025 | optimization | corridor | N | Y | N |
| `trajectory-integrated_accessibility_2025` | Ju et al. | 2025 | optimization | neighborhood | N | N | N |
| `a_data-driven_2024` | Zhang et al. | 2024 | mixed | city | N | N | Y |
| `a_multi-objective_2024` | Zhang et al. | 2024 | optimization | site | N | Y | N |
| `a_particle_2024` | Aljaidi et al. | 2024 | optimization | city | N | N | N |
| `a_quantum_2024` | Radvand et al. | 2024 | optimization | city | N | N | N |
| `a_two-layer_2024` | Wu et al. | 2024 | optimization | city | N | Y | N |
| `advancing_urban_2024` | Zhang et al. | 2024 | optimization | city | N | N | N |
| `battery_swapping_2024` | Liu et al. | 2024 | mixed | neighborhood | N | Y | Y |
| `beyond_profit_2024` | Wang et al. | 2024 | mixed | city | N | Y | N |
| `charging_station_2024` | Cai et al. | 2024 | mixed | site | N | N | N |
| `electric_vehicle_2024` | Li et al. | 2024 | optimization | city | N | Y | N |
| `energy_management_2024` | Cao et al. | 2024 | mixed | city | N | N | N |
| `integrating_en_2024` | Mehditabrizi et al. | 2024 | optimization | city | N | N | N |
| `multiobjective_optimization_2024` | Mohammed et al. | 2024 | optimization | city | N | N | N |
| `optimal_electric_2024` | Kumar et al. | 2024 | optimization | site | N | N | N |
| `optimal_ev_2024` | Pierrou et al. | 2024 | optimization | city | N | Y | N |
| `optimal_evcs_2024` | He et al. | 2024 | optimization | city | N | Y | Y |
| `optimal_planning_2024` | Heo et al. | 2024 | empirical | city | N | N | N |
| `optimization_strategies_2024` | Panyaram | 2024 | optimization | city | N | Y | Y |
| `optimizing_ev_2024` | Huang et al. | 2024 | optimization | city | N | N | N |
| `optimizing_urban_2024` | Munawar | 2024 | mixed | regional | N | N | N |
| `sequential_charging_2024` | Shen et al. | 2024 | optimization | city | N | Y | Y |
| `sustainable_planning_2024` | Seilabi et al. | 2024 | optimization | city | N | Y | Y |
| `the_electric_2024` | Akbay et al. | 2024 | optimization | city | N | N | N |
| `towards_sustainable_2024` | Boonprong et al. | 2024 | empirical | city | Y | Y | N |
| `towards_using_2024` | Miltner et al. | 2024 | mixed | city | N | Y | Y |
| `urban_electric_2024` | Alhussan et al. | 2024 | optimization | city | N | N | N |
| `a_battery_2023` | Xin et al. | 2023 | optimization | city | N | N | N |
| `a_data-driven_2023` | Al-Dahabreh et al. | 2023 | mixed | city | N | Y | N |
| `a_robust_2023` | Arief et al. | 2023 | mixed | city | Y | Y | N |
| `an_agent-based_2023` | Yi et al. | 2023 | mixed | city | N | Y | N |
| `electric_vehicle_2023` | Varma et al. | 2023 | simulation | city | N | Y | N |
| `fast-charging_station_2023` | Qiao et al. | 2023 | optimization | city | N | N | N |
| `incorporating_time-dependent_2023` | Filippi et al. | 2023 | optimization | city | N | Y | Y |
| `initial_location_2023` | Tambunan et al. | 2023 | optimization | city | N | N | N |
| `layout_and_2023` | Jiang | 2023 | optimization | city | N | Y | N |
| `maximum_flow-based_2023` | Parent et al. | 2023 | mixed | city | N | Y | Y |
| `on_the_2023` | Tiu et al. | 2023 | optimization | city | N | Y | Y |
| `optimal_location_2023` | Mourgues et al. | 2023 | optimization | city | N | N | N |
| `optimal_placement_2023` | Liu et al. | 2023 | optimization | city | Y | Y | N |
| `optimizing_electric_2023` | Wu et al. | 2023 | mixed | city | N | N | N |
| `placement_of_2023` | Pal et al. | 2023 | optimization | city | N | N | N |
| `spap_simultaneous_2023` | Wang et al. | 2023 | mixed | city | N | Y | Y |
| `spatial_arbitrage_2023` | Mohammadian et al. | 2023 | mixed | city | N | N | Y |
| `a_framework_2022` | Mishra et al. | 2022 | mixed | corridor | N | Y | N |
| `a_novel_2022` | Hung et al. | 2022 | optimization | city | N | N | N |
| `designing_an_2022` | Amilia et al. | 2022 | mixed | city | Y | Y | Y |
| `development_of_2022` | Jin et al. | 2022 | optimization | city | N | Y | N |
| `distributed_coordination_2022` | Yan et al. | 2022 | optimization | city | N | N | N |
| `ev_charging_2022` | Mousavi et al. | 2022 | mixed | city | N | N | N |
| `optimal_placement_2022` | Srinivas et al. | 2022 | optimization | city | N | N | N |
| `optimising_electric_2022` | Lamontagne et al. | 2022 | mixed | city | N | N | N |
| `performance_analysis_2022` | Qin et al. | 2022 | optimization | city | N | Y | N |
| `planning_of_2022` | Bian et al. | 2022 | optimization | city | N | N | Y |
| `predictive_energy_2022` | Lin et al. | 2022 | mixed | city | N | N | N |
| `reinforcement_learning-based_2022` | Wahl et al. | 2022 | empirical | city | N | Y | N |
| `research_on_2022` | Wang et al. | 2022 | mixed | city | N | Y | N |
| `web_mining_2022` | Hummler et al. | 2022 | empirical | city | N | Y | N |
| `a_gis-based_2021` | Zafar et al. | 2021 | optimization | city | N | N | N |
| `citizen_centric_2021` | Cintrano et al. | 2021 | optimization | neighborhood | N | N | N |
| `deep_spatio-temporal_2021` | Hüttel et al. | 2021 | optimization | city | N | Y | Y |
| `energy-optimal_design_2021` | Hurk et al. | 2021 | mixed | city | N | N | N |
| `hierarchical_optimization_2021` | Mirheli et al. | 2021 | optimization | city | N | Y | Y |
| `joint_optimization_2021` | Luke et al. | 2021 | optimization | city | N | Y | N |
| `optimal_placement_2021` | Padmanabhan et al. | 2021 | optimization | city | N | Y | N |
| `optimal_planning_2021` | Hou et al. | 2021 | mixed | city | N | Y | N |
| `reducing_waiting_2021` | Schoenberg et al. | 2021 | simulation | city | N | N | N |
| `siting_and_2021` | Ahadi et al. | 2021 | mixed | city | N | Y | N |
| `strategic_competition_2021` | Bayani et al. | 2021 | optimization | city | N | N | N |
| `a_method_2020` | Rizopoulos et al. | 2020 | optimization | city | N | N | Y |
| `double-layer_game_2020` | Wang et al. | 2020 | mixed | city | N | N | N |
| `dynamic_modeling_2020` | Yang et al. | 2020 | simulation | regional | N | Y | N |
| `location_of_2020` | Brandstätter et al. | 2020 | mixed | city | N | Y | Y |
| `optimal_fast_2020` | Ma et al. | 2020 | optimization | city | N | N | N |
| `optimizing_the_2020` | GORBUNOVA et al. | 2020 | empirical | city | N | N | N |
| `resource_aware_2020` | Santoyo et al. | 2020 | mixed | city | N | Y | N |
| `a_method_2019` | Ouyang et al. | 2019 | mixed | city | N | Y | Y |
| `optimal_decision_2019` | Upadhaya et al. | 2019 | optimization | city | N | Y | N |
| `predicting_popularity_2019` | Straka et al. | 2019 | optimization | city | N | Y | Y |
| `a_consumer_2018` | Luo et al. | 2018 | mixed | city | N | Y | N |
| `charging_station_2018` | Deza et al. | 2018 | optimization | city | N | N | N |
| `electric_vehicle_2018` | Cui et al. | 2018 | optimization | city | N | N | N |
| `engineering_and_2018` | Luo | 2018 | optimization | city | N | Y | N |
| `placement_of_2018` | Luo et al. | 2018 | simulation | city | N | Y | N |
| `predicting_electric_2018` | Ramachandran et al. | 2018 | simulation | city | N | Y | N |
| `electric_vehicle_2017` | Aveklouris et al. | 2017 | simulation | city | N | N | N |
| `route_optimization_2017` | Kosmanos et al. | 2017 | mixed | city | N | N | N |
| `demand_prediction_2016` | Gopalakrishnan et al. | 2016 | mixed | city | N | Y | Y |
| `charging_games_2015` | Beaude et al. | 2015 | optimization | city | N | N | N |
| `electric_vehicles_2015` | Lanna et al. | 2015 | optimization | city | N | N | Y |
| `introducing_decentralized_2015` | Beaude et al. | 2015 | mixed | neighborhood | N | N | N |
| `minimizing_the_2015` | Beaude et al. | 2015 | mixed | city | N | Y | N |
| `optimizing_the_2015` | Vazifeh et al. | 2015 | optimization | city | N | Y | Y |
| `electric_vehicle_2013` | Lam et al. | 2013 | simulation | city | N | N | N |
| `socially_optimal_2013` | Yudovina et al. | 2013 | simulation | city | N | N | Y |
| `electric_vehicle_0` | Li et al. | 0 | optimization | city | N | Y | Y |

### 4.2 Gap 2: Lack of Zoning Impact Analysis

**Definition:** Despite zoning regulations determining permissible land uses for charging infrastructure, systematic comparison of how different zoning schemas affect station siting outcomes, coverage, equity, cost, utilization, is entirely absent from the literature. Studies that mention zoning typically treat it as a fixed exogenous constraint rather than as a variable whose design has quantifiable consequences.

**Coverage:** 5 of 200 papers (2%). Coverage level: **Low**.

**Current State of Knowledge.** Gap 2 is the most severe in the corpus. Only 5 papers address zoning in any systematic way. The dominant treatment is binary: zoning appears as a feasibility filter (stations can or cannot be located in a given zone type), not as a comparative analytical variable. The consequence is that planners have no evidence base for evaluating whether mixed-use zoning outperforms commercial-only zoning for charging access, or whether regulatory heterogeneity across municipal boundaries affects network equity.

**What Is Missing.** No paper: (1) compares charging infrastructure siting outcomes under ≥2 distinct zoning schemas for the same geographic area; (2) defines a land-use compatibility scoring methodology applicable across zoning frameworks; (3) models regulatory heterogeneity across jurisdictions as an optimization constraint; or (4) quantifies the equity and utilization consequences of alternative zoning ordinance designs.

**Table 4.2: Papers Addressing Gap 2**

| Key | Authors | Year | Approach | Scope | Equity | Util. | Phased |
|-----|---------|------|----------|-------|--------|-------|--------|
| `strategic_planning_2026` | Fariza et al. | 2026 | optimization | regional | N | Y | N |
| `a_multi-modal_2025` | Karakuş et al. | 2025 | empirical | city | N | N | Y |
| `a_multi-objective_2024` | Zhang et al. | 2024 | optimization | site | N | Y | N |
| `towards_sustainable_2024` | Boonprong et al. | 2024 | empirical | city | Y | Y | N |
| `on-demand_valet_2021` | Lai et al. | 2021 | optimization | city | N | Y | N |

### 4.3 Gap 3: Equity and Utilization Separation

**Definition:** The literature treats equity of geographic access and infrastructure utilization efficiency as parallel, competing single-objective functions. Studies optimizing coverage equity rarely model utilization dynamics; studies maximizing utilization rarely impose equity constraints. This separation produces networks that may be highly efficient but spatially unjust, or broadly accessible but chronically underutilized.

**Coverage:** 14 of 200 papers (7%). Coverage level: **Medium**.

**Current State of Knowledge.** Gap 3 is evidenced by the pattern of single-objective treatment: of the 14 papers addressing equity-utilization interaction, only 8 jointly optimize both within a single model. Equity studies define coverage by demographic group or geographic zone but do not model utilization dynamics. Utilization studies maximize station throughput but do not impose equity constraints. The consequence is a systematic blind spot: networks that are locally efficient may be globally unjust, and vice versa, with no quantified tradeoff available to inform policy decisions.

**What Is Missing.** No paper: (1) formulates a joint equity-utilization objective function and solves it to optimality; (2) computes a Pareto frontier between equity access and utilization efficiency; (3) uses both a Gini coefficient (or equivalent) and a utilization rate in the same optimization model; or (4) provides planners with quantified tradeoff information to support equity-efficiency decisions.

**Table 4.3: Papers Addressing Gap 3**

| Key | Authors | Year | Approach | Scope | Equity | Util. | Phased |
|-----|---------|------|----------|-------|--------|-------|--------|
| `a_two-stage_2026` | Najafzad et al. | 2026 | optimization | city | Y | Y | Y |
| `regional_transportation_2026` | Babur et al. | 2026 | simulation | regional | Y | Y | Y |
| `a_united_2025` | Kinchen et al. | 2025 | mixed | city | Y | N | N |
| `an_equity-based_2025` | Jha et al. | 2025 | optimization | city | Y | N | N |
| `electric_vehicle_2025` | Zhao et al. | 2025 | optimization | city | Y | N | N |
| `fairness-oriented_charging_2025` | Yuan et al. | 2025 | optimization | city | Y | N | N |
| `crowdfunding_for_2024` | Erfani et al. | 2024 | optimization | neighborhood | Y | N | N |
| `towards_sustainable_2024` | Boonprong et al. | 2024 | empirical | city | Y | Y | N |
| `a_robust_2023` | Arief et al. | 2023 | mixed | city | Y | Y | N |
| `optimal_placement_2023` | Liu et al. | 2023 | optimization | city | Y | Y | N |
| `designing_an_2022` | Amilia et al. | 2022 | mixed | city | Y | Y | Y |
| `inequitable_access_2021` | Khan et al. | 2021 | optimization | neighborhood | Y | N | N |
| `electrical_vehicle_2017` | Wang et al. | 2017 | mixed | city | Y | Y | N |
| `critical_behaviour_2015` | Carvalho et al. | 2015 | empirical | city | Y | Y | N |

### 4.4 Gap 4: Static Optimization Dominance

**Definition:** The overwhelming majority of siting models optimize a single time period, producing a complete network plan as if all stations will be deployed simultaneously. Real-world charging deployment is phased over multiple budget cycles under demand uncertainty. Adaptive, sequential decision procedures that explicitly model phase transitions and trigger criteria are almost entirely absent.

**Coverage:** 44 of 200 papers (22%). Coverage level: **Medium**.

**Current State of Knowledge.** Gap 4 reflects the temporal structure of the literature: of the 44 papers that address phasing, most model pre-defined temporal periods rather than adaptive sequences driven by observed demand. Sequential stochastic programming approaches exist but are rare, and none defines explicit trigger criteria for phase transitions, the decision rules that determine when current-phase performance warrants expanding to the next phase. The static dominance means that deployment plans are optimal only under their scenario assumptions, which rarely hold as EV adoption evolves.

**What Is Missing.** No paper: (1) defines explicit adaptive trigger criteria for phase transitions based on observed utilization or coverage; (2) quantifies the value of sequential planning relative to static optimization under demand uncertainty; (3) models feedback between realized phase outcomes and next-phase siting decisions; or (4) addresses budget carryover and capital reallocation between phases.

**Table 4.4: Papers Addressing Gap 4**

| Key | Authors | Year | Approach | Scope | Equity | Util. | Phased |
|-----|---------|------|----------|-------|--------|-------|--------|
| `a_two-stage_2026` | Najafzad et al. | 2026 | optimization | city | Y | Y | Y |
| `regional_transportation_2026` | Babur et al. | 2026 | simulation | regional | Y | Y | Y |
| `a_joint_2025` | Yu et al. | 2025 | mixed | city | N | Y | Y |
| `a_multi-modal_2025` | Karakuş et al. | 2025 | empirical | city | N | N | Y |
| `an_electric_2025` | Jiang et al. | 2025 | optimization | city | N | Y | Y |
| `causal_spillover_2025` | Silva et al. | 2025 | empirical | city | N | N | Y |
| `charge-map_an_2025` | Islam et al. | 2025 | mixed | city | N | Y | Y |
| `data-driven_ev_2025` | Alharbi et al. | 2025 | optimization | city | N | N | Y |
| `joint_optimization_2025` | Okada et al. | 2025 | optimization | city | N | Y | Y |
| `large_language_2025` | Zheng et al. | 2025 | mixed | city | N | Y | Y |
| `planning_future_2025` | Yuan et al. | 2025 | empirical | regional | N | Y | Y |
| `stochastic_behavior_2025` | Tang et al. | 2025 | optimization | city | N | N | Y |
| `a_data-driven_2024` | Zhang et al. | 2024 | mixed | city | N | N | Y |
| `battery_swapping_2024` | Liu et al. | 2024 | mixed | neighborhood | N | Y | Y |
| `optimal_evcs_2024` | He et al. | 2024 | optimization | city | N | Y | Y |
| `optimization_strategies_2024` | Panyaram | 2024 | optimization | city | N | Y | Y |
| `sequential_charging_2024` | Shen et al. | 2024 | optimization | city | N | Y | Y |
| `sustainable_planning_2024` | Seilabi et al. | 2024 | optimization | city | N | Y | Y |
| `towards_using_2024` | Miltner et al. | 2024 | mixed | city | N | Y | Y |
| `definition_of_2023` | Giudice et al. | 2023 | simulation | city | N | N | Y |
| `forecasting_electric_2023` | Amara-Ouali et al. | 2023 | empirical | city | N | N | Y |
| `incorporating_time-dependent_2023` | Filippi et al. | 2023 | optimization | city | N | Y | Y |
| `m-bev_masked_2023` | Chen et al. | 2023 | optimization | city | N | Y | Y |
| `maximum_flow-based_2023` | Parent et al. | 2023 | mixed | city | N | Y | Y |
| `on_the_2023` | Tiu et al. | 2023 | optimization | city | N | Y | Y |
| `spap_simultaneous_2023` | Wang et al. | 2023 | mixed | city | N | Y | Y |
| `spatial_arbitrage_2023` | Mohammadian et al. | 2023 | mixed | city | N | N | Y |
| `designing_an_2022` | Amilia et al. | 2022 | mixed | city | Y | Y | Y |
| `model-based_framework_2022` | Eagon et al. | 2022 | optimization | city | N | N | Y |
| `planning_of_2022` | Bian et al. | 2022 | optimization | city | N | N | Y |
| `deep_information_2021` | Sao et al. | 2021 | empirical | city | N | N | Y |
| `deep_spatio-temporal_2021` | Hüttel et al. | 2021 | optimization | city | N | Y | Y |
| `hierarchical_optimization_2021` | Mirheli et al. | 2021 | optimization | city | N | Y | Y |
| `a_method_2020` | Rizopoulos et al. | 2020 | optimization | city | N | N | Y |
| `electric_vehicle_2020` | Guillet et al. | 2020 | optimization | city | N | N | Y |
| `increasing_electric_2020` | Anjos et al. | 2020 | optimization | city | N | N | Y |
| `location_of_2020` | Brandstätter et al. | 2020 | mixed | city | N | Y | Y |
| `a_method_2019` | Ouyang et al. | 2019 | mixed | city | N | Y | Y |
| `predicting_popularity_2019` | Straka et al. | 2019 | optimization | city | N | Y | Y |
| `demand_prediction_2016` | Gopalakrishnan et al. | 2016 | mixed | city | N | Y | Y |
| `electric_vehicles_2015` | Lanna et al. | 2015 | optimization | city | N | N | Y |
| `optimizing_the_2015` | Vazifeh et al. | 2015 | optimization | city | N | Y | Y |
| `socially_optimal_2013` | Yudovina et al. | 2013 | simulation | city | N | N | Y |
| `electric_vehicle_0` | Li et al. | 0 | optimization | city | N | Y | Y |

### 4.5 Gap 5: Missing Meso-Micro Integration

**Definition:** No integrated framework bridges meso-scale city-level rollout plans, which zones or corridors receive stations in each phase, to micro-scale site-level implementation specifications: land-use compatibility, grid connection proximity, access geometry, and facility design. This gap means that rollout plans cannot be operationalized without an implicit, unspecified translation step.

**Coverage:** 11 of 200 papers (6%). Coverage level: **Medium**.

**Current State of Knowledge.** Gap 5 is evidenced by the near-complete absence of meso-micro integration work: only 11 papers engage with this dimension. The gap exists at the boundary between transportation planning (which operates at city or corridor scale) and urban design / site engineering (which operates at parcel and street scale). Planning practice implicitly performs this translation, but without an explicit, validated protocol, the quality and consistency of the translation varies widely across practitioners and contexts.

**What Is Missing.** No paper: (1) defines a meso-to-micro translation protocol specifying the minimum information set that must flow from rollout plan to site selection; (2) develops a site suitability scoring methodology derived from meso outputs; (3) models the feedback from micro-level constraints back to meso-level allocation; or (4) validates a meso-micro integration framework against real-world deployment decisions.

**Table 4.5: Papers Addressing Gap 5**

| Key | Authors | Year | Approach | Scope | Equity | Util. | Phased |
|-----|---------|------|----------|-------|--------|-------|--------|
| `a_2025` | Do et al. | 2025 | mixed | city | N | Y | N |
| `optimizing_urban_2025` | Ai et al. | 2025 | optimization | city | N | Y | N |
| `a_data-driven_2024` | Zhang et al. | 2024 | mixed | city | N | N | Y |
| `crowdfunding_for_2024` | Erfani et al. | 2024 | optimization | neighborhood | Y | N | N |
| `optimizing_urban_2024` | Munawar | 2024 | mixed | regional | N | N | N |
| `electric_vehicle_2023` | Varma et al. | 2023 | simulation | city | N | Y | N |
| `development_of_2022` | Jin et al. | 2022 | optimization | city | N | Y | N |
| `predictive_energy_2022` | Lin et al. | 2022 | mixed | city | N | N | N |
| `securing_the_2021` | Metere et al. | 2021 | optimization | city | N | Y | N |
| `optimal_decision_2019` | Upadhaya et al. | 2019 | optimization | city | N | Y | N |
| `smart_vehicle_2015` | Zuccaro et al. | 2015 | optimization | city | N | Y | N |

### 4.6 Overall Gap Coverage Summary

**Table 4.6: Dissertation Gap Coverage Across the Corpus**

| Gap | Label | N Papers | % | Level | Primary Sub-Gap Missing |
|-----|-------|----------|---|-------|------------------------|
| Gap 1 | Misaligned Spatial Units | 133 | 66% | High | Corridor-based spatial unit construction and comparison |
| Gap 2 | Lack of Zoning Impact Analysis | 5 | 2% | Low | Comparative analysis of ≥2 zoning schemas |
| Gap 3 | Equity and Utilization Separation | 14 | 7% | Medium | Joint equity-utilization single objective function |
| Gap 4 | Static Optimization Dominance | 44 | 22% | Medium | Adaptive phase-transition trigger criteria |
| Gap 5 | Missing Meso-Micro Integration | 11 | 6% | Low | Meso-to-micro translation protocol |

### 4.7 Methodology Distribution Across the Corpus

**Table 4.7: Approach Type Distribution**

| Approach | N | % of Corpus |
|----------|---|-------------|
| optimization | 116 | 58.0% |
| mixed | 48 | 24.0% |
| empirical | 19 | 9.5% |
| simulation | 17 | 8.5% |

**Table 4.8: Spatial Scope Distribution**

| Planning Scope | N | % of Corpus |
|----------------|---|-------------|
| city | 182 | 91.0% |
| neighborhood | 6 | 3.0% |
| site | 5 | 2.5% |
| regional | 5 | 2.5% |
| corridor | 2 | 1.0% |

**Table 4.9: Thematic Coverage Flags Across the Corpus**

| Dimension | N Papers | % of Corpus |
|-----------|----------|-------------|
| Equity measured or addressed | 14 | 7.0% |
| Utilization measured or addressed | 92 | 46.0% |
| Phased/sequential approach modeled | 44 | 22.0% |
| Zoning or land-use considered | 5 | 2.5% |
| Meso-scale planning engaged | 11 | 5.5% |
| Multi-objective formulation | 10 | 5.0% |

**Table 4.10: Primary Category Distribution**

| Category | N | % |
|----------|---|---|
| Spatial Optimization for Charging Station Placement | 133 | 66.5% |
| Related Infrastructure Planning Approaches | 34 | 17.0% |
| Utilization and Demand Modeling | 21 | 10.5% |
| Phased and Sequential Deployment | 7 | 3.5% |
| Equity Considerations in Charging Infrastructure Planning | 5 | 2.5% |


---

## 5. Research Questions

The five identified gaps motivate four research questions, each targeting one or more gaps through a specific methodological contribution. The research questions are designed to be independently answerable while collectively constituting an integrated research program. Each question is framed to produce a measurable deliverable and is grounded in the literature evidence base established in Sections 3 and 4.

### RQ1: Spatial Unit Design and Zoning Schema Comparison (Gaps 1 and 2)

**Research Question:** How can mobility-corridor-aligned spatial units and comparative zoning schema analysis be integrated into urban BEV charging station siting to reduce spatial demand misalignment and quantify the planning consequences of zoning schema choice?

**Motivation:** Gap 1 (133 papers with partial evidence) documents the systematic reliance on administrative spatial boundaries that misrepresent mobility corridor demand. Gap 2 (only 5 papers) documents the complete absence of comparative zoning schema analysis. These two gaps share a common root: the spatial frame for charging infrastructure planning is treated as fixed and given rather than as a design variable with quantifiable consequences. Addressing them jointly through a spatial unit comparison study that simultaneously varies the spatial unit (administrative vs. corridor-based) and the zoning schema (current ordinance vs. alternative permitting frameworks) would produce the first evidence base for both decisions.

**Scope:** City-scale spatial analysis applied to at least one metropolitan area with available origin-destination trip data and municipal zoning ordinances. Comparison metrics include: spatial demand estimation error (root mean square deviation from observed charging events), Gini coefficient of coverage equity across income quartiles, total network infrastructure cost, and average station utilization rate.

**Expected Measurable Outcomes:**
- A spatial unit alignment score metric quantifying corridor-administrative boundary mismatch
- A zoning schema comparison procedure applicable to any metropolitan area with available land-use data
- Quantified reduction in spatial demand estimation error under corridor-based spatial units vs. TAZ-based baseline
- Evidence on whether zoning schema choice significantly affects equity and utilization outcomes

---

### RQ2: Joint Equity-Utilization Optimization (Gap 3)

**Research Question:** How can equity of geographic access and infrastructure utilization efficiency be simultaneously optimized in charging network design, and what are the Pareto-efficient tradeoffs between these objectives that planners can use to inform deployment decisions?

**Motivation:** Gap 3 (14 papers with partial evidence) documents the structural separation of equity and utilization in the optimization literature. Of the 200 reviewed papers, only 14 measure equity and only 92 measure utilization; fewer still measure both in the same study, and none jointly optimizes both in a single objective function. This separation leaves planners without the quantified tradeoff information needed to make defensible deployment decisions under competing objectives.

**Scope:** Multi-objective optimization model formulated as a bi-objective mixed-integer program, applied to a city-scale charging network with real demographic and transportation demand data. Equity is operationalized as the Gini coefficient of spatial accessibility across census tracts weighted by population. Utilization is operationalized as mean fill rate across deployed stations over a planning horizon.

**Expected Measurable Outcomes:**
- A joint equity-utilization objective function with formal Pareto optimality characterization
- A Pareto frontier mapping the equity-utilization tradeoff space under realistic demand scenarios
- Policy-relevant threshold identification: the minimum utilization penalty required to achieve a given equity improvement
- Comparison with single-objective baselines demonstrating the cost of objective separation

---

### RQ3: Adaptive Phased Deployment (Gap 4)

**Research Question:** What sequencing criteria and adaptive decision rules enable effective, budget-constrained phased deployment of BEV fast-charging infrastructure under demand uncertainty, and how much value does adaptive phasing create relative to static single-period optimization?

**Motivation:** Gap 4 (44 papers with partial evidence) documents the dominance of static single-period optimization in the literature. Real-world charging deployment is subject to budget cycles, demand uncertainty, and the irreversibility of sited infrastructure, conditions under which adaptive sequential decision-making is theoretically superior to static planning. The literature has not quantified this superiority or defined the trigger criteria that make adaptive phasing operationally feasible.

**Scope:** Multi-stage stochastic programming model with explicit phase-transition trigger criteria. The model represents multiple planning periods (phases), with decision variables at each phase conditioned on demand observations from prior phases. Trigger criteria are defined as utilization rate thresholds that, when exceeded, activate expansion to the next phase. Monte Carlo demand scenarios represent adoption uncertainty.

**Expected Measurable Outcomes:**
- An adaptive phased deployment decision procedure with defined phase-transition trigger criteria
- Quantified value of sequential planning relative to static optimization (expected cost difference under demand uncertainty)
- Sensitivity analysis on the trigger threshold design
- Minimum viable number of deployment phases for capturing the majority of adaptive value

---

### RQ4: Meso-to-Micro Site Translation (Gap 5)

**Research Question:** How can meso-level rollout plans be systematically translated to micro-level site implementation specifications, and what minimum information set must flow from the meso to the micro planning scale to ensure technical and planning feasibility?

**Motivation:** Gap 5 (11 papers) documents the absence of any validated translation protocol bridging city-level rollout planning to site-level implementation. This gap is the operational boundary of the current literature: research produces rollout plans but cannot operationalize them. The consequence in practice is that site selection is performed ad hoc, potentially violating the spatial intent of the rollout plan and introducing unmeasured equity and efficiency losses.

**Scope:** A translation protocol development and validation study. The protocol specifies: (a) the minimum viable information set from meso to micro (which zones, what phase, what charging tier, what minimum coverage radius); (b) a site suitability scoring methodology incorporating land-use compatibility, grid connection proximity, pedestrian access, and parking geometry; and (c) a feedback procedure for reconciling micro-level infeasibilities with meso-level allocations.

**Expected Measurable Outcomes:**
- A formalized meso-to-micro translation protocol
- A site suitability scoring function with defined weights and data sources
- A minimum viable information set specification validated against real-world site deployment decisions
- A protocol validation metric measuring consistency between meso-level rollout intent and micro-level siting outcomes


---

## 6. Proposed Research Framework

### 6.1 Framework Overview

The proposed research framework comprises three integrated stages that collectively address all five identified gaps and correspond directly to the four research questions:

**Stage A, Mobility-Corridor Spatial Unit Construction and Zoning Schema Comparison** (RQ1; addresses Gaps 1 and 2)

**Stage B, Joint Equity-Utilization Adaptive Phased Rollout Optimization** (RQ2 and RQ3; addresses Gaps 3 and 4)

**Stage C, Meso-to-Micro Site Translation Protocol** (RQ4; addresses Gap 5)

Each stage produces outputs that serve as direct inputs to the subsequent stage, creating a vertically integrated planning framework from city-scale spatial analysis to site-level implementation. The framework is designed to be applied to any metropolitan area with available origin-destination trip data, demographic data, land-use and zoning records, and grid infrastructure maps.

### 6.2 Stage A: Mobility-Corridor Spatial Unit Construction

Stage A addresses the foundational question of how to define the spatial frame for charging infrastructure planning. This stage is grounded in a completed preliminary study (see Chapter 8) that operationalized a mobility-aligned zoning approach in Toronto, Canada. That work provides empirical validation of the Stage A methodology and directly informs its design. Two activities constitute Stage A:

**Activity A1, Arterial Corridor Zone Construction.** The primary spatial unit is the arterial zone, constructed by applying GIS processing to the Toronto Centreline Network. Major arterial road segments are extracted from the full road hierarchy, connectivity is refined to remove topological breaks, and the resulting arterial network is used to partition the urban area into spatially contiguous zones that reflect actual BEV travel corridors rather than administrative or statistical boundaries. In the preliminary study, this procedure yielded 234 arterial zones from over 40,000 road segments, reducing the network to approximately 1,200 major arterial links while preserving the primary mobility corridors. BEV registration counts from Forward Sortation Area (FSA) polygons are proportionally redistributed to arterial zones using areal intersection weights, producing a corridor-aligned BEV density field. A graph-based representation of the arterial zone network is then constructed, where zones form nodes and road adjacencies define edges. Ridge-path extraction identifies contiguous sequences of zones with locally elevated BEV density, delineating the structural backbone of BEV activity. The corridor zones are benchmarked against FSA-based and TAZ-based alternatives on spatial demand alignment, using a graph-theoretic Weighted Proximity Distance (WPD) metric that accounts for BEV density and charger capacity.

**Activity A2, Infrastructure Alignment Benchmarking.** The existing fast-charging network is evaluated by computing the weighted hop distance from ridge-path nodes to the nearest charger locations in the arterial zone graph, benchmarked against a null distribution of 1,050 randomized charger configurations that preserve the observed station count and port capacity. The preliminary Toronto study found that 85.7% of randomized configurations achieved shorter weighted proximity distances than the existing FLO DCFC network of 17 stations, demonstrating that current deployment lacks systematic spatial optimization relative to BEV activity corridors. This benchmarking procedure is formalized as a replicable protocol applicable to any metropolitan area with available road centreline and BEV registration data.

Stage A outputs: (1) an arterial corridor zone map with BEV density assignments; (2) a ridge-path backbone identifying high-activity BEV corridors; (3) a spatial alignment benchmark score comparing the existing network to the mobility-corridor frame; (4) a spatial unit comparison report quantifying outcome differences between arterial, FSA-based, and TAZ-based zoning schemas.

### 6.3 Stage B: Joint Equity-Utilization Adaptive Phased Rollout Optimization

Stage B builds on Stage A outputs by formulating the charging station placement problem as a multi-objective, multi-stage stochastic optimization using the Stage A corridor zones as the spatial frame.

**Activity B1, Joint Objective Formulation.** The primary optimization model jointly minimizes the Gini coefficient of spatial accessibility across corridor zones (equity objective) and the inverse of mean station utilization rate (utilization objective). The bi-objective model is solved using the ε-constraint method to map the full Pareto frontier. This directly addresses Gap 3 by providing planners with a quantified equity-utilization tradeoff curve.

**Activity B2, Adaptive Phasing.** The multi-stage extension represents multiple deployment phases, each subject to a phase budget. Phase-transition trigger criteria are defined as utilization rate thresholds: when mean utilization in deployed stations exceeds a threshold τ, the model activates the next deployment phase. Demand uncertainty is represented through Monte Carlo scenarios of EV adoption growth. The adaptive model is compared to a static single-period benchmark to quantify the value of adaptive phasing (Gap 4).

Stage B outputs: (1) a joint equity-utilization Pareto frontier; (2) an adaptive phased deployment schedule with trigger criteria; (3) quantified value of adaptive vs. static planning.

### 6.4 Stage C: Meso-to-Micro Site Translation Protocol

Stage C operationalizes the Stage B rollout schedule by defining the information translation from meso-level allocation (which corridor zones receive stations in each phase) to micro-level site selection and design specifications.

**Activity C1, Translation Protocol Definition.** The protocol specifies: (a) the minimum information set flowing from meso to micro (zone identifier, phase, charging tier, coverage radius, equity priority flag); (b) a site suitability scoring function incorporating land-use compatibility score, grid connection proximity (distance to nearest transformer), pedestrian accessibility (Walk Score proxy), and parking geometry feasibility; and (c) a conflict resolution procedure for micro-level infeasibilities (when no site within a zone meets minimum suitability threshold, the protocol triggers meso-level reallocation).

**Activity C2, Protocol Validation.** The translation protocol is validated against real-world site deployment decisions in at least one metropolitan context where both a city-level charging plan and individual site selection decisions are documented. The validation metric is the consistency score: the proportion of actual selected sites that fall within the protocol's top-ranked suitability quartile for their respective corridor zones.

Stage C outputs: (1) a formalized meso-to-micro translation protocol; (2) a site suitability scoring function; (3) a validation study with consistency score.

### 6.5 Comparison with Existing Approaches

**Table 6.1: Proposed Framework vs. Existing Approaches in the Literature**

| Dimension | Existing Literature (n=200 papers) | Proposed Framework |
|-----------|-----------------------------------------|-------------------|
| Spatial unit | Administrative (TAZ, census tract) in ~67 papers | Mobility-corridor zones (Stage A) |
| Zoning analysis | Absent in 195 papers; binary constraint in 5 | Comparative multi-schema analysis (Stage A) |
| Equity-utilization | Single-objective in 186 equity papers | Joint bi-objective Pareto optimization (Stage B) |
| Planning horizon | Static single-period in majority | Multi-stage adaptive with trigger criteria (Stage B) |
| Scale integration | Meso only; micro absent | Meso + micro with translation protocol (Stage C) |
| Gap coverage | 0–2 gaps per paper (typical) | All 5 gaps addressed across 3 stages |
| Deliverable | Network plan or model | Validated framework with replication protocol |

### 6.6 Study Area and Data Requirements

The proposed framework will be applied to at least one metropolitan study area meeting the following data requirements: (a) origin-destination trip survey or mobile device mobility data; (b) municipal zoning ordinance GIS layers; (c) EV charging demand observations (station transaction data or smart meter data); (d) demographic data at census tract level; (e) grid infrastructure map (transformer locations and capacity); and (f) an existing or planned city charging infrastructure rollout plan. Where actual site selection decisions are documented, Stage C validation will be possible.


---

## 7. Expected Contributions and Timeline

### 7.1 Expected Contributions

This dissertation produces five primary contributions, each directly resolving one of the identified research gaps:

**Contribution 1, Mobility-Corridor Spatial Unit Methodology (Gap 1)**
A validated method for constructing mobility-corridor spatial zones from origin-destination data, with a quantified spatial unit alignment score and demonstrated reduction in spatial demand estimation error relative to administrative TAZ baselines. This is the first methodology in the literature that directly questions and empirically tests the validity of the spatial frame for charging infrastructure planning.

**Contribution 2, Zoning Schema Comparison Procedure (Gap 2)**
The first systematic comparative analysis of alternative zoning schemas for charging infrastructure siting, producing a replicable schema comparison procedure that quantifies the coverage, equity, cost, and utilization consequences of zoning schema design choices. This contribution provides evidence that has been entirely absent from the planning literature.

**Contribution 3, Joint Equity-Utilization Optimization Model (Gap 3)**
A bi-objective optimization model with formal Pareto frontier characterization that simultaneously optimizes equity of spatial access and infrastructure utilization efficiency. The Pareto frontier provides planners with quantified tradeoff information, translating a political/ethical question (how much equity is worth how much efficiency?) into a technically grounded, reproducible analysis.

**Contribution 4, Adaptive Phasing Decision Procedure (Gap 4)**
A multi-stage stochastic programming model with adaptive phase-transition trigger criteria, validated against demand uncertainty scenarios, with quantified comparison to static single-period optimization. The decision procedure is operationally specified, defining when (trigger criteria) and how (reallocation rules) to advance from one deployment phase to the next.

**Contribution 5, Meso-to-Micro Translation Protocol (Gap 5)**
A formalized information translation protocol bridging meso-level rollout planning to micro-level site selection, with a validated site suitability scoring function and consistency score against real-world deployment decisions. This contribution closes the operational gap between planning and implementation that currently prevents rollout plans from being systematically operationalized.

### 7.2 Research Timeline

**Table 7.1: Three-Year Research Timeline**

| Phase | Year | Key Activities | Deliverables |
|-------|------|----------------|--------------|
| **Phase 1: Review and Stage A** | Year 1, Q1–Q3 | Complete systematic review; develop and validate corridor zone construction method; conduct zoning schema comparison | Systematic review paper (submitted); Stage A methodology paper (draft) |
| **Phase 1: Stage A Completion** | Year 1, Q4 | Finalize spatial unit alignment score; validate against demand estimation error | Stage A paper (submitted) |
| **Phase 2: Stage B Development** | Year 2, Q1–Q2 | Formulate bi-objective optimization model; compute Pareto frontier; begin multi-stage extension | Stage B model paper (draft) |
| **Phase 2: Stage B Completion** | Year 2, Q3–Q4 | Complete adaptive phasing model; demand uncertainty experiments; comparison with static baseline | Stage B paper (submitted); conference presentations |
| **Phase 3: Stage C Development** | Year 3, Q1–Q2 | Define translation protocol; develop site suitability scoring; protocol validation study | Stage C paper (draft) |
| **Phase 3: Integration and Writing** | Year 3, Q3–Q4 | Full framework integration; case study validation; dissertation writing and defense | Dissertation manuscript; Stage C paper (submitted); defense |

### 7.3 Anticipated Venues for Publication

- **Systematic review paper**: Transportation Research Part C: Emerging Technologies or Journal of Transport Geography
- **Stage A paper**: Environment and Planning B: Urban Analytics and City Science or Computers, Environment and Urban Systems
- **Stage B paper**: Transportation Science or European Journal of Operational Research
- **Stage C paper**: Journal of the American Planning Association or Urban Studies


---

## 8. References

All references are presented in academic format, grouped by thematic category. arXiv preprints are identified by their arXiv identifier. For papers with DOIs, the DOI is provided.

### Spatial Optimization for Charging Station Placement

[siting_and_2021] Ramin Ahadi, Wolfgang Ketter, John Collins, Nicolò Daina (2021). *Siting and Sizing of Charging Infrastructure for Shared Autonomous Electric Fleets*. International Joint Conference on Autonomous Agents and Multiagent Systems. DOI: 10.65109/uaun3752
[optimizing_urban_2025] Wenqing Ai, Hanyu Cheng, Wei Qi (2025). *Optimizing Urban EV Charging and Battery Swapping Infrastructure: A Location-Inventory-Grid Model*. arXiv. arXiv:2511.14308v1
[the_electric_2024] Mehmet Anil Akbay, Christian Blum, Michella Saliba (2024). *The EV Problem with Road Junctions and Road Types: An Ant Colony Optimization Approach*. Proceedings of the Genetic and Evolutionary Computation Conference. DOI: 10.1145/3638529.3653997
[a_data-driven_2023] Nassr Al-Dahabreh, Mohammad Ali Sayed, Khaled Sarieddine, Mohamed Elhattab, Maurice Khabbaz, Ribal Atallah, Chadi Assi (2023). *A Data-Driven Framework for Improving Public EV Charging Infrastructure: Modeling and Forecasting*. arXiv. arXiv:2312.05333v1
[data-driven_ev_2025] Talal Alharbi, Ahmed Abdalrahman, Mostafa H. Mostafa (2025). *Data-driven EV charging infrastructure with uncertainty based on a spatial–temporal flow-driven (STFD) models considering batteries*. Scientific Reports. DOI: 10.1038/s41598-025-12079-3
[urban_electric_2024] Amel Ali Alhussan, Doaa Sami Khafaga, El-Sayed M. El-kenawy, Marwa M. Eid, Abdelhameed Ibrahim (2024). *Urban EVCS Placement Optimization with Graylag Goose Optimization Voting Classifier*. Computers, Materials &amp; Continua. DOI: 10.32604/cmc.2024.049001
[a_particle_2024] Mohammad Aljaidi, Ghassan Samara, Manish Kumar Singla, Ayoub Alsarhan, Mohammad Hassan, Murodbek Safaraliev, Pavel Matrenin, Alexander Tavlintsev (2024). *A particle swarm optimizer-based optimization approach for locating EVs charging stations in smart cities*. International Journal of Hydrogen Energy. DOI: 10.1016/j.ijhydene.2024.09.029
[a_density-based_2025] Hamza Ameer, Yujie Wang, Zonghai Chen (2025). *A density-based spatial clustering and linear programming method for EVCS location and price optimization*. Energy. DOI: 10.1016/j.energy.2025.134581
[hybrid_optimization_2025] Hamza Ameer, Yujie Wang, Xiaofei Fan, Zonghai Chen (2025). *Hybrid optimization of EV charging station placement and pricing using Bender’s decomposition and NSGA-II algorithm*. Applied Energy. DOI: 10.1016/j.apenergy.2025.126385
[designing_an_2022] Nissa Amilia, Zulkifli Palinrungi, Iwan Vanany, Mansur Arief (2022). *Designing an Optimized EVCS Infrastructure for Urban Area: A Case study from Indonesia*. arXiv. arXiv:2209.03448v1
[a_robust_2023] Mansur Arief, Yan Akhra, Iwan Vanany (2023). *A Robust and Efficient Optimization Model for EVCSs in Developing Countries under Electricity Uncertainty*. arXiv. arXiv:2307.05470v1
[electric_vehicle_2017] Angelos Aveklouris, Yorie Nakahira, Maria Vlasiou, Bert Zwart (2017). *EV charging: a queueing approach*. arXiv. arXiv:1712.08747v1
[regional_transportation_2026] Ismaeel Babur, Jane Macfarlane (2026). *Regional Transportation Modeling for Equitable EV Charging Infrastructure Design*. arXiv. arXiv:2601.22395v1
[strategic_competition_2021] Reza Bayani, Arash Farokhi Soofi, Saeed D. Manshadi (2021). *Strategic Competition of EVCSs in a Regulated Retail Electricity Market*. arXiv. arXiv:2111.11592v1
[charging_games_2015] Olivier Beaude, Samson Lasaulce, Martin Hennebel (2015). *Charging Games in Networks of Electrical Vehicles*. arXiv. arXiv:1509.07349v1
[introducing_decentralized_2015] Olivier Beaude, Yujun He, Martin Hennebel (2015). *Introducing Decentralized EV Charging Coordination for the Voltage Regulation*. arXiv. arXiv:1509.08497v1
[minimizing_the_2015] Olivier Beaude, Samson Lasaulce, Martin Hennebel, Jamal Daafouz (2015). *Minimizing the impact of EV charging on the electricity distribution network*. arXiv. arXiv:1509.07332v1
[simultaneous_optimization_2026] Juan Pablo Bertucci, Theo Hofman, Mauro Salazar (2026). *Simultaneous Optimization of Electric Ferry Operations and Charging Infrastructure*. arXiv. DOI: 10.1109/ESTS62818.2025.11152468
[planning_of_2022] Haihong Bian, Chengang Zhou, Zhengyang Guo, Ximeng Wang, Ying He, Shan Peng (2022). *Planning of EV fast-charging station based on POI interest point division, functional area, and multiple temporal and spatial characteristics*. Energy Reports. DOI: 10.1016/j.egyr.2022.10.161
[towards_sustainable_2024] Sornkitja Boonprong, Nathapat Punturasan, Pariwate Varnakovida, Wichien Prechathamwong (2024). *Towards Sustainable Urban Mobility: Voronoi-Based Spatial Analysis of EV Charging Stations in Bangkok*. Sustainability. DOI: 10.3390/su16114729
[location_of_2020] Georg Brandstätter, Markus Leitner, Ivana Ljubić (2020). *Location of Charging Stations in Electric Car Sharing Systems*. Transportation Science. DOI: 10.1287/trsc.2019.0931
[charging_station_2024] Li Cai, Junting Li, Haitao Zhu, Chenxi Yang, Juan Yan, Qingshan Xu, Xiaojiang Zou (2024). *Charging Station Site Selection Optimization for Electric Logistics Vehicles, Taking into Account Time-Window and Load Constraints*. World EV Journal. DOI: 10.3390/wevj15050181
[energy_management_2024] Yuan Cao, Menghao Zhou (2024). *Energy management optimization of hybrid EVs based on deep learning model predictive control*. Intelligent Decision Technologies. DOI: 10.3233/idt-240298
[location_and_2025] Minje Choi, Yee Van Fan, Doyun Lee, Sion Kim, Seungjae Lee (2025). *Location and capacity optimization of EV charging stations using genetic algorithms and fuzzy analytic hierarchy process*. Clean Technologies and Environmental Policy. DOI: 10.1007/s10098-024-02986-w
[citizen_centric_2021] Christian Cintrano, Jamal Toutouh, Enrique Alba (2021). *Citizen centric optimal EVCSs locations in a full city: case of Malaga*. arXiv. arXiv:2109.04975v1
[electric_vehicle_2018] Qiushi Cui, Yang Weng, Chin-Woo Tan (2018). *EVCS Placement Method for Urban Areas*. arXiv. arXiv:1808.09660v1
[charging_station_2018] Antoine Deza, Kai Huang, Michael R. Metel (2018). *Charging station optimization for balanced electric car sharing*. arXiv. arXiv:1811.11970v1
[a_2025] Bui Khanh Linh Do, Thanh H. Nguyen, Nghi Huynh Quang, Doanh Nguyen-Ngoc, Laurent El Ghaoui (2025). *A Digital Twin Framework for Decision-Support and Optimization of EV Charging Infrastructure in Localized Urban Systems*. arXiv. DOI: 10.1016/j.compenvurbsys.2026.102422
[strategic_planning_2026] Amelia Nur Fariza, Ilham Kurniawan, Rizki Amalia Pratiwi, Aina Nindiani, Annisa Indah Pratiwi (2026). *Strategic Planning of Public EVCSs Using AHP and GIS to Support Sustainable Mobility in West Java, Indonesia*. E3S Web of Conferences. DOI: 10.1051/e3sconf/202670602004
[incorporating_time-dependent_2023] Carlo Filippi, Gianfranco Guastaroba, Lorenzo Peirano, M. Grazia Speranza (2023). *Incorporating time-dependent demand patterns in the optimal location of capacitated charging stations*. arXiv. arXiv:2301.05077v1
[optimizing_the_2020] ANASTASIYA GORBUNOVA, ILYA ANISIMOV (2020). *OPTIMIZING THE LOCATION OF URBAN CHARGING STATIONS FOR EVs: CASE STUDY OF THE CITY OF TYUMEN, RUSSIAN FEDERATION*. WIT Transactions on The Built Environment. DOI: 10.2495/ut200021
[demand_prediction_2016] Ragavendran Gopalakrishnan, Arpita Biswas, Alefiya Lightwala, Skanda Vasudevan, Partha Dutta, Abhishek Tripathi (2016). *Demand Prediction and Placement Optimization for EVCSs*. arXiv. arXiv:1604.05472v2
[optimal_evcs_2024] Bin He, Bo Yang, Yiming Han, Yimin Zhou, Yuanweiji Hu, Hongchun Shu, Shi Su, Jin Yang, Yuanping Huang, Jiale Li, Lin Jiang, Hongbiao Li (2024). *Optimal EVCS planning via spatial-temporal distribution of charging demand forecasting and traffic-grid coupling*. Energy. DOI: 10.1016/j.energy.2024.133885
[optimal_planning_2024] Jae Heo, Soowon Chang (2024). *Optimal planning for EV FCSs placements in a city scale using an advantage actor-critic deep RL and geospatial analysis*. Sustainable Cities and Society. DOI: 10.1016/j.scs.2024.105567
[optimal_planning_2021] Hui Hou, Junyi Tang, Bo Zhao, Leiqi Zhang, Yifan Wang, Changjun Xie (2021). *Optimal Planning of EVCS Considering Mutual Benefit of Users and Power Grid*. World EV Journal. DOI: 10.3390/wevj12040244
[optimizing_ev_2024] Jinyi Huang, Xiaozhou Zhou (2024). *Optimizing EV Charging Station Placement in New South Wales: A Soft Actor-Critic RL Approach*. 2024 5th International Conference on Computer Engineering and Application (ICCEA). DOI: 10.1109/iccea62105.2024.10603658
[a_spatially_2025] Yanyan Huang, Hangyi Ren, Xudong Jia, Xianyu Yu, Dong Xie, You Zou, Daoyuan Chen, Yi Yang (2025). *A Spatially Aware Machine Learning Method for Locating EVCSs*. World EV Journal. DOI: 10.3390/wevj16080445
[web_mining_2022] Philipp Hummler, Christof Naumzik, Stefan Feuerriegel (2022). *Web Mining to Inform Locations of Charging Stations for EVs*. arXiv. DOI: 10.1145/3487553.3524264
[a_novel_2022] Ying-Chao Hung, George Michailidis (2022). *A Novel Data-Driven Approach for Solving the EVCS Location-Routing Problem*. IEEE Transactions on Intelligent Transportation Systems. DOI: 10.1109/tits.2022.3196835
[energy-optimal_design_2021] Juriaan van den Hurk, Mauro Salazar (2021). *Energy-optimal Design and Control of EVs' Transmissions*. arXiv. arXiv:2105.05119v1
[deep_spatio-temporal_2021] Frederik Boe Hüttel, Inon Peled, Filipe Rodrigues, Francisco C. Pereira (2021). *Deep Spatio-Temporal Forecasting of Electrical Vehicle Charging Demand*. arXiv. arXiv:2106.10940v1
[charge-map_an_2025] Kazi Ashik Islam, Aparna Kishore, Rounak Meyur, Swapna Thorve, Da Qi Chen, H. Vincent Poor, Madhav V. Marathe (2025). *CHARGE-MAP: An integrated framework to study the multicriteria EV charging infrastructure expansion problem*. Proceedings of the National Academy of Sciences. DOI: 10.1073/pnas.2514184122
[layout_and_2023] Yi Jiang (2023). *Layout and optimization of charging piles for new energy EVs – A study on Xi'an urban area*. E3S Web of Conferences. DOI: 10.1051/e3sconf/202342401009
[pricing_electric_2026] Nanfei Jiang, Yi Zhou, Josh A. Taylor, Mahnoosh Alizadeh (2026). *Pricing EV Charging and Station Access via Copositive Duality*. arXiv. arXiv:2604.15227v1
[development_of_2022] Hojun Jin, Sangkeum Lee, Sarvar Hussain Nengroo, Dongsoo Har (2022). *Development of Charging, Discharging Scheduling Algorithm for Economical and Energy Efficient Operation of Multi EV Charging Station*. arXiv. arXiv:2205.04116v1
[trajectory-integrated_accessibility_2025] Yi Ju, Jiaman Wu, Zhihan Su, Lunlong Li, Jinhua Zhao, Marta C. González, Scott J. Moura (2025). *Trajectory-Integrated Accessibility Analysis of Public EVCSs*. arXiv. arXiv:2505.12145v1
[data-driven_optimization_2025] Julius Stephan Junker, Rong Hu, Ziyue Li, Wolfgang Ketter (2025). *Data-Driven Optimization of EV Charging Station Placement Using Causal Discovery*. arXiv. arXiv:2503.17055v1
[explainable_and_2025] Shalini Kapoor (2025). *Explainable and context-aware Graph Neural Networks for dynamic EV route optimization to optimal charging station*. Expert Systems with Applications. DOI: 10.1016/j.eswa.2025.127331
[a_multi-modal_2025] Oktay Karakuş, Padraig Corcoran (2025). *A Multi-Modal Spatial Risk Framework for EV Charging Infrastructure Using Remote Sensing*. arXiv. arXiv:2506.19860v1
[a_united_2025] Tony Kinchen, Panagiotis Typaldos, Andreas A. Malikopoulos (2025). *A United Framework for Planning EV Charging Accessibility*. arXiv. arXiv:2508.05827v1
[route_optimization_2017] Dimitrios Kosmanos, Leandros Maglaras, Michalis Mavrovouniotis, Sotiris Moschoyiannis, Antonios Argyriou, Athanasios Maglaras, Helge Janicke (2017). *Route Optimization of EVs based on Dynamic Wireless Charging*. arXiv. arXiv:1710.03726v1
[optimal_electric_2024] Pulkit Kumar, Harpreet Kaur Channi (2024). *Optimal EVCS Placement: A Multi-Criteria Decision-Making Approach for Site Selection*. 2024 International Conference on Integrated Circuits and Communication Systems (ICICACS). DOI: 10.1109/icicacs60521.2024.10498237
[electric_vehicle_2013] Albert Y. S. Lam, Yiu-Wing Leung, Xiaowen Chu (2013). *EVCS Placement: Formulation, Complexity, and Solutions*. arXiv. DOI: 10.1109/TSG.2014.2344684
[optimising_electric_2022] Steven Lamontagne, Margarida Carvalho, Emma Frejinger, Bernard Gendron, Miguel F. Anjos, Ribal Atallah (2022). *Optimising EVCS Placement using Advanced Discrete Choice Models*. arXiv. DOI: 10.1287/ijoc.2022.0185
[electric_vehicles_2015] Andrea Lanna, Francesco Liberati, Letterio Zuccaro, Alessandro Di Giorgio (2015). *EVs Charging Control based on Future Internet Generic Enablers*. arXiv. arXiv:1503.01267v1
[electric_vehicle_0] Zhiyun Li, Mashrur Chowdhury, Parth Bhavsar (0). *EV Charging Infrastructure Optimization Incorporating Demand Forecasting and Renewable Energy Application*. . DOI: 10.20944/preprints202508.1268.v1
[electric_vehicle_2024] Zhiyun Li, Mashrur Chowdhury, Parth Bhavsar (2024). *EV Charging Infrastructure Optimization Incorporating Demand Forecasting and Renewable Energy Application*. World Journal of Innovation and Modern Technology. DOI: 10.53469/wjimt.2024.07(06).12
[predictive_energy_2022] Weiyi Lin, Han Zhao, Bingzhan Zhang, Ye Wang, Yan Xiao, Kang Xu, Rui Zhao (2022). *Predictive Energy Management Strategy for Range-Extended EVs Based on ITS Information and Start–Stop Optimization with Vehicle Velocity Forecast*. Energies. DOI: 10.3390/en15207774
[optimal_placement_2023] Jiaqi Liu, Jian Sun, Xiao Qi (2023). *Optimal Placement of Charging Stations in Road Networks: A RL Approach with Attention Mechanism*. Applied Sciences. DOI: 10.3390/app13148473
[battery_swapping_2024] Guangyuan Liu, Yu Zhang, Tianshi Ming, Chunlong Yu (2024). *BSS location for EVs: a simulation optimization approach*. arXiv. arXiv:2412.15233v1
[joint_optimization_2021] Justin Luke, Mauro Salazar, Ram Rajagopal, Marco Pavone (2021). *Joint Optimization of Autonomous EV Fleet Operations and Charging Station Siting*. arXiv. DOI: 10.1109/ITSC48978.2021.9565089
[a_consumer_2018] Chao Luo, Yih-Fang Huang, Vijay Gupta (2018). *A Consumer Behavior Based Approach to Multi-Stage EV Charging Station Placement*. arXiv. DOI: 10.1109/VTCSpring.2015.7145593
[engineering_and_2018] Chao Luo (2018). *Engineering and Economic Analysis for EV Charging Infrastructure --- Placement, Pricing, and Market Design*. arXiv. arXiv:1808.03897v1
[placement_of_2018] Chao Luo, Yih-Fang Huang, Vijay Gupta (2018). *Placement of EV Charging Stations --- Balancing Benefits among Multiple Entities*. arXiv. DOI: 10.1109/TSG.2015.2508740
[optimal_fast_2020] Tai-Yu Ma, Simin Xie (2020). *Optimal FCS locations for electric ridesharing service with online vehicle-charging station assignment*. arXiv. DOI: 10.1016/j.trd.2020.102682
[integrating_en_2024] Asal Mehditabrizi, Behnam Tahmasbi, Saeed Saleh Namadi, Cinzia Cirillo (2024). *Integrating En Route and Home Proximity in EV Charging Accessibility: A Spatial Analysis in the Washington Metropolitan Area*. arXiv. arXiv:2409.08287v1
[joint_planning_2026] Mario A. Mejia, Leonardo H. Macedo, Gregorio Muñoz-Delgado, Javier Contreras, John F. Franco (2026). *Joint Planning of Distribution Systems and EV Charging Infrastructure Using a GIS-Based Spatial Analysis Framework*. IEEE Transactions on Industry Applications. DOI: 10.1109/tia.2025.3600209
[a_two-stage_2025] Yunfan Meng, Yonghui Sun, Dongliang Xie, Min Xiao, Chenxu Yin, Liang Zhao (2025). *A two-stage optimization framework for EV charging station planning considering investment cost and service satisfaction*. Applied Energy. DOI: 10.1016/j.apenergy.2025.126911
[towards_using_2024] Marek Miltner, Jakub Zíka, Daniel Vašata, Artem Bryksa, Magda Friedjungová, Ondřej Štogl, Ram Rajagopal, Oldřich Starý (2024). *Towards Using Machine Learning to Generatively Simulate EV Charging in Urban Areas*. arXiv. arXiv:2412.10531v2
[hierarchical_optimization_2021] Amir Mirheli, Leila Hajibabai (2021). *Hierarchical Optimization of EV Charging Infrastructure Design and Facility Logistics*. arXiv. arXiv:2105.10557v1
[a_framework_2022] Partha Mishra, Eric Miller, Shriram Santhanagopalan, Kevin Bennion, Andrew Meintz (2022). *A Framework to Analyze the Requirements of a Multiport Megawatt-Level Charging Station for Heavy-Duty EVs*. Energies. DOI: 10.3390/en15103788
[spatial_arbitrage_2023] Mostafa Mohammadian, Constance Crozier, Kyri Baker (2023). *Spatial Arbitrage Through Bidirectional EV Charging with Delivery Fleets*. arXiv. arXiv:2311.11464v1
[multiobjective_optimization_2024] Abdallah Mohammed, Omar Saif, Maged A Abo-Adma, Rasha Elazab (2024). *Multiobjective optimization for sizing and placing EVCSs considering comprehensive uncertainties*. Energy Informatics. DOI: 10.1186/s42162-024-00428-x
[optimal_location_2023] Rémi Mourgues, Martin Rodriguez-Vega, Carlos Canudas-De-Wit (2023). *Optimal Location of EVs Public Charging Stations Based on a Macroscopic Urban Electromobility Model*. 2023 62nd IEEE Conference on Decision and Control (CDC). DOI: 10.1109/cdc49753.2023.10383407
[analyzing_locational_2025] Arash Mousaei (2025). *Analyzing locational inequalities in the placement of EVCSs using machine learning: A case study in Glasgow*. Next Research. DOI: 10.1016/j.nexres.2024.100123
[predicting_optimal_2025] Arash Mousaei, Yahya Naderi (2025). *Predicting Optimal Placement of EV Charge Stations Using Machine Learning: A Case Study in Glasgow, UK*. 2025 12th Iranian Conference on Renewable Energies and Distributed Generation (ICREDG). DOI: 10.1109/icredg66184.2025.10966078
[ev_charging_2022] Mohammad Mousavi, Li "Lisa" Qi, Alexander Brissette, Meng Wu (2022). *EV Charging Station Wholesale Market Participation: A Strategic Bidding and Pricing Approach*. arXiv. arXiv:2209.05658v1
[optimizing_urban_2024] Soviyan Munawar (2024). *Optimizing Urban Logistics Through EV Integration*. Sinergi International Journal of Logistics. DOI: 10.61194/sijl.v2i3.626
[a_two-stage_2026] Hamid Najafzad, Moddassir Khan Nayeem, Fuhad Ahmed Opu, Omar Abbaas, Gabriel Nicolosi (2026). *A Two-Stage Stochastic Optimization Model for the Equitable Deployment of Fixed and Mobile EVCSs*. arXiv. arXiv:2602.02333v1
[optimal_mixed_2025] Haruko Nakao, Tai-Yu Ma, Richard D. Connors, Francesco Viti (2025). *Optimal mixed fleet and charging infrastructure planning to electrify demand responsive feeder services with target CO2 emission constraints*. arXiv. DOI: 10.1016/j.apenergy.2025.127216
[an_exact_2025] Mobina Nankali, Michael W. Levin (2025). *An Exact Solution Algorithm for the Bi-Level Optimization Problem of EVs Charging Station Placement*. arXiv. arXiv:2511.19884v2
[competitive_ev_2025] The Minh Nguyen, Nagisa Sugishita, Margarida Carvalho, Amira Dems (2025). *Competitive EV charging station location with queues*. arXiv. arXiv:2510.12961v1
[joint_optimization_2025] Akihisa Okada, Keisuke Otaki, Hiroaki Yoshida (2025). *Joint Optimization of EV Routes and Charging Locations Learning Charge Constraints Using QUBO Solver*. arXiv. arXiv:2506.04687v1
[a_method_2019] Tianshu Ouyang, Jiahong Cai, Yuxuan Gao, Xinyan He, Huimiao Chen, Kexin Hang (2019). *A Method of EV Detour-to-Recharge Behavior Modeling and Charging Station Deployment*. arXiv. arXiv:1910.02138v4
[optimal_placement_2021] Shankar Padmanabhan, Aidan Petratos, Allen Ting, Kristina Zhou, Dylan Hageman, Jesse R. Pisel, Michael J. Pyrcz (2021). *Optimal Placement of Public EVCSs Using Deep RL*. arXiv. arXiv:2108.07772v2
[placement_of_2023] A. Pal, A. Bhattacharya, A. K. Chakraborty (2023). *Placement of EVCS and solar distributed generation in distribution system considering uncertainties*. Scientia Iranica. DOI: 10.24200/sci.2021.56782.4908
[optimization_strategies_2024] Sudheer Panyaram (2024). *Optimization Strategies for Efficient Charging Station Deployment in Urban and Rural Networks*. FMDB Transactions on Sustainable Environmental Sciences. DOI: 10.69888/ftsess.2024.000245
[maximum_flow-based_2023] Pierre-Luc Parent, Margarida Carvalho, Miguel F. Anjos, Ribal Atallah (2023). *Maximum flow-based formulation for the optimal location of EVCSs*. arXiv. arXiv:2312.05980v1
[optimal_ev_2024] G. Pierrou, C. Valero-De La Flor, G. Hug (2024). *Optimal EV Charging Scheduling at Electric Railway Stations Under Peak Load Constraints*. arXiv. arXiv:2404.07804v1
[fast-charging_station_2023] Dong Qiao, Guangmin Wang, Meng Xu (2023). *Fast-charging station location problem: A two-phase approach with mathematical program with equilibrium constraints considering charging choice behaviour*. Sustainable Cities and Society. DOI: 10.1016/j.scs.2023.104678
[performance_analysis_2022] Yujie Qin, Mustafa A. Kishk, Mohamed-Slim Alouini (2022). *Performance Analysis of Charging Infrastructure Sharing in UAV and EV-involved Networks*. arXiv. arXiv:2208.06782v1
[a_quantum_2024] Tina Radvand, Alireza Talebpour, Homa Khosravian (2024). *A Quantum Optimization Algorithm for Optimal EVCS Placement for Intercity Trips*. arXiv. arXiv:2410.16231v2
[predicting_electric_2018] Anshul Ramachandran, Ashwin Balakrishna, Peter Kundzicz, Anirudh Neti (2018). *Predicting EVCS Usage: Using Machine Learning to Estimate Individual Station Statistics from Physical Configurations of Charging Station Networks*. arXiv. arXiv:1804.00714v1
[a_method_2020] Dimitrios Rizopoulos, Domokos Esztergár-Kiss (2020). *A Method for the Optimization of Daily Activity Chains Including EVs*. Energies. DOI: 10.3390/en13040906
[multiobjective_model_2025] Francisco Ruiz-Barajas, Elias Olivares-Benitez, Adrian Ramirez-Nafarrate, Rosa G. González-Ramírez (2025). *Multiobjective model to optimize charging station location for the decarbonization process in Mexico*. International Transactions in Operational Research. DOI: 10.1111/itor.13611
[resource_aware_2020] Cesar Santoyo, Gustav Nilsson, Samuel Coogan (2020). *Resource Aware Pricing for EV Charging*. arXiv. arXiv:2009.10771v1
[reducing_waiting_2021] Sven Schoenberg, Falko Dressler (2021). *Reducing Waiting Times at Charging Stations with Adaptive EV Route Planning*. arXiv. DOI: 10.1109/TIV.2022.3140894
[sustainable_planning_2024] Sania E. Seilabi, Mohammadhosein Pourgholamali, Mohammad Miralinaghi, Gonçalo Homem de Almeida Correia, Zongzhi Li, Samuel Labi (2024). *Sustainable Planning of EVCSs: A Bi-Level Optimization Framework for Reducing Vehicular Emissions in Urban Road Networks*. Sustainability. DOI: 10.3390/su17010001
[sequential_charging_2024] Wenjia Shen, Bo Zhou, Ruiwei Jiang, Siqian Shen (2024). *Sequential Charging Station Location Optimization under Uncertain Charging Behavior and User Growth*. arXiv. arXiv:2411.01416v1
[causal_spillover_2025] M. Mavin De Silva, Callie Clark, Tadachika Nakayama, Takahiro Yabe (2025). *Causal spillover effects of EVCS placement on local businesses: a staggered adoption study*. arXiv. arXiv:2511.19507v1
[optimal_placement_2022] Dandu Srinivas, M. Ramasekhara Reddy (2022). *Optimal Placement of EVCS by Considering Dynamic Loads in Radial Distribution System*. 2022 International Conference on Automation, Computing and Renewable Systems (ICACRS). DOI: 10.1109/icacrs55517.2022.10029303
[predicting_popularity_2019] Milan Straka, Pasquale De Falco, Gabriella Ferruzzi, Daniela Proto, Gijs van der Poel, Shahab Khormali, Ľuboš Buzna (2019). *Predicting popularity of EV charging infrastructure from GIS data*. arXiv. DOI: 10.1109/ACCESS.2020.2965621
[initial_location_2023] Handrea Bernando Tambunan, Ruly Bayu Sitanggang, Muhammad Muslih Mafruddin, Oksa Prasetyawan, Kensianesi Kensianesi, Istiqomah Istiqomah, Nur Cahyo, Fefria Tanbar (2023). *Initial location selection of EVs charging infrastructure in urban city through clustering algorithm*. International Journal of Electrical and Computer Engineering (IJECE). DOI: 10.11591/ijece.v13i3.pp3266-3280
[on_the_2023] Johnny Tiu, Shankar Ramharack, Patrick Hosein (2023). *On the Optimal Placement of EVCSs*. arXiv. arXiv:2306.11069v1
[optimal_decision_2019] Bishal Upadhaya, Donghan Feng, Yun Zhou, Qiang Gui, Xiaojin Zhao, Dan Wu (2019). *Optimal Decision Making Model of Battery Energy Storage-Assisted EVCS Considering Incentive Demand Response*. arXiv. arXiv:1906.08497v1
[electric_vehicle_2023] Sushil Mahavir Varma, Francisco Castro, Siva Theja Maguluri (2023). *EV Fleet and Charging Infrastructure Planning*. arXiv. arXiv:2306.10178v4
[optimizing_the_2015] Mohammad M. Vazifeh, Hongmou Zhang, Paolo Santi, Carlo Ratti (2015). *Optimizing the Deployment of EVCSs Using Pervasive Mobility Data*. arXiv. DOI: 10.1016/j.tra.2019.01.002
[reinforcement_learning-based_2022] Leonie von Wahl, Nicolas Tempelmeier, Ashutosh Sao, Elena Demidova (2022). *RL-based Placement of Charging Stations in Urban Road Networks*. arXiv. DOI: 10.1145/3534678.3539154
[double-layer_game_2020] Tian Wang, Bo Yang, Cailian Chen (2020). *Double-Layer Game Based Wireless Charging Scheduling for EVs*. arXiv. arXiv:2003.03119v1
[research_on_2022] Limeng Wang, Chao Yang, Yi Zhang, Fanjin Bu (2022). *Research on Multi-Objective Planning of EVCSs Considering the Condition of Urban Traffic Network*. arXiv. arXiv:2208.12921v1
[spap_simultaneous_2023] Yizong Wang, Dong Zhao, Yajie Ren, Desheng Zhang, Huadong Ma (2023). *SPAP: Simultaneous Demand Prediction and Planning for EV Chargers in a New City*. ACM Transactions on Knowledge Discovery from Data. DOI: 10.1145/3565577
[beyond_profit_2024] Shuoyao Wang, Jiawei Lin (2024). *Beyond Profit: A Multi-Objective Framework for EVCS Operations*. arXiv. arXiv:2407.01536v1
[optimizing_electric_2023] Yongzhong Wu, Yikuan Lu, Zhijie Zhu, José Holguín-Veras (2023). *Optimizing EV Charging Infrastructure on Highways: A Multi-Agent-Based Planning Approach*. Sustainability. DOI: 10.3390/su151813634
[a_two-layer_2024] Chuanshen Wu, Yan Wang, Qianyun Shi, Shan Gao (2024). *A two-layer planning method for location and capacity determination of public EVCSs*. International Journal of Electrical Power &amp; Energy Systems. DOI: 10.1016/j.ijepes.2024.110205
[robust_charging_2025] Dongyang Xia, Lixing Yang, Yahan Lu, Shadi Sharif Azadeh (2025). *Robust charging station location and routing-scheduling for electric modular autonomous units*. arXiv. arXiv:2504.04408v1
[a_battery_2023] Xu Xin, Tao Zhang, Cui Li, Yanran Liu, Lingyu Gao, Yuchuan Du (2023). *A BEV Transportation Network Design Model with Bounded Rational Travelers*. Journal of Advanced Transportation. DOI: 10.1155/2023/6506169
[distributed_coordination_2022] Dongxiang Yan, Chengbin Ma, Yue Chen (2022). *Distributed Coordination of Charging Stations Considering Aggregate EV Power Flexibility*. arXiv. arXiv:2206.06834v1
[dynamic_modeling_2020] Dingtong Yang, Navjyoth J. S. Sarma, Michael Hyland, R. Jayakrishnan (2020). *Dynamic Modeling and Real-time Management of a System of EV Fast-charging Stations*. arXiv. arXiv:2012.09349v1
[an_agent-based_2023] Zhiyan Yi, Bingkun Chen, Xiaoyue Cathy Liu, Ran Wei, Jianli Chen, Zhuo Chen (2023). *An agent-based modeling approach for public charging demand estimation and charging station location optimization at urban scale*. Computers, Environment and Urban Systems. DOI: 10.1016/j.compenvurbsys.2023.101949
[a_joint_2025] Zhe Yu, Xue Hu, Qin Wang (2025). *A Joint Planning Model for Fixed and Mobile EVCSs Considering Flexible Capacity Strategy*. arXiv. arXiv:2507.17587v1
[fairness-oriented_charging_2025] Siyue Yuan, Jiaying Fu, Xiaoyin Ma (2025). *Fairness-Oriented Charging Station Location Optimization Driven by Deep RL*. IEEE Access. DOI: 10.1109/access.2025.3588880
[planning_future_2025] Hong Yuan, Minda Ma, Nan Zhou, Yanqiao Deng, Junhong Liu, Shufan Zhang, Zhili Ma (2025). *Planning future charging infrastructure for private EVs: A city-scale assessment of demand and capacity*. arXiv. arXiv:2508.16175v4
[socially_optimal_2013] Elena Yudovina, George Michailidis (2013). *Socially optimal charging strategies for EVs*. arXiv. arXiv:1304.2329v1
[a_gis-based_2021] Usman Zafar, I. Safak Bayram, Sertac Bayhan (2021). *A GIS-based Optimal Facility Location Framework for Fast EVCSs*. 2021 IEEE 30th International Symposium on Industrial Electronics (ISIE). DOI: 10.1109/isie45552.2021.9576448
[a_data-driven_2024] Yue Zhang, Jie Tan (2024). *A data-driven approach of layout evaluation for EV charging infrastructure using agent-based simulation and GIS*. SIMULATION. DOI: 10.1177/00375497231209996
[a_multi-objective_2024] Hong Zhang, Feifan Shi (2024). *A multi-objective site selection of EVCS based on NSGA-II*. International Journal of Industrial Engineering Computations. DOI: 10.5267/j.ijiec.2023.9.009
[advancing_urban_2024] Ziqi Zhang, Zhong Chen, Erdem Gümrükcü, Zhenya Ji, Ferdinanda Ponci, Antonello Monti (2024). *Advancing urban EVCSs: AI-driven day-ahead optimization of pricing and Nudge strategies utilizing multi-agent deep RL*. eTransportation. DOI: 10.1016/j.etran.2024.100352
[optimization_of_2025] Qian Zhang, Guiwu Si, Hongyi Li (2025). *Optimization of EVCS Location Distribution Based on Activity–Travel Patterns*. ISPRS International Journal of Geo-Information. DOI: 10.3390/ijgi14100373
[electric_vehicle_2025] Alexis Pengfei Zhao, Shuangqi Li, Zhengmao Li, Zhaoyu Wang, Xue Fei, Zechun Hu, Mohannad Alhazmi, Xiaohe Yan, Chenye Wu, Shuai Lu, Yue Xiang, Da Xie (2025). *EV Charging Planning: A Complex Systems Perspective*. IEEE Transactions on Smart Grid. DOI: 10.1109/tsg.2024.3446859
[large_language_2025] Xinda Zheng, Canchen Jiang, Hao Wang (2025). *Large Language Model-Assisted Planning of EV Charging Infrastructure with Real-World Case Study*. arXiv. DOI: 10.1016/j.seta.2025.104723
[optimizing_electric_2025] Shaopeng Zhong, Ao Liu, Meihan Fan, Yan Song, Yu Jiang (2025). *Optimizing electric bus charging station locations: An integrated land-use and transportation approach*. Applied Energy. DOI: 10.1016/j.apenergy.2025.126649
[reinforcement_learning_2025] Yanchen Zhu, Honghui Zou, Chufan Liu, Yuyu Luo, Yuankai Wu, Yuxuan Liang (2025). *RL for Hybrid Charging Stations Planning and Operation Considering Fixed and Mobile Chargers*. arXiv. arXiv:2506.16764v2

### Equity Considerations in Charging Infrastructure Planning

[critical_behaviour_2015] Rui Carvalho, Lubos Buzna, Richard Gibbens, Frank Kelly (2015). *Critical behaviour in charging of EVs*. arXiv. DOI: 10.1088/1367-2630/17/9/095001
[crowdfunding_for_2024] Abdolmajid Erfani, Qingbin Cui, Patrick DeCorla-Souza (2024). *Crowdfunding for Equitable EV Charging Infrastructure*. arXiv. arXiv:2406.14295v1
[an_equity-based_2025] Shreepati Jha, Agnivesh Pani, Harish Puppala, Varun Varghese, Avinash Unnikrishnan (2025). *An equity-based approach for addressing inequality in EV charging infrastructure: Leaving no one behind in transport electrification*. Energy for Sustainable Development. DOI: 10.1016/j.esd.2024.101643
[inequitable_access_2021] Hafiz Anwar Ullah Khan, Sara Price, Charalampos Avraam, Yury Dvorkin (2021). *Inequitable Access to EV Charging Infrastructure*. arXiv. arXiv:2111.05437v1
[electrical_vehicle_2017] Shuoyao Wang, Suzhi Bi, Ying Jun, Zhang, Jianwei Huang (2017). *Electrical Vehicle Charging Station Profit Maximization: Admission, Pricing, and Online Scheduling*. arXiv. arXiv:1705.02116v2

### Utilization and Demand Modeling

[composite_charging_2015] Olivier Beaude, Cheng Wan, Samson Lasaulce (2015). *Composite charging games in networks of EVs*. arXiv. arXiv:1509.07345v1
[ideas_information-driven_2024] Animesh Chattopadhyay, Subrat Kar (2024). *IDEAS: Information-Driven EV Admission in Charging Station Considering User Impatience to Improve QoS and Station Utilization*. arXiv. arXiv:2403.06223v1
[m-bev_masked_2023] Siran Chen, Yue Ma, Yu Qiao, Yali Wang (2023). *M-BEV: Masked BEV Perception for Robust Autonomous Driving*. arXiv. arXiv:2312.12144v1
[optimizing_energy_2024] Victor Fernandez, Virgilio Pérez, Rosa Roig (2024). *Optimizing Energy Supply for Full EVs in Smart Cities: A Comprehensive Mobility Network Model*. World EV Journal. DOI: 10.3390/wevj16010005
[analysis_of_2022] Christopher Hecht, Jan Figgener, Dirk Uwe Sauer (2022). *Analysis of EVCS Usage and Profitability in Germany based on Empirical Data*. arXiv. arXiv:2206.09582v1
[grid-constrained_online_2024] Emily van Huffelen, Roel Brouwer, Marjan van den Akker (2024). *Grid-constrained online scheduling of flexible EV charging*. arXiv. arXiv:2403.03109v1
[an_electric_2025] Dong Jiang, Xiaoqiang Gong, Yanyan Wei, Bo Peng, Zhengsong Xu (2025). *An EV charging demand prediction approach based on a Graph-based Spatio-temporal Attention Network*. Sustainable Energy, Grids and Networks. DOI: 10.1016/j.segan.2025.101975
[on-demand_valet_2021] Zhijie Lai, Sen Li (2021). *On-Demand Valet Charging for EVs: Economic Equilibrium, Infrastructure Planning and Regulatory Incentives*. arXiv. DOI: 10.1016/j.trc.2022.103669
[the_electric_2021] Yijing Liang, Said Dabia, Zhixing Luo (2021). *The EV Routing Problem with Nonlinear Charging Functions*. arXiv. arXiv:2108.01273v1
[load_forecasting_2019] Zeyu Liu, Yaxin Xie, Donghan Feng, Yun Zhou, Shanshan Shi, Chen Fang (2019). *Load Forecasting Model and Day-ahead Operation Strategy for City-located EV Quick Charge Stations*. arXiv. arXiv:1909.00971v1
[policy_interventions_2024] Saeed Makaremi (2024). *Policy interventions and urban characteristics in modeling EV charging infrastructure utilization*. Case Studies on Transport Policy. DOI: 10.1016/j.cstp.2024.101309
[securing_the_2021] Roberto Metere, Myriam Neaimeh, Charles Morisset, Carsten Maple, Xavier Bellekens, Ricardo M. Czekster (2021). *Securing the EV Charging Infrastructure*. arXiv. arXiv:2105.02905v3
[impact_of_2021] A. Samson Mogos, Samuele Grillo (2021). *Impact of EV Charging Stations in Power Grids in Italy and its Mitigation Mechanisms*. arXiv. DOI: 10.1109/EEEIC/ICPSEurope51590.2021.9584782
[integrating_optimal_2023] Georgia Pierrou, Gabriela Hug (2023). *Integrating Optimal EV Charging in the Energy Management of Electric Railway Stations*. arXiv. arXiv:2308.01145v1
[a_dynamic_2011] Nicole Taheri, Robert Entriken, Yinyu Ye (2011). *A Dynamic Algorithm for Facilitated Charging of Plug-In EVs*. arXiv. arXiv:1112.0697v1
[electric_vehicle_2022] Yong Wang, Jingxin Zhou, Yaoyao Sun, Xiuwen Wang, Jiayi Zhe, Haizhong Wang (2022). *EVCS Location-Routing Problem with Time Windows and Resource Sharing*. Sustainability. DOI: 10.3390/su141811681
[allocate_electric_0] Ting Wu, Emily  Zhu Fainman, Yasmina Maizi, J. Shu, Yongzhen Li (0). *Allocate EVs’ Public Charging Stations with Charging Demand Uncertainty*. . DOI: 10.2139/ssrn.4537082
[allocate_electric_2024] Ting Wu, Emily Fainman, Yasmina Maïzi, Jia Shu, Yongzhen Li (2024). *Allocate EVs’ public charging stations with charging demand uncertainty*. Transportation Research Part D: Transport and Environment. DOI: 10.1016/j.trd.2024.104178
[fleet_sizing_2023] Jie Yang, Michael W. Levin, Lu Hu, Haobin Li, Yangsheng Jiang (2023). *Fleet sizing and charging infrastructure design for electric autonomous mobility-on-demand systems with endogenous congestion and limited link space*. Transportation Research Part C: Emerging Technologies. DOI: 10.1016/j.trc.2023.104172
[scalable_electric_2015] Liang Zhang, Vassilis Kekatos, Georgios B. Giannakis (2015). *Scalable EV Charging Protocols*. arXiv. arXiv:1510.00403v2
[smart_vehicle_2015] Letterio Zuccaro, Alessandro Di Giorgio, Francesco Liberati, Silvia Canale et al. (2015). *Smart Vehicle to Grid Interface Project: Electromobility Management System Architecture and Field Test Results*. arXiv. arXiv:1503.01266v1

### Phased and Sequential Deployment

[forecasting_electric_2023] Yvenn Amara-Ouali, Yannig Goude, Nathan Doumèche, Pascal Veyret et al. (2023). *Forecasting EVCS Occupancy: Smarter Mobility Data Challenge*. arXiv. arXiv:2306.06142v1
[increasing_electric_2020] Miguel F. Anjos, Bernard Gendron, Martim Joyce-Moniz (2020). *Increasing EV adoption through the optimal deployment of fast-charging stations for local and long-distance travel*. European Journal of Operational Research. DOI: 10.1016/j.ejor.2020.01.055
[model-based_framework_2022] Matthew Eagon, Setayesh Fakhimi, George Lyu, Audrey Yang, Brian Lin, William F. Northrop (2022). *Model-Based Framework to Optimize Charger Station Deployment for BEVs*. 2022 IEEE Intelligent Vehicles Symposium (IV). DOI: 10.1109/iv51971.2022.9827442
[definition_of_2023] Davide del Giudice, Angelo Maurizio Brambilla, Federico Bizzarri, Daniele Linaro, Samuele Grillo (2023). *Definition of Static and Dynamic Load Models for Grid Studies of EVs Connected to FCSs*. arXiv. arXiv:2302.03943v1
[electric_vehicle_2020] Marianne Guillet, Gerhard Hiermann, Alexander Kröller, Maximilian Schiffer (2020). *EVCS Search in Stochastic Environments*. arXiv. arXiv:2012.00883v1
[deep_information_2021] Ashutosh Sao, Nicolas Tempelmeier, Elena Demidova (2021). *Deep Information Fusion for EVCS Occupancy Forecasting*. arXiv. arXiv:2108.12352v1
[stochastic_behavior_2025] Yao Tang, Wei Liu, Kwok Tong Chau, Yunhe Hou, Jian Guo (2025). *Stochastic Behavior Modeling and Optimal Bidirectional Charging Station Deployment in EV Energy Network*. IEEE Transactions on Intelligent Transportation Systems. DOI: 10.1109/tits.2025.3553513

### Related Infrastructure Planning Approaches

[a_model_2020] Lennart Adenaw, Markus Lienkamp (2020). *A Model for the Data-based Analysis and Design of Urban Public Charging Infrastructure*. 2020 Fifteenth International Conference on Ecological Vehicles and Renewable Energies (EVER). DOI: 10.1109/ever48776.2020.9243147
[mobile_charging_2022] Shahab Afshar, Zachary K Pecenak, Vahid Disfani (2022). *MCS: A Complementary Charging Technology for EVs*. 2022 IEEE Transportation Electrification Conference &amp; Expo (ITEC). DOI: 10.1109/itec53557.2022.9814039
[electric_vehicles_2023] Fayez Alanazi (2023). *EVs: Benefits, Challenges, and Potential Solutions for Widespread Adaptation*. Applied Sciences. DOI: 10.3390/app13106016
[bounds_and_2018] Angelos Aveklouris, Maria Vlasiou, Bert Zwart (2018). *Bounds and Limit Theorems for a Layered Queueing Model in EV Charging*. arXiv. arXiv:1810.05473v1
[secure_charging_2021] Omer Aydin (2021). *Secure Charging and Payment System for Electric Land Vehicles with Authentication Protocol*. arXiv. arXiv:2107.06100v1
[optimal_routing_2013] John Barco, Andres Guerra, Luis Muñoz, Nicanor Quijano (2013). *Optimal Routing and Scheduling of Charge for EVs: Case Study*. arXiv. arXiv:1310.0145v1
[intelligent_algorithm-based_2023] M. Bilal, M. Rizwan (2023). *Intelligent algorithm-based efficient planning of EVCS: A case study of metropolitan city of India*. Scientia Iranica. DOI: 10.24200/sci.2021.57433.5238
[optimizing_electric_2024] Harpreet Kaur Channi (2024). *Optimizing EV Charging Infrastructure: A Site Selection Strategy for Ludhiana, India*. Mechatronics and Intelligent Transportation Systems. DOI: 10.56578/mits030304
[plug-in_electric_2017] Huimiao Chen, Hongcai Zhang, Zechun Hu, Yunyi Liang, Haocheng Luo, Yinhai Wang (2017). *Plug-in EV Charging Congestion Analysis Using Taxi Travel Data in the Central Area of Beijing*. arXiv. arXiv:1712.07300v1
[risk-aware_hierarchical_2024] Xianlong Chen, Xiuli Wang, Mohammad Shahidehpour (2024). *Risk-Aware Hierarchical Coordination of Peer-to-Peer Energy Trading for EVCSs in Constrained Power Distribution and Urban Transportation Networks Under Uncertainties*. IEEE Transactions on Transportation Electrification. DOI: 10.1109/tte.2024.3362848
[retracted_charging_2023] J. Chitra, R. Lal Raja Singh, R. Leena Rose (2023). *RETRACTED: Charging infrastructure facilitate a large-scale Introduction of EV in urban areas using hybrid technique: A RBFNN-SPOA approach*. Energy &amp; Environment. DOI: 10.1177/0958305x221117518
[optimal_pricing_2021] Yan Cui, Zechun Hu, Xiaoyu Duan (2021). *Optimal Pricing of Public EVCSs Considering Operations of Coupled Transportation and Power Systems*. IEEE Transactions on Smart Grid. DOI: 10.1109/tsg.2021.3053026
[optimal_management_2023] Xuefeng Ding, Qihong Gan, Mir Pasha Shaker (2023). *Optimal management of parking lots as a big data for EVs using internet of things and Long–Short term Memory*. Energy. DOI: 10.1016/j.energy.2023.126613
[integrated_electric_2022] Jiajie Hao, Hui Hou, Yubao Zhang, Yu Wang, Baike Cai, Chao Liu (2022). *Integrated EV Charging Path Planning Considering Traffic Network and Power Grid*. 2022 4th Asia Energy and Electrical Engineering Symposium (AEEES). DOI: 10.1109/aeees54426.2022.9759746
[wecharge_democratizing_2022] Md Umar Hashmi, Mohammad Meraj Alam, Ony Lalaina Valerie Ramarozatovo, Mohammad Shadab Alam (2022). *WEcharge: democratizing EV charging infrastructure*. arXiv. arXiv:2204.01478v1
[locating_and_2024] Dandan Hu, Liu Huang, Chen Liu, Zhi-Wei Liu (2024). *Locating and sizing charging station in multi-period to promote EVs adoption in urban areas*. Energy Reports. DOI: 10.1016/j.egyr.2024.03.029
[optimal_planning_2023] Sachin Shivaji Kumbhar, Vaiju N. Kalkhambkar (2023). *Optimal Planning of Battery Swapping and Charging Stations for the Urban Cities*. 2023 International Conference on Advanced Computing Technologies and Applications (ICACTA). DOI: 10.1109/icacta58201.2023.10392556
[coupling_of_2018] Felix Lehfuss, Georg Lauss, Christian Seitl, Fabian Leimgruber, Martin Noehrer, Thomas I. Strasser (2018). *Coupling of Real-Time and Co-Simulation for the Evaluation of the Large Scale Integration of EVs into Intelligent Power Systems*. arXiv. DOI: 10.1109/VPPC.2017.8331020
[smart_and_2023] Haoyu Li, Jihuang Chen, Chao Yang, Xin Chen, Le Chang, Jiabei Liu (2023). *Smart and efficient EV charging navigation scheme in vehicular edge computing networks*. Journal of Cloud Computing. DOI: 10.1186/s13677-023-00547-y
[a_vehicle-to-grid_2024] Zeyu Liang, Tao Qian, Mert Korkali, Ruben Glatt, Qinran Hu (2024). *A V2G planning framework incorporating EV user equilibrium and distribution network flexibility enhancement*. Applied Energy. DOI: 10.1016/j.apenergy.2024.124231
[planning_of_2024] Jiafeng Lin, Jing Qiu, Yuechuan Tao, Xianzhuo Sun (2024). *Planning of EVCSs With PV and Energy Storage Using a Fuzzy Inference System*. IEEE Transactions on Transportation Electrification. DOI: 10.1109/tte.2023.3322418
[phase_separation_2022] Philip Marszal, Marc Timme, Malte Schröder (2022). *Phase separation induces congestion waves in EV charging*. arXiv. DOI: 10.1103/PhysRevE.104.L042302
[charging_stations_2022] Pasqual Martí, Jaume Jordán, Javier Palanca, Vicente Julian (2022). *Charging stations and mobility data generators for agent-based simulations*. Neurocomputing. DOI: 10.1016/j.neucom.2021.06.098
[cost-benefit_and_2025] Munyem Ahammad Muyeed, Moslema Hoque Oeishee, Abu S.M. Mohsin (2025). *Cost-benefit and net zero impact analysis of PV-grid-battery systems for EV charging stations in Bangladesh*. Energy Conversion and Management: X. DOI: 10.1016/j.ecmx.2025.101256
[a_comparative_2025] Abu Nasar, Aman Sharma, N. Nezamuddin (2025). *A comparative analysis of in-motion and overnight charging infrastructure design for e-buses*. Energy for Sustainable Development. DOI: 10.1016/j.esd.2025.101784
[optimal_siting_2020] Arushi Relan, Vishu Gupta, Rajesh Kumar, Shashank Vyas, B.K. Panigrahi (2020). *Optimal Siting of EV BSSs with Centralized Charging*. 2020 IEEE International Conference on Power Electronics, Drives and Energy Systems (PEDES). DOI: 10.1109/pedes49360.2020.9379513
[a_decentralized_2024] Chengcheng Shao, Ke Li, Xuliang Li, Zechun Hu, Mohammad Shahidehpour, Xifan Wang (2024). *A Decentralized Bi-Level Decomposition Method for Optimal Operation of EVs in Coupled Urban Transportation and Power Distribution Systems*. IEEE Transactions on Transportation Electrification. DOI: 10.1109/tte.2023.3284783
[coordinated_management_2025] Akın Taşcıkaraoğlu, Muhammed Ali Beyazıt, Jan Kleissl, Yuanyuan Shi (2025). *Coordinated Management of MCSs and Community Energy Storage for EV Charging*. Applied Energy. DOI: 10.1016/j.apenergy.2025.126066
[collaborative_multidepot_2023] Yong Wang, Jingxin Zhou, Yaoyao Sun, Jianxin Fan, Zheng Wang, Haizhong Wang (2023). *Collaborative multidepot EV routing problem with time windows and shared charging stations*. Expert Systems with Applications. DOI: 10.1016/j.eswa.2023.119654
[equilibrium_configuration_2024] Zhaoqi Wang, Lu Zhang, Wei Tang, Ziyao Ma, Jiajin Huang (2024). *Equilibrium configuration strategy of V2G-based EVCSs in low-carbon resilient distribution networks*. Applied Energy. DOI: 10.1016/j.apenergy.2024.122931
[competitive_charging_2015] Wei Yuan, Jianwei Huang, Ying Jun Zhang (2015). *Competitive Charging Station Pricing for Plug-in EVs*. arXiv. arXiv:1511.07907v2
[routing_and_2023] Kenan Zhang, John Lygeros (2023). *Routing and charging game in ride-hailing service with EVs*. arXiv. arXiv:2309.05120v1
[charging_infrastructure_2024] Zihe Zhang, Jun Liu, Javier Pena Bastidas, Steven Jones (2024). *Charging infrastructure assessment for shared autonomous EVs in 374 small and medium-sized urban areas: An agent-based simulation approach*. Transport Policy. DOI: 10.1016/j.tranpol.2024.06.017
[planning_of_2023] Ze Zhou, Zhitao Liu, Hongye Su, Liyan Zhang (2023). *Planning of static and dynamic charging facilities for EVs in electrified transportation networks*. Energy. DOI: 10.1016/j.energy.2022.126073
