from config.db import Base
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__="users"
    id: Mapped[int]= mapped_column(Integer, primary_key=True, autoincrement=True)
    email:Mapped[str]=mapped_column(String(200), unique=True, index=True, nullable=False)
    password:Mapped[str]=mapped_column(String(100), nullable=False)
    is_active:Mapped[bool]=mapped_column(Boolean, default=True, nullable=False)