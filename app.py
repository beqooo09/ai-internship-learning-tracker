import streamlit as st
import pandas as pd
import plotly.express as px

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
# SIDEBAR FILTERS
# =========================

st.sidebar.header("Filter Learning Tasks")

selected_topics = st.sidebar.multiselect(
    "Select Topic",
    options=df["Topic"].unique(),
    default=df["Topic"].unique()
)

selected_status = st.sidebar.multiselect(
    "Select Status",
    options=df["Status"].unique(),
    default=df["Status"].unique()
)

# Apply filters
filtered_df = df[
    (df["Topic"].isin(selected_topics)) &
    (df["Status"].isin(selected_status))
]

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

total_tasks = len(filtered_df)

completed_tasks = len(
    filtered_df[filtered_df["Status"] == "Completed"]
)

in_progress_tasks = len(
    filtered_df[filtered_df["Status"] == "In Progress"]
)

not_started_tasks = len(
    filtered_df[filtered_df["Status"] == "Not Started"]
)

completion_rate = (
    round((completed_tasks / total_tasks) * 100, 1)
    if total_tasks > 0 else 0
)

st.subheader("Learning Progress Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("In Progress", in_progress_tasks)
col4.metric("Completion %", f"{completion_rate}%")

# =========================
# CHARTS
# =========================

st.subheader("Learning Analytics")

chart_col1, chart_col2 = st.columns(2)

# PIE CHART

status_counts = filtered_df["Status"].value_counts()

fig_pie = px.pie(
    values=status_counts.values,
    names=status_counts.index,
    title="Task Status Distribution"
)

chart_col1.plotly_chart(fig_pie, use_container_width=True)

# BAR CHART

topic_counts = filtered_df["Topic"].value_counts()

fig_bar = px.bar(
    x=topic_counts.index,
    y=topic_counts.values,
    labels={"x": "Topic", "y": "Number of Tasks"},
    title="Tasks by Topic"
)

chart_col2.plotly_chart(fig_bar, use_container_width=True)

# =========================
# DATA TABLE
# =========================

st.subheader("Learning Tasks")

st.dataframe(filtered_df, use_container_width=True)

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
st.caption("Built with Python, Pandas, Streamlit, and Plotly.")