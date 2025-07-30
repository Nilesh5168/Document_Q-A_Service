# Document_Q-A_Service

This project is an async FastAPI backend for a Document Q&A system. Users can upload documents, ask questions about them, and get simulated LLM-based answers. It showcases modern backend design, modular structure, async database operations, and background task simulation.

🚀 Features
✅ Upload documents (title + content)

💬 Ask questions about uploaded documents

🤖 Simulated LLM answers generated asynchronously

🔁 PostgreSQL + Async SQLAlchemy integration

🧪 Modular routing and clean architecture

🛠️ Tech Stack
FastAPI

PostgreSQL

Async SQLAlchemy (2.0)

Pydantic

Uvicorn

Python 3.10+


🧰 Setup Instructions
1. Clone the Repository

git clone https://github.com/Nilesh5168/Document_Q-A_Service.git
cd Document_Q-A_Service

2. Install Dependencies

pip install fastapi uvicorn psycopg2-binary sqlalchemy asyncpg

3. Set Up PostgreSQL Database
Ensure PostgreSQL is running and accessible. Create a database:

CREATE DATABASE documentqa;

Update your APP/database.py with your PostgreSQL connection URL:

DATABASE_URL = "postgresql+asyncpg://username:password@localhost/documentqa"

4. Initialize the Database
Run the table creation script:

python -m APP.init_db

▶️ Running the App

uvicorn APP.main:app --reload

Your API will be live at: http://127.0.0.1:8000

📬 API Endpoints

📁 1. Post a Document
URL: POST http://127.0.0.1:8000/documents/documents/


{
  "title": "AI in Healthcare",
  "content": "This document covers AI use cases in healthcare..."
}


❓2. Ask a Question About a Document
URL: POST http://127.0.0.1:8000/questions/questions/{document_id}

Example: /questions/questions/2

{
  "question": "What are the applications of AI in diagnosis?"
}


✅ 3. Get the Answer for a Question
URL: GET http://127.0.0.1:8000/questions/questions/{question_id}

Example: /questions/questions/2


🧪 Testing
You can test the endpoints using Postman or curl.
