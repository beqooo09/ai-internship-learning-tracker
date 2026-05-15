import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI

st.set_page_config(
    page_title="AI Internship Learning Tracker",
    layout="wide"
)

df = pd.read_csv("learning_data.csv")


def generate_rule_based_recommendations(data):
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
        weakest_topic = incomplete_tasks["Topic"].value_counts().idxmax()
        recommendations.append(
            f"You have the most unfinished work in **{weakest_topic}**. Spend extra time there this week."
        )

    total_hours = data["Hours"].sum()

    if total_hours < 20:
        recommendations.append(
            "Your logged learning hours are still low. Try to reach at least **20 hours** as your next milestone."
        )
    else:
        recommendations.append(
            "Good progress on learning hours. Keep balancing theory with practical projects."
        )

    not_started = data[data["Status"] == "Not Started"]

    if len(not_started) > 0:
        next_task = not_started.iloc[0]
        recommendations.append(
            f"Start **{next_task['Task']}** next to avoid leaving too many tasks untouched."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Great work. All visible tasks are completed. Add more advanced tasks to keep progressing."
        )

    return recommendations


def generate_gpt_study_plan(data, user_goal):
    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        learning_summary = data.to_string(index=False)

        prompt = f"""
You are an AI internship study coach.

Current learning tracker data:
{learning_summary}

User goal:
{user_goal}

Create a practical 7-day study plan.
"""

        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        return response.output_text

    except Exception:
        incomplete_tasks = data[data["Status"] != "Completed"]
        high_priority_tasks = incomplete_tasks[
            incomplete_tasks["Priority"] == "High"
        ]

        if len(high_priority_tasks) > 0:
            focus_task = high_priority_tasks.iloc[0]
        elif len(incomplete_tasks) > 0:
            focus_task = incomplete_tasks.iloc[0]
        else:
            return """
### Local AI Study Plan

Great job — all current tasks are completed.

Next step:
- Add advanced AI, SQL, and data engineering tasks
- Build one portfolio project
- Practice explaining your work like in an interview
"""

        topic = focus_task["Topic"]
        task = focus_task["Task"]

        return f"""
### Local AI Study Plan

Because GPT is unavailable right now, this plan was generated using your tracker data.

### Top Priority
Focus on **{task}** in **{topic}**.

### 7-Day Plan

**Day 1:** Review the basics of {topic}  
**Day 2:** Study examples related to {task}  
**Day 3:** Practice small exercises  
**Day 4:** Build a mini project using {topic}  
**Day 5:** Review mistakes and improve notes  
**Day 6:** Practice interview-style questions  
**Day 7:** Update your tracker and mark progress  

### Mini Project Idea
Build a small project related to **{topic}** and document it in your README.

### Motivation
Consistency matters more than speed. Keep building and committing progress.
"""

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

st.title("AI Internship Learning Tracker")

st.markdown("""
Track your AI internship learning progress, skills, priorities, and study goals.
""")

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

st.subheader("Smart Rule-Based Recommendations")

recommendations = generate_rule_based_recommendations(filtered_df)

for recommendation in recommendations:
    st.info(recommendation)

st.subheader("GPT Study Coach")

user_goal = st.text_area(
    "What do you want help with?",
    placeholder="Example: Help me prepare for an AI internship interview using my current learning tracker."
)

if st.button("Generate AI Study Plan"):
    if user_goal.strip() == "":
        st.warning("Please enter a goal first.")
    else:
        with st.spinner("Generating your AI study plan..."):
            ai_plan = generate_gpt_study_plan(filtered_df, user_goal)
            st.markdown(ai_plan)

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

st.subheader("Priority Distribution")

priority_counts = filtered_df["Priority"].value_counts()

fig_priority = px.bar(
    x=priority_counts.index,
    y=priority_counts.values,
    labels={"x": "Priority", "y": "Tasks"},
    title="Tasks by Priority"
)

st.plotly_chart(fig_priority, use_container_width=True)

st.subheader("Learning Tasks")

st.dataframe(filtered_df, use_container_width=True)

st.subheader("Current Learning Goals")

st.markdown("""
- Prepare for Databricks assessment
- Improve Python and SQL skills
- Understand data engineering workflows
- Build small portfolio projects
- Continue learning machine learning and cloud concepts
""")

st.markdown("---")
st.caption("Built with Python, Pandas, Streamlit, Plotly, rule-based AI, and OpenAI GPT.")