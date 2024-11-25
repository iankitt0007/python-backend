from fastapi import FastAPI
from app.routes import auth, dashboard
from app.database import create_db_and_tables

app = FastAPI(title="Admin Panel", version="1.0.0", description="Admin Panel Backend with FastAPI")

# Include API routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])

@app.on_event("startup")
async def startup():
    create_db_and_tables()  # Automatically create database tables on startup
