def calculate_rubric(
    similarity,
    concept_coverage
):

    # Understanding
    if similarity >= 0.8:
        understanding = 4
    elif similarity >= 0.6:
        understanding = 3
    elif similarity >= 0.4:
        understanding = 2
    else:
        understanding = 1

    # Accuracy
    if similarity >= 0.85:
        accuracy = 4
    elif similarity >= 0.65:
        accuracy = 3
    elif similarity >= 0.45:
        accuracy = 2
    else:
        accuracy = 1

    # Completeness
    if concept_coverage >= 80:
        completeness = 4
    elif concept_coverage >= 60:
        completeness = 3
    elif concept_coverage >= 40:
        completeness = 2
    else:
        completeness = 1

    return {
        "understanding": understanding,
        "accuracy": accuracy,
        "completeness": completeness
    }