from fastapi import FastAPI
import os
from .db import DatabaseFactory


app = FastAPI()

db_url = os.getenv("DATABASE_URL")
df = DatabaseFactory(db_url)
db_engine = df.create_engine()


@app.get("/")
async def root():
    return {"message": "holi"}
