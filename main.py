from fastapi import FastAPI, Depends

from db.session import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def check_root(db: Session = Depends(get_db)):
    return {"New": "Stuff"}
