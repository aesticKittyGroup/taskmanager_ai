from ..postgre_connect import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from datetime import datetime



class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    description: Mapped[str] = mapped_column(String(200))
    date_create: Mapped[datetime] = mapped_column()
    expire_time: Mapped[datetime] = mapped_column()
    points: Mapped[int] = mapped_column()
    
    user = relationship("User", back_populates="tasks")