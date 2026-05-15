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

DATA_FILE = "learning_data.csv"

df = pd.read_csv(DATA_FILE)

# =========================
# SAVE FUNCTION
# =========================

def save_data(dataframe):
    dataframe.to_csv(DATA_FILE, index=False)

# =========================
# LOCAL AI STUDY COACH
# =========================

def generate_local_ai_plan(data):

    incomplete_tasks = data[data["Status"] != "Completed"]

    if len(incomplete_tasks) > 0:
        focus_task = incomplete_tasks.iloc[0]
    else:
        return """
### Local AI Study Plan

Excellent progress.

Next steps:
- Add advanced AI tasks
- Build portfolio projects
- Practice technical interviews
"""

    topic = focus_task["Topic"]
    task = focus_task["Task"]

    return f"""
### Local AI Study Plan

### Recommended Focus
Focus on **{task}** in **{topic}**.

### 7-Day Plan

Day 1 → Review fundamentals  
Day 2 → Watch tutorials  
Day 3 → Practice exercises  
Day 4 → Build mini project  
Day 5 → Review mistakes  
Day 6 → Practice interview questions  
Day 7 → Update tracker and reflect

### Advice
Consistency beats intensity. Small daily progress compounds quickly.
"""

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

filtered_df = df[
    (df["Topic"].isin(selected_topics)) &
    (df["Status"].isin(selected_status))
]

# =========================
# TITLE
# =========================

st.title("AI Internship Learning Tracker")

st.markdown("""
Track your AI internship learning progress, goals, and study analytics.
""")

# =========================
# ADD TASK FORM
# =========================

st.subheader("Add New Learning Task")

with st.form("task_form"):

    topic = st.text_input("Topic")
    task = st.text_input("Task")

    status = st.selectbox(
        "Status",
        ["Not Started", "In Progress", "Completed"]
    )

    hours = st.number_input(
        "Estimated Learning Hours",
        min_value=1,
        max_value=100,
        value=1
    )

    submit_button = st.form_submit_button("Add Task")

    if submit_button:

        new_task = pd.DataFrame({
            "Topic": [topic],
            "Task": [task],
            "Status": [status],
            "Hours": [hours]
        })

        df = pd.concat([df, new_task], ignore_index=True)

        save_data(df)

        st.success("Task added successfully!")

# =========================
# ANALYTICS
# =========================

total_tasks = len(filtered_df)

completed_tasks = len(
    filtered_df[filtered_df["Status"] == "Completed"]
)

in_progress_tasks = len(
    filtered_df[filtered_df["Status"] == "In Progress"]
)

completion_rate = (
    round((completed_tasks / total_tasks) * 100, 1)
    if total_tasks > 0 else 0
)

total_hours = filtered_df["Hours"].sum()

st.subheader("Learning Progress Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("Completion %", f"{completion_rate}%")
col4.metric("Learning Hours", total_hours)

# =========================
# LOCAL AI RECOMMENDATIONS
# =========================

st.subheader("AI Study Coach")

if st.button("Generate AI Study Plan"):

    ai_plan = generate_local_ai_plan(filtered_df)

    st.markdown(ai_plan)

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
# DATA TABLE
# =========================

st.subheader("Learning Tasks")

st.dataframe(filtered_df, use_container_width=True)

# =========================
# FOOTER
# =========================

st.markdown("---")
st.caption("Built with Python, Pandas, Streamlit, Plotly, and Local AI logic.")