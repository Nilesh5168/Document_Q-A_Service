from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from APP.database import get_db
from APP.models import Document
from APP.schemas import DocumentCreate, DocumentResponse

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/", response_model=DocumentResponse)
async def upload_document(doc: DocumentCreate, db: AsyncSession = Depends(get_db)):
    new_doc = Document(title=doc.title, content=doc.content)
    db.add(new_doc)
    await db.commit()
    await db.refresh(new_doc)
    return new_doc

@router.get("/{id}", response_model=DocumentResponse)
async def get_document(id: int, db: AsyncSession = Depends(get_db)):
    doc = await db.get(Document, id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc
