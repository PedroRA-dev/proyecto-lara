from __future__ import annotations

from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, func, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .user import User


class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Identificador único del token (metes este value como jti en el JWT refresh)
    jti: Mapped[str] = mapped_column(String(64), nullable=False, unique=True, index=True)

    # Guarda HASH del refresh token (ej: sha256 o mejor, HMAC/argon2/bcrypt)
    token_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Rotación: este refresh fue reemplazado por otro (nuevo) refresh
    replaced_by_id: Mapped[int | None] = mapped_column(
        ForeignKey("refresh_token.id", ondelete="SET NULL"),
        nullable=True,
    )

    # Telemetría opcional (útil para seguridad)
    created_by_ip: Mapped[str | None] = mapped_column(String(45), nullable=True)      # IPv4/IPv6
    created_by_ua: Mapped[str | None] = mapped_column(String(255), nullable=True)

    user: Mapped["User"] = relationship(back_populates="refresh_tokens")

    replaced_by: Mapped[Optional["RefreshToken"]] = relationship(
        remote_side="RefreshToken.id",
        uselist=False,
    )

    table_args = (
        Index("ix_refresh_token_user_id_revoked_at", "user_id", "revoked_at"),
    )