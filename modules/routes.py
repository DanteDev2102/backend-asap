from fastapi import APIRouter
import modules.user.routes as userRoutes

router = APIRouter()

router.include_router(userRoutes.router, prefix="/user")