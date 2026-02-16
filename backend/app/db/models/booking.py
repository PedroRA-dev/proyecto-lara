from __future__ import annotations

from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, DateTime, Integer, String, func, Enum, ForeignKey
from datetime import datetime
import enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .experience import Experience

class BookingStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"

class Booking(Base):
    __tablename__ = "booking"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(80), nullable=False)
    surname: Mapped[str] = mapped_column(String(130), nullable=False)

    dni: Mapped[str] = mapped_column(String(9), nullable=False)
    email: Mapped[str] = mapped_column(String(130), nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False)

    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    
    experience_id: Mapped[int] = mapped_column(ForeignKey("experience.id", ondelete="CASCADE"), nullable=False, index=True)
    experience: Mapped["Experience"] = relationship("Experience", back_populates="bookings")
    status: Mapped[BookingStatus] = mapped_column(Enum(BookingStatus), nullable=False, server_default=BookingStatus.pending.value)


    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )




