from crud import (
    create_product,
    get_product,
    get_products,
    delete_product,
    update_product,
)
from typing import List
from schema import ProductResponse, ProductUpdate, ProductCreate
from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    """
    This function is used to estabilish the API route to insert a product in the database.
    """
    return create_product(db=db, product=product)


@router.get("/products/", response_model=List[ProductResponse])
def read_all_products_route(db: Session = Depends(get_db)):
    """
    This function is used to estabilish the API route to get all products data from the database.
    """
    products = get_products(db)
    return products


@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    This function is used to estabilish the API route to get data of a specific product.
    """
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    return db_product


@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    This function is used to estabilish the API route to delete product data from the database.
    """
    db_product = delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    return db_product


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    """
    This function is used to estabilish the API route to update the data of a specific product.
    """
    db_product = update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    return db_product
