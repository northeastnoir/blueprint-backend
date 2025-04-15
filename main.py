from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Blueprint backend is LIVE 🚀"}from api.index import app
