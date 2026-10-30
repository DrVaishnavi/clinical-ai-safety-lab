# Clinical AI Safety Lab

**Where does AI fail clinically, and can AI catch its own failures?**

A clinician-led evaluation project testing large language models on safety-critical healthcare tasks, using one shared clinical rubric and one LLM-as-judge across four modules.

Built by Dr. Vaishnavi Thonge (BDS; MCA in AI & Data Science; 2.5 years evaluating clinical AI output), with AI assistance for code.

## Modules

| # | Module | Question | Data | Status |
|---|---|---|---|---|
| 1 | Patient Q&A traps | Do models miss guideline exceptions and hidden drug risks in patient questions? | 15 synthetic, clinician-verified cases | 🚧 In progress |
| 2 | Clinical summary evaluation | Do AI summaries of patient records hallucinate or omit critical facts? | Synthea synthetic patients | Planned |
| 3 | India extension | Do models handle Indian brand names, Hinglish questions, and Indian medical exam content? | Original India cases + MedMCQA sample | Planned |
| 4 | Guideline RAG | Does grounding a model in clinical guidelines fix the failures found in modules 1–3? | Public guideline text | Planned |

## Approach
- **Ground truth first:** every case has a clinician-written answer key tied to a named guideline.
- **One rubric everywhere:** accuracy, safety, completeness, and a critical-error flag.
- **Human vs. AI judge:** each module compares clinician grades with LLM-as-judge grades, with a focus on dangerous errors the judge misses.

## Data and ethics
All data is synthetic or from public, appropriately licensed sources. No real patient data, no employer data, and no content from any evaluation platform. Free-tier model APIs may use inputs to improve their models, which is one reason only synthetic data is used.

*This project is for research and education. Nothing here is medical advice.*
