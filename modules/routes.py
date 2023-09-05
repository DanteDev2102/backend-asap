from fastapi import APIRouter
import modules.user.routes as userRoutes
import modules.producto.routes as productRoutes

router = APIRouter()

router.include_router(userRoutes.router, prefix="/user")
router.include_router(productRoutes.router, prefix="/product")