from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


# Enum for transfer types
class TransferTypeEnum(str, Enum):
    TAXI = "taxi"
    BUS = "bus"
    FERRY = "ferry"
    PRIVATE_CAR = "private_car"
    AIRPLANE = "airplane"


# Location Schemas
class LocationBase(BaseModel):
    name: str
    region: str
    description: Optional[str] = None


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int

    model_config = {"from_attributes": True}


# Hotel Schemas
class HotelBase(BaseModel):
    name: str
    location_id: int
    description: Optional[str] = None
    rating: Optional[float] = None
    price_per_night: Optional[float] = None


class HotelCreate(HotelBase):
    pass


class Hotel(HotelBase):
    id: int

    model_config = {"from_attributes": True}


# Transfer Schemas
class TransferBase(BaseModel):
    origin_location_id: int
    destination_location_id: int
    transfer_type: TransferTypeEnum
    duration_minutes: Optional[int] = None
    price: Optional[float] = None


class TransferCreate(TransferBase):
    pass


class Transfer(TransferBase):
    id: int

    model_config = {"from_attributes": True}


# Activity Schemas
class ActivityBase(BaseModel):
    name: str
    location_id: int
    description: Optional[str] = None
    duration_minutes: Optional[int] = None
    price: Optional[float] = None


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: int

    model_config = {"from_attributes": True}


# HotelStay Schemas
class HotelStayBase(BaseModel):
    hotel_id: int


class HotelStayCreate(HotelStayBase):
    pass


class HotelStay(HotelStayBase):
    id: int
    itinerary_day_id: int

    model_config = {"from_attributes": True}


# ItineraryDay Schemas for Creation
class ItineraryDayCreate(BaseModel):
    day_number: int
    transfer_id: Optional[int] = None
    hotel_id: int
    activity_ids: List[int] = []


# ItineraryDay Schema for Response
class ItineraryDay(BaseModel):
    id: int
    day_number: int
    transfer: Optional[Transfer] = None
    hotel_stay: Optional[HotelStay] = None
    activities: List[Activity] = []

    model_config = {"from_attributes": True}


# Itinerary Schemas
class ItineraryBase(BaseModel):
    name: str
    description: Optional[str] = None
    region: str
    duration_nights: int
    is_recommended: Optional[int] = 0


class ItineraryCreate(ItineraryBase):
    days: List[ItineraryDayCreate]


class Itinerary(ItineraryBase):
    id: int
    days: List[ItineraryDay] = []

    model_config = {"from_attributes": True}


# Schema for detailed itinerary response with expanded relationships
class ItineraryDetailed(Itinerary):
    pass
