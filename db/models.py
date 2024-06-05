from uuid import UUID, uuid4
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .engins import Base


class User(Base):
    __tablename__ = "users"

    password: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column(
        unique=True)
    id: Mapped[UUID] = mapped_column(
        primary_key=True, index=True, default_factory=uuid4)
