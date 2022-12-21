from fastapi import FastAPI

from config.database import engine
from src.user import models as user_models
from src.units import models as units_models
from src.user.endpoints import router as users_endpoints

app = FastAPI()

user_models.Base.metadata.create_all(bind=engine)
units_models.Base.metadata.create_all(bind=engine)

app.include_router(users_endpoints)


@app.get("/")
async def root():
    return {"message": "Hello World"}