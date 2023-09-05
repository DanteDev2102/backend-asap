from db import session
from .model import Product

class ProductController:
    

    def create_product(self, product_data):
        product = Product(**product_data)
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    def read_product(self, product_id):
        return session.query(Product).filter(Product.id == product_id).first()

    def update_product(self, product_id, product_data):
        product = session.query(Product).filter(Product.id == product_id).first()
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            session.commit()
            session.refresh(product)
        return product

    def delete_product(self, product_id):
        product = session.query(Product).filter(Product.id == product_id).first()
        if product:
            session.delete(product)
            session.commit()
        return product