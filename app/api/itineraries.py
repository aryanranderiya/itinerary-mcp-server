from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.database.connection import get_db
from app.models.models import Itinerary, ItineraryDay, HotelStay, Activity
from app.schemas.schemas import Itinerary as ItinerarySchema
from app.schemas.schemas import ItineraryCreate, ItineraryDetailed

router = APIRouter(
    prefix="/itineraries",
    tags=["itineraries"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ItinerarySchema])
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
    Get all itineraries with optional filtering
    """
    query = db.query(Itinerary)

    # Apply filters if provided
    if region:
        query = query.filter(Itinerary.region == region)
    if min_nights:
        query = query.filter(Itinerary.duration_nights >= min_nights)
    if max_nights:
        query = query.filter(Itinerary.duration_nights <= max_nights)
    if recommended is not None:
        query = query.filter(Itinerary.is_recommended == (1 if recommended else 0))

    itineraries = query.offset(skip).limit(limit).all()

    return itineraries


@router.get("/{itinerary_id}", response_model=ItineraryDetailed)
async def get_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    """
    Get a specific itinerary by ID with detailed information
    """
    itinerary = db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()
    if itinerary is None:
        raise HTTPException(status_code=404, detail="Itinerary not found")

    return itinerary


@router.post("/", response_model=ItineraryDetailed, status_code=201)
async def create_itinerary(itinerary: ItineraryCreate, db: Session = Depends(get_db)):
    """
    Create a new itinerary with days, hotel stays, and activities
    """
    try:
        # Create the itinerary
        db_itinerary = Itinerary(
            name=itinerary.name,
            description=itinerary.description,
            region=itinerary.region,
            duration_nights=itinerary.duration_nights,
            is_recommended=itinerary.is_recommended,
        )
        db.add(db_itinerary)
        db.commit()
        db.refresh(db_itinerary)

        # Add itinerary days
        for day in itinerary.days:
            db_day = ItineraryDay(
                itinerary_id=db_itinerary.id,
                day_number=day.day_number,
                transfer_id=day.transfer_id,
            )
            db.add(db_day)
            db.commit()
            db.refresh(db_day)

            # Add hotel stay
            hotel_stay = HotelStay(itinerary_day_id=db_day.id, hotel_id=day.hotel_id)
            db.add(hotel_stay)
            db.commit()

            # Add activities
            if day.activity_ids:
                for activity_id in day.activity_ids:
                    activity = db.query(Activity).get(activity_id)
                    if activity:
                        db_day.activities.append(activity)

                db.commit()

        # Return the created itinerary with its relationships
        return db_itinerary

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400, detail=f"Error creating itinerary: {str(e)}"
        )
