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

**Day 1:** Review fundamentals  
**Day 2:** Watch tutorials and take notes  
**Day 3:** Practice exercises  
**Day 4:** Build a mini project  
**Day 5:** Review mistakes and improve code  
**Day 6:** Practice interview questions  
**Day 7:** Update tracker and reflect on progress  

### Advice
Consistency beats intensity. Small daily progress compounds quickly.
"""