from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict_career
from recommender import skill_gap, get_required_skills
from course_recommender import get_course_recommendations, get_learning_path_priority

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

@app.post("/recommend")
def recommend(data: UserInput):
    career = predict_career(data.skills, data.interest, data.education)
    gaps = skill_gap(data.skills, career)
    required_skills = get_required_skills(career)
    
    # Get prioritized learning path
    prioritized_skills = get_learning_path_priority(gaps, career)
    
    # Get course recommendations for missing skills
    course_suggestions = get_course_recommendations(prioritized_skills)

    return {
        "recommended_career": career,
        "missing_skills": gaps,
        "required_skills": required_skills,
        "total_required": len(required_skills),
        "roadmap": [f"Learn {skill}" for skill in prioritized_skills],
        "course_suggestions": course_suggestions,
        "learning_priority": prioritized_skills
    }
