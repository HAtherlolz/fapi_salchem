from fastapi import FastAPI

from config.database import metadata, engine, database
from src.user.endpoints import router as users_endpoints


# metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(users_endpoints)


@app.get("/")
async def root():
    return {"message": "Hello World"}