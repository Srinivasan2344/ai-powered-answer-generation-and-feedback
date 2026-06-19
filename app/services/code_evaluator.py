from difflib import SequenceMatcher


def evaluate_code(expected_code, student_code):

    similarity = SequenceMatcher(
        None,
        expected_code.strip(),
        student_code.strip()
    ).ratio()

    score = round(similarity * 10, 2)

    if score >= 8:
        feedback = "Code closely matches the expected solution."
    elif score >= 5:
        feedback = "Code is partially correct. Review the logic."
    else:
        feedback = "Code differs significantly from the expected solution."

    return {
        "score": score,
        "similarity": round(similarity * 100, 2),
        "feedback": feedback
    }