from db import BaseModel
from pydantic import BaseModel as Base
from sqlalchemy import Column, Integer, String, Boolean, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date 

from db import session
from typing import ClassVar


import enum

# class EType(enum.Enum):
#     logistic = "L"
#     production_control = "PC"
#     seller = "V"
#     user = "U"



class ProductCreate(Base):
    name: str
    code: str
    unit_measurement_id: int
    cost: float
    price: float
    description: str
    categorie_id: int
    type: str
    suplier_id: int
    expiration_date: date
    state_product: str
    use_product: str


class ProductUpdate(Base):
    name: str
    price: float
    description: str

class Product(BaseModel):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60))
    code = Column(String(10))
    unit_measurement_id = Column(Integer, ForeignKey("Unit_Measurement.id"))  # Relación con Unit_Measurement
    cost = Column(Float)
    last_cost = Column(Float)
    active = Column(Boolean, default=True)
    price = Column(Float)
    description = Column(String(20))
    categorie_id = Column(Integer, ForeignKey("Categorie.id"))  # Relación con Categorie
    type = Column(String(20))
    suplier_id = Column(Integer, ForeignKey("Suplier.id"))  # Relación con Suplier
    expiration_date = Column(Date)
    state_product = Column(String(20))
    use_product = Column(String(20))

    # Definir las relaciones inversas
    unit_measurement = relationship("Unit_Measurement", back_populates="products")
    categorie = relationship("Categorie", back_populates="products")
    suplier = relationship("Suplier", back_populates="products")

class Suplier(BaseModel):
    __tablename__ = "Suplier"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60))
    rif = Column(String(10))
    phone = Column(String(20))
    code = Column(String(10))
    active = Column(Boolean, default=True)

    # Definir la relación inversa
    products = relationship("Product", back_populates="suplier")

class Categorie(BaseModel):
    __tablename__ = "Categorie"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60))
    active = Column(Boolean, default=True)
    code = Column(String(10))

    # Definir la relación inversa
    products = relationship("Product", back_populates="categorie")

class Unit_Measurement(BaseModel):
    __tablename__ = "Unit_Measurement"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60))
    symbol = Column(String(1))
    active = Column(Boolean, default=True)

    # Definir la relación inversa
    products = relationship("Product", back_populates="unit_measurement")

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()