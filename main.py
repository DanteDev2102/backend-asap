from fastapi import FastAPI
from db import BaseModel, db
from modules.routes import router
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/ok")
async def check_alive():
    return {"msg": "ok"}


@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")

app.include_router(router)

BaseModel.metadata.create_all(bind=db)
