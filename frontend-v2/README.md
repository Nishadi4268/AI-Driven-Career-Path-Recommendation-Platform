# CareerAI Frontend v2

A modern, modular, and accessible UI for career recommendations with intelligent course suggestions.

## Features
- Chips-based skills input (Enter to add, ✕ to remove)
- Clean dark-theme design with responsive cards
- Loading states, toasts, and friendly error messages
- **Smart Course Recommendations**: Get specific courses from Coursera, Udemy, freeCodeCamp, and more
- **Prioritized Learning Paths**: Skills ordered by importance for your target career
- ES modules: `api.js`, `ui.js`, `app.js`
- LocalStorage persistence of skills

## Run
1. Start the backend API:
```bash
# From /backend
python -m uvicorn main:app --reload
```
2. Serve the v2 frontend:
```bash
# From /frontend-v2
python -m http.server 5501
# Open http://127.0.0.1:5501
```

## API Contract
- POST http://127.0.0.1:8000/recommend
- Request JSON: `{ skills: string, interest: string, education: string }`
- Response JSON: 
```json
{
  "recommended_career": "Data Scientist",
  "missing_skills": ["ml", "statistics"],
  "roadmap": ["Learn ml", "Learn statistics"],
  "course_suggestions": [
    {
      "skill": "ml",
      "courses": [
        {
          "title": "Machine Learning Specialization",
          "platform": "Coursera",
          "url": "https://...",
          "duration": "3 months",
          "level": "Intermediate"
        }
      ]
    }
  ],
  "learning_priority": ["ml", "statistics"]
}
```

## What's New in Course Recommendations
- **50+ skills mapped** to 200+ curated courses from top platforms
- Each missing skill shows **2 best courses** with direct links
- Course cards include: platform, duration, difficulty level
- Skills prioritized by career relevance
- Fallback to search links for unmapped skills

## Notes
- Ensure CORS is enabled in `backend/main.py` (already configured).
- If you open `index.html` directly (file://), some browsers may block requests. Prefer the simple HTTP server.
- Course data stored in `backend/course_recommender.py` - easily extensible.
