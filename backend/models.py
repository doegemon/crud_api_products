from database import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Float, DateTime


class ProductModel(Base):
    """
    Class that represents a Table in our database.
    """

    # Table name
    __tablename__ = "products"

    # Columns names and data types
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    vendor_email = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
