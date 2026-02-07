def calculate_priority(subject):
    return (
        subject.credits * 0.4
        + (6 - subject.confidence) * 0.4
        + len(subject.weak_areas) * 0.2
    )

def generate_schedule(data):
    schedules = []

    total_weekly_hours = (data.weekday_hours * 5) + (data.weekend_hours * 2)

    subject_priorities = [
        calculate_priority(sub) for sub in data.subjects
    ]
    total_priority = sum(subject_priorities)

    for subject in data.subjects:
        subject_hours = round(
            (calculate_priority(subject) / total_priority)
            * total_weekly_hours,
            1
        )

        topics = []
        weak_weight = 0.6
        strong_weight = 0.4

        weak_hours = subject_hours * weak_weight
        strong_hours = subject_hours * strong_weight

        if subject.weak_areas:
            per_weak = round(weak_hours / len(subject.weak_areas), 2)
            for t in subject.weak_areas:
                topics.append({
                    "name": t,
                    "hours": per_weak,
                    "level": "weak"
                })

        if subject.strong_areas:
            per_strong = round(strong_hours / len(subject.strong_areas), 2)
            for t in subject.strong_areas:
                topics.append({
                    "name": t,
                    "hours": per_strong,
                    "level": "strong"
                })

        schedules.append({
            "subject": subject.name,
            "weekly_hours": subject_hours,
            "topics": topics
        })

    return schedules
