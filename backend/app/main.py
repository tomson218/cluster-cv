from fastapi import FastAPI
from .database import Base, engine
from .routers import items

Base.metadata.create_all(bind=engine)  # fine for learning; use Alembic later

app = FastAPI(title="My API")
app.include_router(items.router)

@app.get("/health")
def health():
    return {"status": "ok"}