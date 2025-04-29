# Travel Itinerary Backend System

A FastAPI-based backend system for managing travel itineraries, focused on Thailand's Phuket and Krabi regions.

## Features

- **Database Architecture**: SQLAlchemy models for itineraries, accommodations, transfers, and activities
- **RESTful API**: Endpoints to create and view trip itineraries
- **Seed Data**: Pre-populated database with realistic data for Phuket and Krabi regions
- **Recommended Itineraries**: Sample itineraries ranging from 2-8 nights

## Tech Stack

- **FastAPI**: High-performance web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight database
- **Pydantic**: Data validation and settings management
- **uv**: Fast Python package installer

## Project Structure

```
.
├── app
│   ├── api
│   │   └── itinerary.py  # API routes for itineraries
│   ├── database
│   │   ├── connection.py  # Database connection setup
│   │   └── seed.py  # Database seeding logic
│   ├── models
│   │   └── models.py  # SQLAlchemy models
│   └── schemas
│       └── schemas.py  # Pydantic schemas
├── main.py  # FastAPI application entry point
└── README.md
```

## API Endpoints

### Itineraries

#### Get all itineraries

```
GET /itineraries
```

Query parameters:

- `skip` (int, optional): Number of records to skip (default: 0)
- `limit` (int, optional): Maximum number of records to return (default: 100)
- `region` (string, optional): Filter by region (e.g., "Phuket", "Krabi", "Phuket-Krabi")
- `min_nights` (int, optional): Filter by minimum number of nights
- `max_nights` (int, optional): Filter by maximum number of nights
- `recommended` (bool, optional): Filter by recommended status

#### Get a specific itinerary

```
GET /itineraries/{itinerary_id}
```

Path parameters:

- `itinerary_id` (int, required): ID of the itinerary to retrieve

#### Create a new itinerary

```
POST /itineraries
```

Request body:

```json
{
  "name": "Custom Phuket Trip",
  "description": "A custom 4-night trip to Phuket",
  "region": "Phuket",
  "duration_nights": 4,
  "is_recommended": 0,
  "days": [
    {
      "day_number": 1,
      "transfer_id": 1,
      "hotel_id": 1,
      "activity_ids": [1]
    },
    {
      "day_number": 2,
      "hotel_id": 1,
      "activity_ids": [2, 3]
    },
    {
      "day_number": 3,
      "hotel_id": 2,
      "activity_ids": [4]
    },
    {
      "day_number": 4,
      "transfer_id": 2,
      "hotel_id": 3,
      "activity_ids": []
    }
  ]
}
```

## Running the Project

1. Ensure you have Python 3.8+ installed
2. Install dependencies:

```bash
uv pip install -r requirements.txt
```

3. Run the server:

```bash
uvicorn main:app --reload
```

4. Access the API documentation at `http://localhost:8000/docs`

## Database Schema

The database is structured with the following key entities:

- **Locations**: Geographic locations in Thailand (Phuket, Krabi)
- **Hotels**: Accommodation options available in different locations
- **Activities**: Available excursions and experiences in each location
- **Transfers**: Transportation options between locations
- **Itineraries**: Complete trip plans combining hotels, activities, and transfers
- **ItineraryDays**: Individual days within an itinerary
- **HotelStays**: Hotel bookings for specific days in an itinerary
