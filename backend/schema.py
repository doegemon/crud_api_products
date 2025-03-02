from typing import Optional
from datetime import datetime
from pydantic import BaseModel, PositiveFloat, EmailStr


class ProductBase(BaseModel):
    """
    Class that validates the data types of the table columns.
    """

    name: str
    description: Optional[str] = None
    price: PositiveFloat
    category: str
    vendor_email: EmailStr


class ProductCreate(ProductBase):
    """
    Class that validates the data types of the table columns when creating/adding a new product.
    """

    pass


class ProductResponse(ProductBase):
    """
    Class that validates the data types of the table columns when searching for a product.
    """

    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    """
    Class that validates the data types of the table columns when updating a product.
    """

    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    vendor_email: Optional[EmailStr] = None
