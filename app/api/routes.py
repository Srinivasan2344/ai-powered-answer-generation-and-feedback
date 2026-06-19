from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.schemas import (
    EvaluationRequest,
    CodeEvaluationRequest
)

from app.services.evaluator import evaluate_answer
from app.services.feedback import generate_feedback
from app.services.code_evaluator import evaluate_code
from app.services.rubric import calculate_rubric
from app.services.answer_classifier import classify_answer

from app.database.db import get_db
from app.database.crud import (
    save_evaluation,
    get_all_evaluations,
    get_analytics,
    get_report,
    get_all_evaluations_for_export
)
import csv
from fastapi.responses import FileResponse

router = APIRouter()


@router.post("/evaluate")
def evaluate(
    data: EvaluationRequest,
    db: Session = Depends(get_db)
):

    score, similarity, missing_keywords, coverage = evaluate_answer(
        data.expected_answer,
        data.student_answer
    )

    confidence = round(similarity * 100, 2)

    answer_status = classify_answer(
        similarity,
        coverage
    )

    rubric = calculate_rubric(
        similarity,
        coverage
    )

    feedback = generate_feedback(
        score,
        missing_keywords
    )

    save_evaluation(
        db=db,
        expected_answer=data.expected_answer,
        student_answer=data.student_answer,
        score=score,
        similarity=similarity,
        confidence=confidence,
        concept_coverage=coverage,
        answer_status=answer_status,
        strengths=feedback["strengths"],
        improvements=feedback["improvements"]
    )

    return {
        "score": score,
        "similarity": round(similarity, 2),
        "confidence": confidence,
        "answer_status": answer_status,
        "concept_coverage": coverage,
        "missing_keywords": missing_keywords,
        "rubric": rubric,
        "feedback": feedback
    }


@router.post("/evaluate-code")
def evaluate_code_answer(
    data: CodeEvaluationRequest
):

    return evaluate_code(
        data.expected_code,
        data.student_code
    )


@router.get("/history")
def history(
    db: Session = Depends(get_db)
):

    return get_all_evaluations(db)


@router.get("/analytics")
def analytics(
    db: Session = Depends(get_db)
):

    return get_analytics(db)


@router.get("/report")
def report(
    db: Session = Depends(get_db)
):

    return get_report(db)

@router.get("/export-csv")
def export_csv(
    db: Session = Depends(get_db)
):

    evaluations = get_all_evaluations_for_export(db)

    filename = "evaluation_report.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Score",
            "Similarity",
            "Confidence",
            "Status",
            "Concept Coverage"
        ])

        for e in evaluations:

            writer.writerow([
                e.id,
                e.score,
                e.similarity,
                e.confidence,
                e.answer_status,
                e.concept_coverage
            ])

    return FileResponse(
        filename,
        media_type="text/csv",
        filename=filename
    )