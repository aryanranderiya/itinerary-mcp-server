from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.schemas import Itinerary as ItinerarySchema
from app.schemas.schemas import ItineraryCreate, ItineraryDetailed
from app.services.itinerary_service import ItineraryService

router = APIRouter(
    prefix="/itineraries",
    tags=["itineraries"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/", response_model=List[ItinerarySchema], operation_id="Get_All_Itineraries"
)
async def get_itineraries(
    skip: int = 0,
    limit: int = 100,
    region: Optional[str] = None,
    min_nights: Optional[int] = None,
    max_nights: Optional[int] = None,
    recommended: Optional[bool] = None,
    db: Session = Depends(get_db),
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
        db (Session): Database session dependency

    Returns:
        List[ItinerarySchema]: List of matching itineraries
    """
    return ItineraryService.get_itineraries(
        db=db,
        skip=skip,
        limit=limit,
        region=region,
        min_nights=min_nights,
        max_nights=max_nights,
        recommended=recommended,
    )


@router.get(
    "/{itinerary_id}",
    response_model=ItineraryDetailed,
    operation_id="Get_Itinerary_by_ID",
)
async def get_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    """
    Retrieve detailed information for a specific itinerary by its ID.

    Parameters:
        itinerary_id (int): The ID of the itinerary to retrieve
        db (Session): Database session dependency

    Returns:
        ItineraryDetailed: Detailed representation of the itinerary including related data

    Raises:
        HTTPException: 404 if itinerary with specified ID does not exist
    """
    itinerary = ItineraryService.get_itinerary_by_id(db, itinerary_id)
    if itinerary is None:
        raise HTTPException(status_code=404, detail="Itinerary not found")

    return itinerary


@router.post(
    "/",
    response_model=ItineraryDetailed,
    status_code=201,
    operation_id=("Create_Itinerary"),
)
async def create_itinerary(itinerary: ItineraryCreate, db: Session = Depends(get_db)):
    """
    Create a new itinerary with associated days, hotel stays, and activities.

    Parameters:
        itinerary (ItineraryCreate): The itinerary data to create
        db (Session): Database session dependency

    Returns:
        ItineraryDetailed: Created itinerary with all related entities

    Raises:
        HTTPException:
            - 400 for validation or input errors
            - 500 for database errors during creation
    """
    try:
        return ItineraryService.create_itinerary(db, itinerary)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error creating itinerary: {str(e)}"
        )
