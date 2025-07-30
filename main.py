from fastapi import FastAPI
from APP.routes import documents, questions, test_db  
app = FastAPI(title="Document Q&A Service")


app.include_router(documents.router, prefix="/documents", tags=["Documents"])
app.include_router(questions.router, prefix="/questions", tags=["Questions"])
app.include_router(test_db.router, tags=["Test"])


@app.get("/")
async def root():
    return {"message": "FastAPI Document Q&A Service is running"}
