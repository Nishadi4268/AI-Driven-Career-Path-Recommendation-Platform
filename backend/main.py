from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict_career, get_model_metrics
from recommender import skill_gap, get_required_skills
from course_recommender import get_course_recommendations, get_learning_path_priority
from skill_normalizer import normalize_skills_text
from feedback_store import store_feedback

app = FastAPI()

# Enable CORS for local development (frontend on file:// or different port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    skills: str
    interest: str
    education: str


class FeedbackInput(BaseModel):
    skills: str
    interest: str
    education: str
    recommended_career: str
    selected_career: str | None = None
    helpful: bool | None = None
    comment: str | None = None

@app.post("/recommend")
def recommend(data: UserInput):
    normalized_skills = normalize_skills_text(data.skills)
    career, confidence = predict_career(normalized_skills, data.interest, data.education)
    gaps = skill_gap(normalized_skills, career)
    required_skills = get_required_skills(career)
    model_metrics = get_model_metrics()
    
    # Get prioritized learning path
    prioritized_skills = get_learning_path_priority(gaps, career)
    
    # Get course recommendations for missing skills
    course_suggestions = get_course_recommendations(prioritized_skills)

    return {
        "recommended_career": career,
        "confidence": confidence,
        "model_metrics": model_metrics,
        "missing_skills": gaps,
        "required_skills": required_skills,
        "total_required": len(required_skills),
        "roadmap": [f"Learn {skill}" for skill in prioritized_skills],
        "course_suggestions": course_suggestions,
        "learning_priority": prioritized_skills
    }


@app.post("/feedback")
def feedback(data: FeedbackInput):
    normalized_skills = normalize_skills_text(data.skills)
    record = {
        "skills": normalized_skills,
        "interest": data.interest,
        "education": data.education,
        "recommended_career": data.recommended_career,
        "selected_career": data.selected_career or "",
        "helpful": "" if data.helpful is None else str(data.helpful).lower(),
        "comment": data.comment or "",
    }
    store_feedback(record)
    return {"status": "ok"}
