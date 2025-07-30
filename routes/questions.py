from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from APP.database import get_db
from APP.models import Question, Document
from APP.schemas import QuestionCreate, QuestionResponse
from APP.services.llm_simulator import simulate_llm_response
import asyncio

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post("/{document_id}", response_model=QuestionResponse)
async def ask_question(document_id: int, q: QuestionCreate, db: AsyncSession = Depends(get_db)):
    # Check if document exists
    doc = await db.get(Document, document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    # Create new question
    new_q = Question(document_id=document_id, question=q.question)
    db.add(new_q)
    await db.commit()
    await db.refresh(new_q)

    # Start background task (simulate LLM response)
    asyncio.create_task(simulate_llm_response(new_q.id))  # Will update DB later

    return new_q  # ORM model works with `orm_mode=True`


@router.get("/{id}", response_model=QuestionResponse)
async def get_answer(id: int, db: AsyncSession = Depends(get_db)):
    question = await db.get(Question, id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question
