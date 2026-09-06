from config.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


class Message(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(255), nullable=False)
    author_email: Mapped[str | None] = mapped_column(String(255), nullable=True) #opcional
    priority: Mapped[int] = mapped_column(Integer, nullable=False, default=1)