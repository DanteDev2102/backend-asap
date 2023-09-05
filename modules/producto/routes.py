from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .controller import ProductController
from .model import Product,get_db


router = APIRouter()
product_controller = ProductController()

@router.post("/products/")
def create_product(product_data: dict):
    try:
        product = product_controller.create_product(product_data)
        return {"message": "Producto creado exitosamente", "product": product}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/products/{product_id}")
def read_product(product_id: int):
    product = product_controller.read_product(product_id)
    if product:
        return {"product": product}
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@router.put("/products/{product_id}")
def update_product(product_id: int, product_data: dict):
    product = product_controller.update_product(product_id, product_data)
    if product:
        return {"message": "Producto actualizado exitosamente", "product": product}
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    product = product_controller.delete_product(product_id)
    if product:
        return {"message": "Producto eliminado exitosamente", "product": product}
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
