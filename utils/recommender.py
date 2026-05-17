from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_task_text(row):
    return f"{row['Topic']} {row['Task']}"


def generate_smart_recommendations(data, top_n=3):
    completed_tasks = data[data["Status"] == "Completed"].copy()
    unfinished_tasks = data[data["Status"] != "Completed"].copy()

    if completed_tasks.empty:
        return []

    if unfinished_tasks.empty:
        return []

    completed_tasks["TaskText"] = completed_tasks.apply(build_task_text, axis=1)
    unfinished_tasks["TaskText"] = unfinished_tasks.apply(build_task_text, axis=1)

    all_task_text = list(completed_tasks["TaskText"]) + list(unfinished_tasks["TaskText"])

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(all_task_text)

    completed_vectors = vectors[:len(completed_tasks)]
    unfinished_vectors = vectors[len(completed_tasks):]

    similarity_matrix = cosine_similarity(unfinished_vectors, completed_vectors)

    unfinished_tasks = unfinished_tasks.reset_index(drop=True)
    recommendations = []

    for index, row in unfinished_tasks.iterrows():
        similarity_score = similarity_matrix[index].max()
        score_percentage = round(similarity_score * 100, 1)

        recommendations.append({
            "Topic": row["Topic"],
            "Task": row["Task"],
            "Status": row["Status"],
            "Hours": row["Hours"],
            "Similarity Score": score_percentage
        })

    recommendations = sorted(
        recommendations,
        key=lambda item: item["Similarity Score"],
        reverse=True
    )

    return recommendations[:top_n]