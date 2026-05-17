from utils.recommendation_engine import generate_learning_recommendations
import random

import streamlit as st

from utils.ai_coach import generate_local_ai_plan
from utils.charts import create_status_pie_chart, create_topic_hours_chart
from utils.data_manager import load_data, save_data
from utils.interview_questions import INTERVIEW_QUESTIONS


st.set_page_config(
    page_title="AI Internship Learning Tracker",
    page_icon="🚀",
    layout="wide"
)


with open("styles/style.css", encoding="utf-8") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)


df = load_data()


with st.expander("Filter Learning Tasks", expanded=False):
    selected_topics = st.multiselect(
        "Select Topic",
        options=df["Topic"].unique(),
        default=df["Topic"].unique()
    )

    selected_status = st.multiselect(
        "Select Status",
        options=df["Status"].unique(),
        default=df["Status"].unique()
    )


filtered_df = df[
    (df["Topic"].isin(selected_topics)) &
    (df["Status"].isin(selected_status))
]


st.markdown(
    """
    <div class="main-title">AI Internship Learning Tracker</div>
    <div class="subtitle">
        A personal dashboard for tracking internship learning, technical progress,
        AI preparation, and interview readiness.
    </div>
    <span class="badge">Streamlit</span>
    <span class="badge">Python</span>
    <span class="badge">Pandas</span>
    <span class="badge">Plotly</span>
    <span class="badge">Local AI</span>
    """,
    unsafe_allow_html=True
)


st.subheader("Internship Achievements")

achievement_col1, achievement_col2, achievement_col3, achievement_col4 = st.columns(4)

achievement_col1.success("Passed Databricks Assessment")
achievement_col2.info("Built AI Learning Dashboard")
achievement_col3.info("Practiced ETL Pipelines")
achievement_col4.info("Studied Computer Vision")


st.subheader("Add New Learning Task")

with st.form("task_form"):
    form_col1, form_col2 = st.columns(2)

    with form_col1:
        topic = st.text_input("Topic")
        status = st.selectbox(
            "Status",
            ["Not Started", "In Progress", "Completed"]
        )

    with form_col2:
        task = st.text_input("Task")
        hours = st.number_input(
            "Estimated Learning Hours",
            min_value=1,
            max_value=100,
            value=1
        )

    submit_button = st.form_submit_button("Add Task")

    if submit_button:
        if topic.strip() == "" or task.strip() == "":
            st.warning("Please enter both a topic and a task.")
        else:
            new_row = {
                "Topic": topic.strip(),
                "Task": task.strip(),
                "Status": status,
                "Hours": hours
            }

            df.loc[len(df)] = new_row
            save_data(df)

            st.success("Task added successfully! Refresh the app to update filters and charts.")


total_tasks = len(filtered_df)
completed_tasks = len(filtered_df[filtered_df["Status"] == "Completed"])
in_progress_tasks = len(filtered_df[filtered_df["Status"] == "In Progress"])

completion_rate = (
    round((completed_tasks / total_tasks) * 100, 1)
    if total_tasks > 0 else 0
)

total_hours = int(filtered_df["Hours"].sum())


st.subheader("Learning Progress Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("Completion %", f"{completion_rate}%")
col4.metric("Learning Hours", total_hours)


st.subheader("AI Study Coach")

coach_col1, coach_col2 = st.columns([1, 2])

with coach_col1:
    generate_plan = st.button("Generate AI Study Plan", use_container_width=True)

with coach_col2:
    st.caption("Creates a local AI-based 7-day study plan using your incomplete tasks.")

if generate_plan:
    ai_plan = generate_local_ai_plan(filtered_df)
    st.markdown(ai_plan)


st.subheader("Learning Practice")

practice_col1, practice_col2 = st.columns([1, 2])

with practice_col1:
    practice_topic = st.selectbox(
        "Choose an interview topic",
        list(INTERVIEW_QUESTIONS.keys())
    )

    generate_question = st.button(
        "Generate Practice Question",
        use_container_width=True
    )

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if generate_question:
    st.session_state.current_question = random.choice(
        INTERVIEW_QUESTIONS[practice_topic]
    )

with practice_col2:
    if st.session_state.current_question:
        question_data = st.session_state.current_question

        st.markdown("### Interview Question")
        st.info(question_data["question"])

        with st.expander("Show Model Answer"):
            st.markdown(question_data["answer"])

        with st.expander("Show Simple Example"):
            st.markdown(question_data["example"])
    else:
        st.info("Choose a topic and generate a question to start practicing.")


st.subheader("AI Recommendation Engine")

recommendations = generate_learning_recommendations(filtered_df)

for rec in recommendations:
    st.info(rec)



st.subheader("Learning Analytics")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.plotly_chart(
        create_status_pie_chart(filtered_df),
        use_container_width=True
    )

with chart_col2:
    st.plotly_chart(
        create_topic_hours_chart(filtered_df),
        use_container_width=True
    )


st.subheader("Learning Tasks")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


st.markdown("---")
st.caption(
    "Built with Python, Pandas, Streamlit, Plotly, Local AI logic, and interview practice mode."
)