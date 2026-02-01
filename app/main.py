from fastapi import FastAPI
from app.routes import risk


app = FastAPI(title="Deslaves MVP")

app.include_router(risk.router)

@app.get("/")
def root():
    return {"status": "Backend funcionando"}