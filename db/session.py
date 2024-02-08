from sqlalchemy import create_engine
import settings
from sqlalchemy.orm import sessionmaker


engine = create_engine(settings.POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

