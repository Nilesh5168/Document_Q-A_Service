import asyncio
from APP.database import SessionLocal
from APP.models import Question, StatusEnum

async def simulate_llm_response(question_id: int):
    await asyncio.sleep(5)  # Simulate processing delay

    async with SessionLocal() as session:
        question = await session.get(Question, question_id)
        if question:
            question.answer = f"Simulated answer for: {question.question}"
            question.status = StatusEnum.answered
            await session.commit()
