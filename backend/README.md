# Wayne BI Backend (FastAPI)

Run locally:
```bash
python -m venv .venv && source .venv/bin/activate # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
The API docs will be at http://localhost:8000/docs
