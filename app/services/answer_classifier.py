def classify_answer(
    similarity,
    concept_coverage
):

    if similarity < 0.30:
        return "Irrelevant"

    if similarity < 0.60:
        return "Incorrect"

    if concept_coverage < 50:
        return "Incomplete"

    return "Relevant"