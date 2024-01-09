from fastapi import FastAPI
from routes.pais import pais

app = FastAPI()
app.include_router(pais)