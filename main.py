from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import BaseModel, db
from modules.routes import router
from starlette.responses import RedirectResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins="*",
    allow_headers=["*"],
    allow_methods=["*"],
    expose_headers=["*"],
    max_age=3600
)


@app.get("/ok")
async def check_alive():
    return {"msg": "ok"}


@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")

app.include_router(router)

BaseModel.metadata.create_all(bind=db)
