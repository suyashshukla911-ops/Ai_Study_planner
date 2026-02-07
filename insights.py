def generate_insights(data, schedule):
    insights = []

    for item in schedule:
        insights.append(
            f"{item['subject']} needs focused attention due to higher difficulty or lower confidence."
        )

    insights.append(
        f"High-focus topics are scheduled during your preferred study time ({data.preferred_time})."
    )

    insights.append(
        "Buffer time is included every week to manage spillovers and revision."
    )

    return insights
