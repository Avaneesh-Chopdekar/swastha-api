import os
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("DB_URI") or "mongodb://localhost:27017"
