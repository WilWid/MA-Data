============================================================
README – DataFrozenTraining
============================================================

This directory contains data and scripts related to the
frozen training analysis (Section 4.2), including feature
importance evaluations and visualization tools.

------------------------------------------------------------
# PFI
------------------------------------------------------------

Contains results from Permutation Feature Importance (PFI).

Files:
- FrozenTraining*.txt
- FrozenTraining*50.txt  
  Summarize feature importances obtained from frozen training
  runs.

- *.json  
  Store raw data from the frozen training runs.

- *_on_data.ipynb  
  Notebooks used to process and evaluate PFI results.

------------------------------------------------------------
# SHAP
------------------------------------------------------------

Contains results from SHAP-based feature attribution.

Files:
- FrozenTraining*.txt
- FrozenTraining*50.txt  
  Summarize feature importances obtained from frozen training
  runs.

- *.json  
  Store raw data from the frozen training runs.

- *_on_data.ipynb  
  Notebooks used to process and evaluate SHAP results.

------------------------------------------------------------
# VIMFrozen
------------------------------------------------------------

Contains scripts for analysis and visualization of feature
importance measures in the frozen training setting.

Files:
- VIMFrozen.py  
  Generates summary tables from the frozen training data.

- VIMPlot.py  
  Generates plots based on the processed data.

------------------------------------------------------------
# Notes
------------------------------------------------------------

- Text files contain processed importance values and serve as
  input for analysis and plotting.
- JSON files store raw outputs from frozen training runs.
- Notebooks are used for intermediate evaluation and data
  handling.
- VIMFrozen provides additional aggregation and visualization
  of the results.
