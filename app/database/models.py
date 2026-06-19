from sqlalchemy import Column, Integer, Float, String
from app.database.db import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)

    expected_answer = Column(String)
    student_answer = Column(String)

    score = Column(Float)
    similarity = Column(Float)
    confidence = Column(Float)

    concept_coverage = Column(Float)

    answer_status = Column(String)

    strengths = Column(String)
    improvements = Column(String)