from fastapi import FastAPI
from app.configs.db import Base, engine
from app.routers.CharacterRouter import CharacterRouter

app = FastAPI(title="API - Character")

app.include_router(CharacterRouter)

Base.metadata.create_all(bind=engine)