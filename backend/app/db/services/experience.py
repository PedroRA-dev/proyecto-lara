from app.db.models import Experience
from sqlalchemy import select
from sqlalchemy.orm import Session



def upsert_experience(
        session: Session, 
        name: str,                       
        description: str, 
        main_image_url: str, 
        price: float, 
        disclaimer: str
) -> Experience:
    existing_experience = session.execute(
        select(Experience).where(Experience.name == name)
    ).scalar_one_or_none()

    if existing_experience:
        existing_experience.description = description
        existing_experience.main_image_url = main_image_url
        existing_experience.price = price
        existing_experience.disclaimer = disclaimer     
        session.commit()
        return existing_experience

    new_experience = Experience(
        name=name,
        description=description,
        main_image_url=main_image_url,
        price=price,
        disclaimer=disclaimer
    )
    session.add(new_experience)
    session.commit()
    return new_experience