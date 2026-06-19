from pydantic import BaseModel

class EvaluationRequest(BaseModel):
    expected_answer: str
    student_answer: str

class EvaluationResponse(BaseModel):
    score: float
    similarity: float
    feedback: str

class CodeEvaluationRequest(BaseModel):
    expected_code: str
    student_code: str