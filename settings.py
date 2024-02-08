import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "local")
POSTGRES_URL = os.getenv("DATABASE_URL", os.getenv("POSTGRES_URL", ""))
