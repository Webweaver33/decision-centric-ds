Decision-Centric Data Science Platform

This repository contains an end-to-end data science project built to reflect how machine learning systems are actually used in real-world environments, not just in academic exercises or notebooks.

The focus of this project is not only on building a predictive model, but on converting predictions into decisions, measuring business impact, monitoring model behavior over time, and presenting outcomes in a usable format.

Most data science projects stop after model evaluation. This project deliberately goes beyond that.

----------------------------------------------------------------

What makes this project different

Unlike common ML projects that focus only on accuracy or AUC, this system is designed around decisions and outcomes.

Key differences:
- Predictions are translated into concrete actions using a decision threshold
- A business cost framework is used to estimate savings versus a no-model baseline
- Model uncertainty is explicitly handled through confidence-based escalation
- Drift and performance degradation are monitored instead of assumed away
- Outputs are saved and consumed by a separate dashboard instead of staying inside a notebook

This mirrors how machine learning systems are deployed and evaluated in production settings.

----------------------------------------------------------------

Project structure

project_root/
- Untitled1.ipynb  
  End-to-end pipeline covering data preparation, modeling, decision logic, monitoring, and analytics.

- app.py  
  Streamlit dashboard that consumes generated outputs and presents business-facing insights.

- final_decisions.csv  
  Row-level decisions produced by the model, including actions and flags.

- kpi_summary.csv  
  Aggregated business metrics derived from model decisions.

- business_impact.png  
  Visualization comparing expected cost with and without the model.

- prediction_distribution.png  
  Distribution of predicted probabilities with the decision threshold applied.

- requirements.txt  
  Python dependencies required to run the project.

- .gitignore  

----------------------------------------------------------------

Workflow overview

1. Data preparation  
   Raw data is cleaned, missing values are handled, and features are prepared for modeling with a focus on stability and robustness.

2. Modeling  
   A baseline model and an advanced model are trained and evaluated. The final model is selected based on practical performance rather than novelty.

3. Decision logic  
   Model probabilities are converted into actions using a threshold. A business cost matrix is applied to quantify the impact of decisions.

4. Uncertainty and monitoring  
   Low-confidence predictions are identified and flagged. Statistical drift detection and performance decay checks are used to determine retraining needs.

5. Analytics and reporting  
   KPIs, cost comparisons, and diagnostic plots are generated and saved for downstream consumption.

6. Dashboard  
   A Streamlit application presents decisions, metrics, and model health in an accessible format.

----------------------------------------------------------------

How to run the project

1. Install dependencies

   pip install -r requirements.txt

2. Run the pipeline

   Open and execute the notebook:
   Untitled1.ipynb

   This will generate all CSV files and visual outputs used by the dashboard.

3. Launch the dashboard

   streamlit run app.py

   The dashboard will open in a browser window.

----------------------------------------------------------------

How to explain this project in an interview

This project demonstrates how machine learning fits into a decision-making system rather than existing in isolation. It shows how predictions are operationalized, how business impact is measured, and how models are monitored after deployment.

The emphasis is on system thinking, reliability, and business relevance rather than purely on model performance.

----------------------------------------------------------------

Intended use

This repository is meant to showcase applied data science and machine learning system design, especially for roles that value production awareness, decision-making, and business impact.

----------------------------------------------------------------

Note

The models used in this project are intentionally simple. The goal is to demonstrate end-to-end reasoning, monitoring, and decision flow rather than to optimize for marginal accuracy gains.
# decision-centric-ds
