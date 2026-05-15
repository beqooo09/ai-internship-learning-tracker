import random

import pandas as pd
import plotly.express as px
import streamlit as st

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
# INTERVIEW QUESTION BANK
# =========================

INTERVIEW_QUESTIONS = {
    "Python": [
        {
            "question": "What is the difference between a list and a tuple in Python?",
            "answer": "A list is mutable, meaning it can be changed after creation. A tuple is immutable, meaning its values cannot be changed after creation. Lists are useful when data needs to change, while tuples are useful for fixed data.",
            "example": "Example: Use a list for tasks you update. Use a tuple for fixed coordinates like (10, 20)."
        },
        {
            "question": "What is a function in Python?",
            "answer": "A function is a reusable block of code that performs a specific task. It helps reduce repetition and makes code easier to organize and test.",
            "example": "Example: def greet(name): return f'Hello, {name}'"
        },
        {
            "question": "What is a dictionary in Python?",
            "answer": "A dictionary stores data as key-value pairs. It is useful when you want to look up values by a meaningful key.",
            "example": "Example: {'name': 'Beqir', 'skill': 'Python'}"
        }
    ],
    "SQL": [
        {
            "question": "What is the difference between INNER JOIN and LEFT JOIN?",
            "answer": "INNER JOIN returns only matching rows from both tables. LEFT JOIN returns all rows from the left table and matching rows from the right table. If there is no match, the right table columns return NULL.",
            "example": "Example: Use LEFT JOIN when you want all customers even if some have no orders."
        },
        {
            "question": "What is GROUP BY used for?",
            "answer": "GROUP BY is used to group rows that have the same values and apply aggregate functions like COUNT, SUM, AVG, MIN, or MAX.",
            "example": "Example: SELECT department, COUNT(*) FROM employees GROUP BY department;"
        },
        {
            "question": "What is a window function?",
            "answer": "A window function performs a calculation across a set of rows related to the current row without collapsing the rows like GROUP BY does.",
            "example": "Example: ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC)"
        }
    ],
    "Machine Learning": [
        {
            "question": "What is supervised learning?",
            "answer": "Supervised learning is a machine learning approach where the model learns from labeled data. Each training example includes input features and the correct output.",
            "example": "Example: Predicting house prices using historical house data with known prices."
        },
        {
            "question": "What is overfitting?",
            "answer": "Overfitting happens when a model learns the training data too well, including noise, and performs poorly on new unseen data.",
            "example": "Example: A model gets 99% accuracy on training data but only 60% on test data."
        },
        {
            "question": "What is the difference between classification and regression?",
            "answer": "Classification predicts categories or labels. Regression predicts continuous numeric values.",
            "example": "Example: Spam detection is classification. House price prediction is regression."
        }
    ],
    "Deep Learning": [
        {
            "question": "What is a neural network?",
            "answer": "A neural network is a model inspired by the brain. It uses layers of connected nodes to learn patterns from data.",
            "example": "Example: Neural networks can be used for image recognition, text classification, and speech processing."
        },
        {
            "question": "What is an activation function?",
            "answer": "An activation function helps a neural network learn non-linear patterns by deciding how strongly a neuron should activate.",
            "example": "Example: ReLU is commonly used because it is simple and works well in many deep learning models."
        },
        {
            "question": "What is a CNN?",
            "answer": "A Convolutional Neural Network is a deep learning model commonly used for image data. It detects patterns like edges, shapes, and objects.",
            "example": "Example: CNNs are used in facial recognition and medical image analysis."
        }
    ],
    "Cloud": [
        {
            "question": "What is cloud computing?",
            "answer": "Cloud computing means using remote servers over the internet to store, process, and manage data instead of using only a local computer.",
            "example": "Example: Azure, AWS, and Google Cloud provide cloud services."
        },
        {
            "question": "What is scalability in cloud computing?",
            "answer": "Scalability means increasing or decreasing computing resources based on demand.",
            "example": "Example: A website can automatically add more servers during high traffic."
        },
        {
            "question": "What is the difference between IaaS, PaaS, and SaaS?",
            "answer": "IaaS provides infrastructure like servers. PaaS provides a platform for building apps. SaaS provides ready-to-use software.",
            "example": "Example: Azure VMs are IaaS, Azure App Service is PaaS, Gmail is SaaS."
        }
    ],
    "Databricks": [
        {
            "question": "What is Databricks used for?",
            "answer": "Databricks is used for data engineering, data analytics, machine learning, and big data processing using Apache Spark.",
            "example": "Example: A company can use Databricks to process large datasets and build ML pipelines."
        },
        {
            "question": "What is Apache Spark?",
            "answer": "Apache Spark is a distributed data processing engine designed to process large amounts of data quickly across multiple machines.",
            "example": "Example: Spark can process large CSV, Parquet, or Delta tables much faster than traditional single-machine tools."
        },
        {
            "question": "What is a notebook in Databricks?",
            "answer": "A notebook is an interactive workspace where users can write code, run queries, visualize data, and document analysis.",
            "example": "Example: A Databricks notebook can contain Python, SQL, and Markdown in one place."
        }
    ]
}

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
Track your AI internship learning progress, goals, study analytics, and interview preparation.
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
        if topic.strip() == "" or task.strip() == "":
            st.warning("Please enter both a topic and a task.")
        else:
            new_task = pd.DataFrame({
                "Topic": [topic.strip()],
                "Task": [task.strip()],
                "Status": [status],
                "Hours": [hours]
            })

            df = pd.concat([df, new_task], ignore_index=True)
            save_data(df)

            st.success("Task added successfully! Refresh the app to see it in filters.")

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
# LOCAL AI STUDY COACH
# =========================

st.subheader("AI Study Coach")

if st.button("Generate AI Study Plan"):
    ai_plan = generate_local_ai_plan(filtered_df)
    st.markdown(ai_plan)

# =========================
# AI INTERVIEW PRACTICE MODE
# =========================

st.subheader("AI Interview Practice Mode")

practice_topic = st.selectbox(
    "Choose an interview topic",
    list(INTERVIEW_QUESTIONS.keys())
)

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if st.button("Generate Interview Question"):
    st.session_state.current_question = random.choice(
        INTERVIEW_QUESTIONS[practice_topic]
    )

if st.session_state.current_question:
    question_data = st.session_state.current_question

    st.markdown("### Interview Question")
    st.info(question_data["question"])

    with st.expander("Show Model Answer"):
        st.markdown(question_data["answer"])

    with st.expander("Show Simple Example"):
        st.markdown(question_data["example"])

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
st.caption("Built with Python, Pandas, Streamlit, Plotly, Local AI logic, and interview practice mode.")