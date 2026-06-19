from sentence_transformers import SentenceTransformer, util
from app.services.keyword_etractor import extract_keywords

model = SentenceTransformer("all-MiniLM-L6-v2")


def evaluate_answer(expected_answer, student_answer):

    emb1 = model.encode(expected_answer)
    emb2 = model.encode(student_answer)

    similarity = float(util.cos_sim(emb1, emb2)[0][0])

    score = round(similarity * 10, 2)

    expected_keywords = set(extract_keywords(expected_answer))

    student_text = student_answer.lower()

    missing_keywords = [
        keyword
        for keyword in expected_keywords
        if keyword.lower() not in student_text
    ]
    print("Expected Keywords:", expected_keywords)

    matched_keywords = len(expected_keywords) - len(missing_keywords)

    coverage = round(
        (matched_keywords / len(expected_keywords)) * 100,
        2
    ) if expected_keywords else 0

    return (
        score,
        similarity,
        missing_keywords,
        coverage
    )