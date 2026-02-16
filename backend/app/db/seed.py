from app.db import session
from app.db.services.experience import upsert_experience
from app.db.models import Experience
from typing import List
from app.db.session import SessionLocal



SEEDED_EXPERIENCES: List[Experience] = [
    {
        "name": "Experience 1",
        "description": "Description 1",
        "main_image_url": "https://example.com/image1.jpg",
        "price": 100.0,
        "disclaimer": "Disclaimer 1"
    }
]

def run_seed():
    with SessionLocal() as db:
        with db.begin():
            for experience_data in SEEDED_EXPERIENCES:
                upsert_experience(db, **experience_data)


if __name__ == "__main__":
    run_seed()