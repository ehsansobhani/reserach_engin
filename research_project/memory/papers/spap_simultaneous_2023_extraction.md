# Extraction: SPAP: Simultaneous Demand Prediction and Planning for Electric Vehicle Chargers in a New City

**Key:** spap_simultaneous_2023
**Authors:** Yizong Wang, Dong Zhao, Yajie Ren, Desheng Zhang, Huadong Ma
**Year:** 2023
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

<jats:p>
            For a new city that is committed to promoting Electric Vehicles (EVs), it is significant to plan the public charging infrastructure where charging demands are high. However, it is difficult to predict charging demands before the actual deployment of EV chargers for lack of operational data, resulting in a deadlock. A direct idea is to leverage the urban transfer learning paradigm to learn the knowledge from a source city, then exploit it to predict charging demands, and meanwhile determine locations and amounts of slow/fast chargers for charging stations in the target city. However, the demand prediction and charger planning depend on each other, and it is required to re-train the prediction model to eliminate the negative transfer between cities for each varied charger plan, leading to the unacceptable time complexity. To this end, we design an effective solution of
            <jats:underline>S</jats:underline>
            imultaneous Demand
            <jats:underline>P</jats:underline>
            rediction
            <jats:underline>A</jats:underline>
            nd
            <jats:underline>P</jats:underline>
            lanning (
            <jats:italic>SPAP</jats:italic>
            ): discriminative features are extracted from multi-source data, and fed into an Attention-based Spatial-Temporal City Domain Adaptation Network (
            <jats:italic>AST-CDAN</jats:italic>
            ) for cross-city demand prediction; a novel Transfer Iterative Optimization (
            <jats:italic>TIO</jats:italic>
            ) algorithm is designed for charger planning by iteratively utilizing
            <jats:italic>AST-CDAN</jats:italic>
            and a charger plan fine-tuning algorithm. Extensive experiments on real-world datasets collected from three cities in China validate the effectiveness and efficiency of
            <jats:italic>SPAP</jats:italic>
            . Specially,
            <jats:italic>SPAP</jats:italic>
            improves at most 72.5% revenue compared with the real-world charger deployment.
          </jats:p>
