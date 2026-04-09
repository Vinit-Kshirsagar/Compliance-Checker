# Compliance Checker

Automated regulatory compliance tool for RBI/SEBI/MCA circulars.
Detects changes, maps them to internal company documents, drafts amendments,
and tracks compliance evolution across runs.

## Stack
- **Backend**: Python 3.11, FastAPI, CrewAI (single agent), ChromaDB, Ollama llama3.2
- **Frontend**: Next.js 15, React 19, TypeScript, Tailwind CSS

## Quick Start

### Prerequisites
- Python 3.11
- Node.js 20
- Ollama with llama3.2 pulled (`ollama pull llama3.2`)

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..
ollama serve   # in a separate terminal
uvicorn backend.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

- Backend: http://localhost:8000/docs
- Frontend: http://localhost:3000

## Team
- Backend Dev: main.py, FastAPI endpoints, shared_data/ schema
- AI Dev: crew.py, LLM pipeline, ChromaDB
- Frontend Dev: everything in frontend/
