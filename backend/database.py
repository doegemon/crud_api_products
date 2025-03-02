from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Creating the database engine, that connects with the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Database session, that allow the execution of the queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Function that creates a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
