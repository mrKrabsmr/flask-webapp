from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from internal.app.database import Base
from internal.app.database.models.user import User


class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    title = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True))

    user = relationship(User, backref="surveys")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    survey_id = Column(Integer(), ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False)
    body = Column(String(1000), nullable=False)
    true_option = Column(String(), nullable=False)
    false_option_1 = Column(String(), nullable=False)
    false_option_2 = Column(String(), nullable=False)
    false_option_3 = Column(String(), nullable=False)

    survey = relationship(Survey, backref="questions")

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(String(5), nullable=False)
    survey_id = Column(Integer, ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=False)

    survey = relationship(Survey, backref="results")
    user = relationship(User, backref="results")
