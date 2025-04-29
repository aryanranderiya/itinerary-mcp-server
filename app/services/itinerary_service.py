from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models.models import Activity, HotelStay, Itinerary, ItineraryDay
from app.schemas.schemas import ItineraryCreate


class ItineraryService:
    @staticmethod
    def get_itineraries(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        region: Optional[str] = None,
        min_nights: Optional[int] = None,
        max_nights: Optional[int] = None,
        recommended: Optional[bool] = None,
    ):
        """
        Retrieve a list of itineraries with optional filtering parameters.
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

    @staticmethod
    def get_itinerary_by_id(db: Session, itinerary_id: int):
        """
        Retrieve detailed information for a specific itinerary by its ID.
        """
        return db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()

    @staticmethod
    def create_itinerary(db: Session, itinerary: ItineraryCreate):
        """
        Create a new itinerary with associated days, hotel stays, and activities.
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
                hotel_stay = HotelStay(
                    itinerary_day_id=db_day.id, hotel_id=day.hotel_id
                )
                db.add(hotel_stay)
                db.commit()

                # Add activities
                if day.activity_ids:
                    for activity_id in day.activity_ids:
                        activity = db.query(Activity).get(activity_id)
                        if activity:
                            db_day.activities.append(activity)

                    db.commit()

            return db_itinerary

        except SQLAlchemyError as e:
            db.rollback()
            raise SQLAlchemyError(f"Database error: {str(e)}")
        except Exception as e:
            db.rollback()
            raise Exception(f"Error creating itinerary: {str(e)}")
