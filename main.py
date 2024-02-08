from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def check_root():
    return {"New": "Stuff"}
