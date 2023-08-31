from fastapi import FastAPI
from db import BaseModel, db
from modules.routes import router

app = FastAPI()


@app.get("/")
async def check_alive():
    return {"msg": "ok"}

app.include_router(router)

BaseModel.metadata.create_all(bind=db)
