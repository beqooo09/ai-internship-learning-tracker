def generate_learning_recommendations(data):
    recommendations = []

    topic_hours = data.groupby("Topic")["Hours"].sum()

    low_hour_topics = topic_hours.sort_values().head(3)

    for topic, hours in low_hour_topics.items():
        recommendations.append(
            f"Increase focus on {topic} (currently {hours} learning hours)."
        )

    in_progress_tasks = data[data["Status"] == "In Progress"]

    if len(in_progress_tasks) > 0:
        top_task = in_progress_tasks.sort_values(
            by="Hours",
            ascending=False
        ).iloc[0]

        recommendations.append(
            f"Prioritize completing '{top_task['Task']}' to improve progress consistency."
        )

    completed_tasks = len(data[data["Status"] == "Completed"])

    if completed_tasks >= 10:
        recommendations.append(
            "You have strong foundational progress. Consider building larger end-to-end AI projects."
        )

    return recommendations