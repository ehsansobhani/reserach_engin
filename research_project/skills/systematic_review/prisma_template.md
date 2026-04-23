# PRISMA 2020 Template for BEV Charging Infrastructure Review

This template follows the PRISMA 2020 statement (Page et al., 2021) and is adapted for the urban BEV fast-charging rollout planning systematic review.

## Prisma Flow Diagram — Text Representation

```
┌─────────────────────────────────────────────────────────────────┐
│  IDENTIFICATION                                                 │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Records identified from:                                 │   │
│  │   • Database search (arXiv, Semantic Scholar, WoS, TRB)  │   │
│  │   • Backward citation chasing (snowball)                  │   │
│  │   • Forward citation searching                            │   │
│  │   • Expert recommendation                                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Total records: N                                         │   │
│  │   • Database: N1                                        │   │
│  │   • Snowball: N2                                        │   │
│  │   • Other: N3                                           │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘

                          ▼ (remove duplicates)

┌─────────────────────────────────────────────────────────────────┐
│  SCREENING                                                     │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Records screened (title + abstract): N                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│              ┌──────────────────────────┐                       │
│              │ Records excluded: N      │                       │
│              │ Reason: title/abstract   │                       │
│              │ not relevant             │                       │
│              └──────────────────────────┘                       │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Full-text assessed for eligibility: N                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│              ┌──────────────────────────┐                       │
│              │ Full-text excluded: N     │                       │
│              │ Reason: [categorize]      │                       │
│              └──────────────────────────┘                       │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Reports reviewed in detail: N                           │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘

                          ▼ (apply classification)

┌─────────────────────────────────────────────────────────────────┐
│  INCLUDED                                                      │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Papers included in review: N                           │   │
│  │   • Included in qualitative synthesis: N               │   │
│  │   • Included in quantitative analysis (if applicable): N│   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## Search Strings by Database

### arXiv
```
(ev charging infrastructure OR "EV charging" OR "electric vehicle charging")
AND (planning OR placement OR location OR deployment OR rollout)
AND (urban OR city OR "spatial optimization" OR equity OR "land use" OR zoning)
```

### Semantic Scholar
```
Title/Abstract: (EV charging OR electric vehicle charging) AND (infrastructure OR planning OR deployment)
Filter: Computer Science, Engineering, Environmental Science
```

### Web of Science
```
TS = (("EV charging" OR "electric vehicle charging" OR "battery electric vehicle")
AND ("infrastructure planning" OR "charging station placement" OR "deployment strategy"
OR "urban charging" OR "equity" OR "zoning"))
```

### TRB Transportation Research Board
```
Keywords: EV charging infrastructure, urban charging deployment, equity in charging, station location
```

## Inclusion / Exclusion Checklist

Apply to each paper at full-text review stage:

**INCLUDE if ALL of:**
- [ ] Addresses EV charging infrastructure planning (not only vehicle technology)
- [ ] Contains spatial or planning dimension (not purely electrical engineering)
- [ ] Describes methodology (model, data, analysis approach)
- [ ] Peer-reviewed or substantial conference paper
- [ ] English language

**EXCLUDE if ANY of:**
- [ ] Pure V2G (vehicle-to-grid) technical without spatial planning
- [ ] Highway-only corridor focus without urban context
- [ ] No identifiable methodology (poster, workshop abstract, editorial)
- [ ] Not accessible (full text unavailable)
- [ ] Duplicate of already-included paper

## Exclusion Reason Codes

| Code | Reason |
|------|--------|
| E1 | No EV charging infrastructure planning component |
| E2 | No spatial/planning dimension |
| E3 | Insufficient methodology detail |
| E4 | Not peer-reviewed / workshop abstract |
| E5 | Full text unavailable |
| E6 | Duplicate study |
| E7 | Wrong language |

## Stage Counts Log

Maintain these counts throughout the review:

```
Date       | Identified | Screened | Excluded(S) | FullText | Excluded(FT) | Included
-----------|------------|----------|-------------|----------|--------------|----------
YYYY-MM-DD |     N      |    N     |      N      |    N     |      N       |    N
```

## Citation

Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement. BMJ 2021;372:n71. doi: 10.1136/bmj.n71