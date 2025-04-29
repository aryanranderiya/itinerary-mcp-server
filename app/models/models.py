from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    Text,
    Enum,
    Table,
)
from sqlalchemy.orm import relationship
import enum

from app.database.connection import Base

# Association table for many-to-many relationships
itinerary_activity = Table(
    "itinerary_activity",
    Base.metadata,
    Column("itinerary_day_id", Integer, ForeignKey("itinerary_days.id")),
    Column("activity_id", Integer, ForeignKey("activities.id")),
)


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)  # e.g., Phuket, Krabi
    description = Column(Text)

    # Relationships
    hotels = relationship("Hotel", back_populates="location")
    activities = relationship("Activity", back_populates="location")

    def __repr__(self):
        return f"<Location {self.name} ({self.region})>"


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    description = Column(Text)
    rating = Column(Float)  # e.g., 4.5 stars
    price_per_night = Column(Float)  # Average price per night

    # Relationships
    location = relationship("Location", back_populates="hotels")
    stays = relationship("HotelStay", back_populates="hotel")

    def __repr__(self):
        return f"<Hotel {self.name}>"


class TransferType(str, enum.Enum):
    TAXI = "taxi"
    BUS = "bus"
    FERRY = "ferry"
    PRIVATE_CAR = "private_car"
    AIRPLANE = "airplane"


class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    origin_location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    destination_location_id = Column(
        Integer, ForeignKey("locations.id"), nullable=False
    )
    transfer_type = Column(Enum(TransferType), nullable=False)
    duration_minutes = Column(Integer)  # Duration in minutes
    price = Column(Float)

    # Relationships
    origin = relationship("Location", foreign_keys=[origin_location_id])
    destination = relationship("Location", foreign_keys=[destination_location_id])
    itinerary_days = relationship("ItineraryDay", back_populates="transfer")

    def __repr__(self):
        return f"<Transfer {self.transfer_type.value} from {self.origin_location_id} to {self.destination_location_id}>"


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    description = Column(Text)
    duration_minutes = Column(Integer)  # Duration in minutes
    price = Column(Float)

    # Relationships
    location = relationship("Location", back_populates="activities")
    itinerary_days = relationship(
        "ItineraryDay", secondary=itinerary_activity, back_populates="activities"
    )

    def __repr__(self):
        return f"<Activity {self.name}>"


class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    region = Column(String, nullable=False)  # e.g., Phuket, Krabi, or Phuket-Krabi
    duration_nights = Column(Integer, nullable=False)  # e.g., 5 nights
    is_recommended = Column(Integer, default=0)  # 1 for recommended itineraries

    # Relationships
    days = relationship(
        "ItineraryDay", back_populates="itinerary", order_by="ItineraryDay.day_number"
    )

    def __repr__(self):
        return f"<Itinerary {self.name} ({self.duration_nights} nights)>"


class ItineraryDay(Base):
    __tablename__ = "itinerary_days"

    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"), nullable=False)
    day_number = Column(
        Integer, nullable=False
    )  # 1-based index of the day in the itinerary
    transfer_id = Column(
        Integer, ForeignKey("transfers.id"), nullable=True
    )  # Optional transfer for this day

    # Relationships
    itinerary = relationship("Itinerary", back_populates="days")
    hotel_stay = relationship(
        "HotelStay", back_populates="itinerary_day", uselist=False
    )
    transfer = relationship("Transfer", back_populates="itinerary_days")
    activities = relationship(
        "Activity", secondary=itinerary_activity, back_populates="itinerary_days"
    )

    def __repr__(self):
        return f"<ItineraryDay {self.day_number} of Itinerary {self.itinerary_id}>"


class HotelStay(Base):
    __tablename__ = "hotel_stays"

    id = Column(Integer, primary_key=True, index=True)
    itinerary_day_id = Column(
        Integer, ForeignKey("itinerary_days.id"), nullable=False, unique=True
    )
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)

    # Relationships
    itinerary_day = relationship("ItineraryDay", back_populates="hotel_stay")
    hotel = relationship("Hotel", back_populates="stays")

    def __repr__(self):
        return f"<HotelStay at {self.hotel_id} for Day {self.itinerary_day.day_number}>"
