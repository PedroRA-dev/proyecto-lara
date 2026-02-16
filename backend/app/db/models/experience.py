from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, DateTime, Integer, String, func, Float
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .booking import Booking

class Experience(Base):
    __tablename__ = "experience"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    main_image_url: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    disclaimer: Mapped[str] = mapped_column(String(100), nullable=True)
    bookings: Mapped[list["Booking"]] = relationship("Booking", back_populates="experience", cascade="all, delete-orphan", passive_deletes=True)
