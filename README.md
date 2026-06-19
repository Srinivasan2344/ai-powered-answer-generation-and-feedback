# AI-Powered Answer Evaluation & Feedback System

## Overview

The AI-Powered Answer Evaluation & Feedback System is an intelligent application that automatically evaluates student answers using Natural Language Processing (NLP) and Machine Learning techniques. The system compares student responses with expected answers, calculates semantic similarity, analyzes concept coverage, and generates constructive feedback.

## Features

* Automated Answer Evaluation
* Semantic Similarity Scoring
* Confidence Score Generation
* Keyword Extraction using KeyBERT
* Concept Coverage Analysis
* Missing Keyword Detection
* Personalized Feedback Generation
* Answer Classification

  * Relevant
  * Incomplete
  * Incorrect
  * Irrelevant
* Evaluation History Tracking
* Performance Analytics
* CSV Report Export
* PostgreSQL Database Integration
* REST API using FastAPI

## Technology Stack

### Backend

* FastAPI
* Python

### AI & NLP

* Sentence Transformers
* KeyBERT
* Scikit-Learn

### Database

* PostgreSQL
* SQLAlchemy

### Tools

* Uvicorn
* Swagger UI

## Project Structure

app/
├── api/
├── services/
├── models/
├── database/
│ ├── db.py
│ ├── models.py
│ └── crud.py

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd AI-Answer-Evaluation-System
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

```bash
.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Configure PostgreSQL database

Update the DATABASE_URL in db.py:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/answer_evaluation_db"
```

6. Run the application

```bash
python -m uvicorn app.main:app --reload
```

## API Endpoints

### Evaluate Answer

POST /evaluate

### Evaluation History

GET /history

### Analytics Report

GET /analytics

### Summary Report

GET /report

### Export CSV

GET /export-csv

## Sample Request

```json
{
  "expected_answer": "Machine Learning is a branch of Artificial Intelligence that enables systems to learn from data.",
  "student_answer": "Machine learning allows systems to learn from data and improve automatically."
}
```

## Sample Response

```json
{
  "score": 8.39,
  "similarity": 0.84,
  "confidence": 83.95,
  "answer_status": "Relevant",
  "concept_coverage": 100
}
```
