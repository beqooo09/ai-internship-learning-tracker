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
# AI RECOMMENDATION ENGINE
# =========================

def generate_ai_recommendations(data):
    recommendations = []

    incomplete_tasks = data[data["Status"] != "Completed"]
    high_priority_incomplete = incomplete_tasks[
        incomplete_tasks["Priority"] == "High"
    ]

    if len(high_priority_incomplete) > 0:
        top_task = high_priority_incomplete.iloc[0]
        recommendations.append(
            f"Focus first on **{top_task['Task']}** in **{top_task['Topic']}** because it is high priority and not completed."
        )

    if len(incomplete_tasks) > 0:
        topic_counts = incomplete_tasks["Topic"].value_counts()
        weakest_topic = topic_counts.idxmax()

        recommendations.append(
            f"You have the most unfinished work in **{weakest_topic}**. Spend extra time there this week."
        )

    total_hours = data["Hours"].sum()

    if total_hours < 20:
        recommendations.append(
            "Your total logged learning hours are still low. Try to reach at least **20 hours** as your next milestone."
        )
    else:
        recommendations.append(
            "Good progress on learning hours. Keep balancing practice projects with theory."
        )

    not_started = data[data["Status"] == "Not Started"]

    if len(not_started) > 0:
        next_task = not_started.iloc[0]
        recommendations.append(
            f"Start **{next_task['Task']}** next to avoid leaving too many tasks untouched."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Great work. All visible tasks are completed. Add new advanced tasks to keep progressing."
        )

    return recommendations

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

selected_priority = st.sidebar.multiselect(
    "Select Priority",
    options=df["Priority"].unique(),
    default=df["Priority"].unique()
)

filtered_df = df[
    (df["Topic"].isin(selected_topics)) &
    (df["Status"].isin(selected_status)) &
    (df["Priority"].isin(selected_priority))
]

# =========================
# TITLE
# =========================

st.title("AI Internship Learning Tracker")

st.markdown("""
Track your AI internship learning progress, skills, priorities, and study goals.
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

total_hours = filtered_df["Hours"].sum()

st.subheader("Learning Progress Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("In Progress", in_progress_tasks)
col4.metric("Completion %", f"{completion_rate}%")
col5.metric("Learning Hours", total_hours)

# =========================
# AI RECOMMENDATIONS
# =========================

st.subheader("AI-Powered Study Recommendations")

recommendations = generate_ai_recommendations(filtered_df)

for recommendation in recommendations:
    st.info(recommendation)

# =========================
# CHARTS
# =========================

st.subheader("Learning Analytics")

chart_col1, chart_col2 = st.columns(2)

status_counts = filtered_df["Status"].value_counts()

fig_pie = px.pie(
    values=status_counts.values,
    names=status_counts.index,
    title="Task Status Distribution"
)

chart_col1.plotly_chart(fig_pie, use_container_width=True)

topic_hours = filtered_df.groupby("Topic")["Hours"].sum()

fig_bar = px.bar(
    x=topic_hours.index,
    y=topic_hours.values,
    labels={"x": "Topic", "y": "Learning Hours"},
    title="Learning Hours by Topic"
)

chart_col2.plotly_chart(fig_bar, use_container_width=True)

# =========================
# PRIORITY DISTRIBUTION
# =========================

st.subheader("Priority Distribution")

priority_counts = filtered_df["Priority"].value_counts()

fig_priority = px.bar(
    x=priority_counts.index,
    y=priority_counts.values,
    labels={"x": "Priority", "y": "Tasks"},
    title="Tasks by Priority"
)

st.plotly_chart(fig_priority, use_container_width=True)

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
st.caption("Built with Python, Pandas, Streamlit, Plotly, and rule-based AI recommendations.")