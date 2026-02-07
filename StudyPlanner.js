import { useState } from "react";

export default function StudyPlanner() {
  const [data, setData] = useState(null);

  const generate = async () => {
    const res = await fetch("http://127.0.0.1:8000/generate-plan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: "Aman",
        college: "XYZ Institute",
        branch: "CSE",
        graduation_year: 2026,
        email: "aman@test.com",
        subjects: [
          {
            name: "Data Structures",
            credits: 4,
            confidence: 3,
            strong_areas: ["Arrays", "Linked Lists"],
            weak_areas: ["Trees", "Graphs"]
          },
          {
            name: "Operating Systems",
            credits: 3,
            confidence: 2,
            strong_areas: ["Processes"],
            weak_areas: ["Deadlocks", "Memory"]
          }
        ],
        weekday_hours: 3,
        weekend_hours: 6,
        preferred_time: "Night",
        target_date: "2026-03-15"
      })
    });

    const json = await res.json();
    setData(json.schedule);
  };

  return (
    <div style={{ padding: 30, fontFamily: "Arial" }}>
      <h1>AI Study Planner</h1>
      <button onClick={generate}>Generate Study Plan</button>

      {data &&
        data.map((s, i) => (
          <div key={i} style={{ marginTop: 20 }}>
            <h3>{s.subject} ({s.weekly_hours} hrs/week)</h3>
            {s.topics.map((t, j) => (
              <div key={j}>
                {t.level === "weak" ? "🔴" : "🟢"} {t.name} – {t.hours} hrs
              </div>
            ))}
          </div>
        ))}
    </div>
  );
}
