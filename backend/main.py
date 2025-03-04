import models
from router import router
from fastapi import FastAPI
from database import engine

models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router)
