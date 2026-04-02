============================================================
README – Training and Population Data
============================================================

This directory contains data related to feature attribution,
pruning analysis, and overall model evaluation.

------------------------------------------------------------
# DataFrozenTraining
------------------------------------------------------------

Contains data from the frozen training setting (Section 4.2),
including results obtained using:
- SHAP
- Permutation Feature Importance (PFI)
- ISP applied in the frozen training setup

------------------------------------------------------------
# PopulationData
------------------------------------------------------------

Core dataset of the study.

Contains data for:
- All pruning schemes (input features, tensor bases, combined)
- All variants (baseline, post-hoc, ISP)
- All investigated flow cases

Additionally includes:
- Data used for the generalization analysis
- Data used for the complexity analysis

------------------------------------------------------------
# Notes
------------------------------------------------------------

- PopulationData represents the central repository of all
  evaluated model configurations and results.
- DataFrozenTraining focuses specifically on attribution
  analysis under frozen training conditions.
