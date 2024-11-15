# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

FAISS_FILE_PATH = "data/faiss_store_openai.pkl"
