# =========================
# PROGRESS ANALYTICS
# =========================

st.subheader("Learning Progress Analytics")

# Calculate stats
total_tasks = len(df)

completed_tasks = len(df[df["Status"] == "Completed"])
in_progress_tasks = len(df[df["Status"] == "In Progress"])
not_started_tasks = len(df[df["Status"] == "Not Started"])

completion_rate = round((completed_tasks / total_tasks) * 100, 1)

# Metrics row
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("In Progress", in_progress_tasks)
col4.metric("Completion %", f"{completion_rate}%")