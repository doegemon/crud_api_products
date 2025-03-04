from models import ProductModel
from schema import ProductUpdate, ProductCreate
from sqlalchemy.orm import Session


def get_product(db: Session, product_id: int):
    """
    Function that returns the product data based on the id of the product.
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def get_products(db: Session):
    """
    Function that returns all products from the database.
    """
    return db.query(ProductModel).all()


def create_product(db: Session, product: ProductCreate):
    """
    Function that inserts a new product in the database.
    """
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    """
    Function that deletes an existent product in the database.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Function that updates the data from an existent product in the database.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.category is not None:
        db_product.category = product.category
    if product.vendor_email is not None:
        db_product.vendor_email = product.vendor_email

    db.commit()
    return db_product
