from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.itineraries import router as itinerary_router
from app.database.seed import init_db
from contextlib import asynccontextmanager

# Initialize application
app = FastAPI(
    title="Travel Itinerary API",
    description="API for managing travel itineraries",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(itinerary_router)


# Lifespan manager of FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    # Initialize db tables and seed data
    init_db()
    yield
    print("Shutting Down...")


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Travel Itinerary API",
        "docs": "/docs",
        "endpoints": {"itineraries": "/itineraries"},
    }
