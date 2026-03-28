from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="MentorAI Agents Layer", description="Handles smart alerts and performance analysis.")

class PerformanceData(BaseModel):
    student_id: str
    marks: list[float]
    contest_rating: int

@app.get("/health")
def health_check():
    return {"status": "AI Agents Layer is active."}

@app.post("/agents/analyze-performance")
def analyze_performance(data: PerformanceData):
    # Heurisitic or AI-based performance analysis
    average = sum(data.marks) / len(data.marks) if data.marks else 0
    insight = ""
    
    if average < 50:
        insight = "Critical: Student requires immediate intervention."
    elif data.contest_rating > 1500:
        insight = "Excellent problem-solving skills. Recommend joining the 'Advanced CP' pathway."
    else:
        insight = "On track. Recommend daily practice problems on LeetCode."
    
    return {"student_id": data.student_id, "insight_generated": insight}

if __name__ == "__main__":
    # Internal agent service runs on a different port
    uvicorn.run(app, host="0.0.0.0", port=8000)
