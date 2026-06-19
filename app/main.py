from fastapi import FastAPI
from app.api.routes import router

from app.database.db import engine, Base
from app.database.models import Evaluation

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Answer Evaluation System"
)

app.include_router(router)