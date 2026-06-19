from app.database.models import Evaluation
from sqlalchemy import func


def save_evaluation(
    db,
    expected_answer,
    student_answer,
    score,
    similarity,
    confidence,
    concept_coverage,
    answer_status,
    strengths,
    improvements
):

    evaluation = Evaluation(
        expected_answer=expected_answer,
        student_answer=student_answer,
        score=score,
        similarity=similarity,
        confidence=confidence,
        concept_coverage=concept_coverage,
        answer_status=answer_status,
        strengths=", ".join(strengths),
        improvements=", ".join(improvements)
    )

    db.add(evaluation)
    db.commit()
    db.refresh(evaluation)

    return evaluation


def get_all_evaluations(db):

    return db.query(Evaluation).all()

def get_all_evaluations_for_export(db):

    return db.query(Evaluation).all()


def get_analytics(db):

    total = db.query(Evaluation).count()

    avg_score = db.query(
        func.avg(Evaluation.score)
    ).scalar()

    avg_confidence = db.query(
        func.avg(Evaluation.confidence)
    ).scalar()

    max_score = db.query(
        func.max(Evaluation.score)
    ).scalar()

    min_score = db.query(
        func.min(Evaluation.score)
    ).scalar()

    return {
        "total_evaluations": total,
        "average_score": round(avg_score or 0, 2),
        "average_confidence": round(avg_confidence or 0, 2),
        "highest_score": round(max_score or 0, 2),
        "lowest_score": round(min_score or 0, 2)
    }


def get_report(db):

    evaluations = db.query(Evaluation).all()

    return {
        "total_evaluations": len(evaluations),

        "relevant_answers": len(
            [e for e in evaluations if e.answer_status == "Relevant"]
        ),

        "incomplete_answers": len(
            [e for e in evaluations if e.answer_status == "Incomplete"]
        ),

        "incorrect_answers": len(
            [e for e in evaluations if e.answer_status == "Incorrect"]
        ),

        "irrelevant_answers": len(
            [e for e in evaluations if e.answer_status == "Irrelevant"]
        )
    }