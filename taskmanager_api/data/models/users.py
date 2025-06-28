from ..postgre_connect import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    points: Mapped[int] = mapped_column(default=0)
    completed_tasks: Mapped[int] = mapped_column(default=0)
    all_tasks: Mapped[int] = mapped_column(default=0)
    referal_link: Mapped[str] = mapped_column()
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")