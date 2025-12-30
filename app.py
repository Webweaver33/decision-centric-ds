import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Decision-Centric Data Science Dashboard",
    layout="wide"
)

st.title("Decision-Centric Data Science Platform")

def safe_load_csv(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()

kpi_df = safe_load_csv("kpi_summary.csv")
decision_df = safe_load_csv("final_decisions.csv")

st.header("Key Business Metrics")

if not kpi_df.empty:
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Customers", int(kpi_df["total_customers"][0]))
    col2.metric("Actions Taken", int(kpi_df["actions_taken"][0]))
    col3.metric("Escalations", int(kpi_df["escalations"][0]))
    col4.metric("Business Savings", f"₹ {int(kpi_df['business_savings'][0])}")
else:
    st.warning("KPI data not found.")

st.header("Business Impact")

if os.path.exists("business_impact.png"):
    st.image("business_impact.png")
else:
    st.warning("business_impact.png not found")

st.header("Prediction Distribution")

if os.path.exists("prediction_distribution.png"):
    st.image("prediction_distribution.png")
else:
    st.warning("prediction_distribution.png not found")

st.header("Decision Table")

if not decision_df.empty:
    st.dataframe(decision_df.head(50), use_container_width=True)
else:
    st.warning("Decision data not found")

st.header("Model Health")

if "retrain_required" in decision_df.columns:
    if decision_df["retrain_required"].iloc[0]:
        st.error("Model retraining REQUIRED")
    else:
        st.success("Model healthy — no retraining required")
else:
    st.warning("Drift information missing")
