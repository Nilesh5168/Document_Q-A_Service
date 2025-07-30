from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import relationship
from APP.database import Base
import enum

class StatusEnum(str, enum.Enum):
    pending = "pending"
    answered = "answered"

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)

    questions = relationship("Question", back_populates="document")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.pending)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    document = relationship("Document", back_populates="questions")
