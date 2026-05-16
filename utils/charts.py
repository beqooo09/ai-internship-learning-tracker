import plotly.express as px


def apply_dark_chart_style(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#f8fafc",
        height=450
    )

    return fig


def create_status_pie_chart(data):
    status_counts = data["Status"].value_counts()

    fig = px.pie(
        values=status_counts.values,
        names=status_counts.index,
        title="Task Status Distribution",
        hole=0.35
    )

    return apply_dark_chart_style(fig)


def create_topic_hours_chart(data):
    topic_hours = (
        data.groupby("Topic")["Hours"]
        .sum()
        .sort_values(ascending=False)
    )

    fig = px.bar(
        x=topic_hours.index,
        y=topic_hours.values,
        labels={"x": "Topic", "y": "Learning Hours"},
        title="Learning Hours by Topic"
    )

    fig.update_layout(xaxis_tickangle=-35)

    return apply_dark_chart_style(fig)