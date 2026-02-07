from fastapi import FastAPI
from models import StudentInput
from scheduler import generate_schedule
from insights import generate_insights

app = FastAPI(title="AI Study Planner MVP")

@app.post("/generate-plan")
def generate_plan(data: StudentInput):
    schedule = generate_schedule(data)
    insights = generate_insights(data, schedule)

    return {
        "schedule": schedule,
        "insights": insights
    }
