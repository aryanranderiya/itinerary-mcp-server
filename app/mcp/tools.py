from typing import Optional, cast

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.mcp import mcp
from app.schemas.schemas import ItineraryCreate
from app.services.itinerary_service import ItineraryService


@mcp.tool()
def get_itineraries(
    skip: int = 0,
    limit: int = 100,
    region: Optional[str] = None,
    min_nights: Optional[int] = None,
    max_nights: Optional[int] = None,
    recommended: Optional[bool] = None,
):
    """
    Retrieve a list of itineraries with optional filtering parameters.

    Parameters:
        skip (int): Number of records to skip for pagination (default: 0)
        limit (int): Maximum number of records to return (default: 100)
        region (str, optional): Filter itineraries by region
        min_nights (int, optional): Filter itineraries with duration >= min_nights
        max_nights (int, optional): Filter itineraries with duration <= max_nights
        recommended (bool, optional): Filter by recommended status

    Returns:
        List of matching itineraries
    """
    db = cast(Session, get_db(mcp=True))  # Prevent type issues
    try:
        return ItineraryService.get_itineraries(
            db=db,
            skip=skip,
            limit=limit,
            region=region,
            min_nights=min_nights,
            max_nights=max_nights,
            recommended=recommended,
        )
    finally:
        db.close()


@mcp.tool()
def get_itinerary_by_id(itinerary_id: int):
    """
    Retrieve detailed information for a specific itinerary by its ID.

    Parameters:
        itinerary_id (int): The ID of the itinerary to retrieve

    Returns:
        Detailed representation of the itinerary including related data or None if not found
    """
    db = cast(Session, get_db(mcp=True))
    try:
        return ItineraryService.get_itinerary_by_id(db, itinerary_id)
    finally:
        db.close()


@mcp.tool()
def create_itinerary(itinerary: ItineraryCreate):
    """
    Create a new itinerary with associated days, hotel stays, and activities.

    Parameters:
        itinerary (ItineraryCreate): The itinerary data to create

    Returns:
        Created itinerary with all related entities

    Raises:
        Exception: For validation, input, or database errors during creation
    """
    db = cast(Session, get_db(mcp=True))
    try:
        return ItineraryService.create_itinerary(db, itinerary)
    finally:
        db.close()
