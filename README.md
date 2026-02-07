📚 AI Study Planner (MVP)

An AI-powered study planning system that intelligently allocates study time across subjects and topics based on difficulty, confidence level, and available study hours.

This project was built as an MVP (Minimum Viable Product) to demonstrate how AI-driven logic can help students plan their studies more effectively.

🚀 Features

📊 Subject-wise study hour allocation

🧠 Topic-level breakdown (strong vs weak areas)

⏱️ Dynamic time distribution based on available weekday/weekend hours

🔴 Weak-topic prioritization

⚡ FastAPI backend with validation

🧪 Swagger UI for easy testing

🛠️ Tech Stack
Backend

Python

FastAPI

Pydantic

Uvicorn

Frontend (Basic MVP)

React (Create React App)

Fetch API (for backend communication)

📁 Project Structure
ai-study-planner/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── scheduler.py
│   ├── requirements.txt
│
└── frontend/
    ├── public/
    ├── src/
    │   ├── App.js
    │   ├── StudyPlanner.js
    │   ├── index.js
    │   └── index.css

⚙️ How It Works

User Input

Student details

Subjects with:

credits

confidence level

strong topics

weak topics

Available study hours (weekday + weekend)

Backend Logic

Calculates total weekly study hours

Distributes hours evenly across subjects

Allocates:

60% time to weak topics

40% time to strong topics

Output

Weekly study plan

Topic-level hour breakdown

Weak topics are clearly highlighted

🧪 API Usage
Endpoint
POST /generate-plan

Sample Request
{
  "name": "Aman",
  "college": "XYZ Institute of Technology",
  "branch": "CSE",
  "graduation_year": 2026,
  "email": "aman@example.com",
  "subjects": [
    {
      "name": "Data Structures",
      "credits": 4,
      "confidence": 3,
      "strong_areas": ["Arrays", "Linked Lists"],
      "weak_areas": ["Trees", "Graphs"]
    }
  ],
  "weekday_hours": 3,
  "weekend_hours": 6,
  "preferred_time": "Night",
  "target_date": "2026-03-15"
}

Sample Response
{
  "schedule": [
    {
      "subject": "Data Structures",
      "weekly_hours": 13.5,
      "topics": [
        { "name": "Trees", "hours": 4.1, "level": "weak" },
        { "name": "Graphs", "hours": 4.1, "level": "weak" },
        { "name": "Arrays", "hours": 2.7, "level": "strong" }
      ]
    }
  ]
}

▶️ How to Run Locally
Backend
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload


Open:

http://127.0.0.1:8000/docs

Frontend
cd frontend
npm install
npm start


Open:

http://localhost:3000

🎯 Use Case

College students preparing for exams

Competitive exam aspirants

Anyone who wants a structured, weakness-focused study plan

🔮 Future Enhancements

📅 Calendar-based study schedule

🔄 Confidence updates & plan regeneration

📈 Progress tracking

🎨 Improved UI with Tailwind CSS

🔗 Authentication & user profiles

🏁 Conclusion

The AI Study Planner MVP demonstrates how intelligent scheduling can help students focus on what matters most — their weak areas — while maintaining balanced study coverage.

This project serves as a strong foundation for a full-scale AI-based learning assistant.
