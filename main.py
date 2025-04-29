from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.itineraries import router as itinerary_router
from app.database.seed import init_db
from contextlib import asynccontextmanager
from fastapi_mcp import FastApiMCP

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

# Mount the MCP server directly to the FastAPI app
# Doing this over here to ensure mcp server is created after including routes
mcp = FastApiMCP(
    app,
    name="Travel Itinerary API MCP Server",
    description="MCP server for managing travel itineraries",
    describe_full_response_schema=True,  # Describe the full response JSON-schema
    describe_all_responses=True,  # All possible responses instead of just success (2XX) response
)
mcp.mount()


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
