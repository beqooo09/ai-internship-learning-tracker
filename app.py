import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Internship Learning Tracker",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("learning_data.csv")

# =========================
# TITLE
# =========================

st.title("AI Internship Learning Tracker")

st.markdown("""
Track your AI internship learning progress, skills, and study goals.
""")

# =========================
# LEARNING ANALYTICS
# =========================

total_tasks = len(df)

completed_tasks = len(df[df["Status"] == "Completed"])
in_progress_tasks = len(df[df["Status"] == "In Progress"])
not_started_tasks = len(df[df["Status"] == "Not Started"])

completion_rate = round((completed_tasks / total_tasks) * 100, 1)

st.subheader("Learning Progress Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("In Progress", in_progress_tasks)
col4.metric("Completion %", f"{completion_rate}%")

# =========================
# DATA TABLE
# =========================

st.subheader("Learning Tasks")

st.dataframe(df, use_container_width=True)

# =========================
# GOALS
# =========================

st.subheader("Current Learning Goals")

st.markdown("""
- Prepare for Databricks assessment
- Improve Python and SQL skills
- Understand data engineering workflows
- Build small portfolio projects
- Continue learning machine learning and cloud concepts
""")

# =========================
# FOOTER
# =========================

st.markdown("---")
st.caption("Built with Python, Pandas, and Streamlit.")