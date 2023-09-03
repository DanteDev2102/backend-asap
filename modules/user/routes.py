from fastapi import APIRouter
from modules.user.model import UserModel, LoginModel
from modules.user.controller import UserController

router = APIRouter()
controller = UserController()


@router.get("/")
async def get_users():
    return {
        "msg": "success",
        "code": 200,
        "data": controller.search(),
        "errors": []
    }


@router.post("/", status_code=201)
async def create_user(user: UserModel):
    return {
        "msg": "user created",
        "code": 201,
        "data": {
            "user": controller.create(user)
        },
        "errors": []
    }


@router.get("/{code}")
async def get_user(code:str):
    return {
        "msg": "sucess",
        "code": 200,
        "data": {
            "user": controller.search_one(code=code)
        },
        "errors": []
    }


@router.patch("/{code}")
async def unlink_user(code:str):
    return {
        "msg": "sucess",
        "code": 200,
        "data": {
            "user": controller.unlink(code)
        },
        "errors": []
    }


@router.post("/auth")
async def login(login:LoginModel):
    user = controller.login(login)

    if isinstance(user, str):
        return {
            "msg": user,
            "code": 403,
            "data": [],
            "errors": []
        }
    
    return {
        "msg": "sucess",
        "code": 200,
        "data": {
            "user": user
        },
        "errors": []
    }