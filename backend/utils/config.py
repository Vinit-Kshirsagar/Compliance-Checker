import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2")
BACKEND_PORT: int = int(os.getenv("BACKEND_PORT", "8000"))
SHARED_DATA_PATH: str = os.getenv("SHARED_DATA_PATH", "./shared_data")
