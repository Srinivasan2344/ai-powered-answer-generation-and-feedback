def generate_feedback(score, missing_keywords):

    strengths = []
    improvements = []

    if score >= 8:
        strengths.append(
            "Answer demonstrates good understanding of the topic."
        )

        if len(missing_keywords) <= 1:
            improvements.append(
                "Good answer. Adding a few more technical details would make it more complete."
            )

    elif score >= 5:
        strengths.append(
            "Basic understanding is present."
        )
        improvements.append(
            "Add more detailed explanation and examples."
        )

    else:
        improvements.append(
            "Concept understanding needs improvement."
        )

    if len(missing_keywords) > 1:
        improvements.append(
            f"Missing concepts: {', '.join(missing_keywords[:5])}"
        )

    return {
        "strengths": strengths,
        "improvements": improvements
    }