from fastapi import APIRouter
from modules.user.model import UserModel
from modules.user.controller import UserController

router = APIRouter()
controller = UserController()


@router.get("/")
async def get_paginate_users():
    pass


@router.post("/")
async def create_user(user: UserModel):
    alo = controller.create(user)
    print(alo)
    return "si"
