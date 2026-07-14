from fastapi import FastAPI
from app.api.auth import router as auth_router
app = FastAPI(
    title="EstateGPT API"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to EstateGPT"
    }

app.include_router(auth_router)