from sqlalchemy.orm import Session
from app.models.models import (
    Location,
    Hotel,
    Transfer,
    Activity,
    Itinerary,
    ItineraryDay,
    HotelStay,
    TransferType,
)
from app.database.connection import engine, Base, SessionLocal


def seed_database(db: Session):
    print("Creating locations...")
    phuket = Location(
        name="Phuket",
        region="Phuket",
        description="Thailand's largest island known for beaches, resorts, and nightlife.",
    )
    patong = Location(
        name="Patong",
        region="Phuket",
        description="Most popular beach resort in Phuket with vibrant nightlife and shopping.",
    )
    kata = Location(
        name="Kata",
        region="Phuket",
        description="Family-friendly beach known for surfing during monsoon season.",
    )
    karon = Location(
        name="Karon",
        region="Phuket",
        description="Long, scenic beach with a relaxed atmosphere.",
    )

    krabi_town = Location(
        name="Krabi Town",
        region="Krabi",
        description="Provincial capital with markets, restaurants, and access to beautiful beaches.",
    )
    ao_nang = Location(
        name="Ao Nang",
        region="Krabi",
        description="Popular beach destination with limestone cliffs and island access.",
    )
    railay = Location(
        name="Railay",
        region="Krabi",
        description="Peninsula accessible only by boat, famous for rock climbing and stunning beaches.",
    )

    phi_phi = Location(
        name="Phi Phi Islands",
        region="Krabi",
        description="Group of islands with stunning beaches, crystal clear water, and vibrant marine life.",
    )

    db.add_all([phuket, patong, kata, karon, krabi_town, ao_nang, railay, phi_phi])
    db.commit()

    # Create hotels
    print("Creating hotels...")
    # Phuket hotels
    patong_beach_hotel = Hotel(
        name="Patong Beach Resort",
        location_id=patong.id,
        description="4-star hotel directly on Patong Beach with ocean views",
        rating=4.2,
        price_per_night=120.00,
    )

    kata_sun_resort = Hotel(
        name="Kata Sun Resort",
        location_id=kata.id,
        description="Family-friendly resort with large pool and spacious rooms",
        rating=4.0,
        price_per_night=95.00,
    )

    karon_beach_hotel = Hotel(
        name="Karon Beachfront Hotel",
        location_id=karon.id,
        description="Luxury beachfront hotel with spa and multiple restaurants",
        rating=4.7,
        price_per_night=180.00,
    )

    # Krabi hotels
    krabi_riverside = Hotel(
        name="Krabi Riverside Hotel",
        location_id=krabi_town.id,
        description="Modern hotel in town center with river views",
        rating=3.9,
        price_per_night=65.00,
    )

    ao_nang_cliff_resort = Hotel(
        name="Ao Nang Cliff Resort",
        location_id=ao_nang.id,
        description="Resort nestled in the cliffs with panoramic views",
        rating=4.5,
        price_per_night=150.00,
    )

    railay_beach_club = Hotel(
        name="Railay Beach Club",
        location_id=railay.id,
        description="Exclusive beach bungalows with direct beach access",
        rating=4.8,
        price_per_night=210.00,
    )

    phi_phi_island_village = Hotel(
        name="Phi Phi Island Village",
        location_id=phi_phi.id,
        description="Luxury villas on private beach with coral reef",
        rating=4.9,
        price_per_night=250.00,
    )

    db.add_all(
        [
            patong_beach_hotel,
            kata_sun_resort,
            karon_beach_hotel,
            krabi_riverside,
            ao_nang_cliff_resort,
            railay_beach_club,
            phi_phi_island_village,
        ]
    )
    db.commit()

    # Create transfers
    print("Creating transfers...")
    # Phuket internal transfers
    phuket_to_patong = Transfer(
        origin_location_id=phuket.id,
        destination_location_id=patong.id,
        transfer_type=TransferType.TAXI,
        duration_minutes=45,
        price=20.00,
    )

    phuket_to_kata = Transfer(
        origin_location_id=phuket.id,
        destination_location_id=kata.id,
        transfer_type=TransferType.TAXI,
        duration_minutes=60,
        price=25.00,
    )

    phuket_to_karon = Transfer(
        origin_location_id=phuket.id,
        destination_location_id=karon.id,
        transfer_type=TransferType.TAXI,
        duration_minutes=50,
        price=22.00,
    )

    # Transfers between Phuket and Krabi
    phuket_to_krabi = Transfer(
        origin_location_id=phuket.id,
        destination_location_id=krabi_town.id,
        transfer_type=TransferType.BUS,
        duration_minutes=180,
        price=15.00,
    )

    patong_to_ao_nang = Transfer(
        origin_location_id=patong.id,
        destination_location_id=ao_nang.id,
        transfer_type=TransferType.FERRY,
        duration_minutes=240,
        price=35.00,
    )

    # Krabi internal transfers
    krabi_to_ao_nang = Transfer(
        origin_location_id=krabi_town.id,
        destination_location_id=ao_nang.id,
        transfer_type=TransferType.TAXI,
        duration_minutes=30,
        price=15.00,
    )

    ao_nang_to_railay = Transfer(
        origin_location_id=ao_nang.id,
        destination_location_id=railay.id,
        transfer_type=TransferType.FERRY,
        duration_minutes=15,
        price=8.00,
    )

    krabi_to_phi_phi = Transfer(
        origin_location_id=krabi_town.id,
        destination_location_id=phi_phi.id,
        transfer_type=TransferType.FERRY,
        duration_minutes=90,
        price=25.00,
    )

    db.add_all(
        [
            phuket_to_patong,
            phuket_to_kata,
            phuket_to_karon,
            phuket_to_krabi,
            patong_to_ao_nang,
            krabi_to_ao_nang,
            ao_nang_to_railay,
            krabi_to_phi_phi,
        ]
    )
    db.commit()

    # Create activities
    print("Creating activities...")
    # Phuket activities
    patong_beach_day = Activity(
        name="Patong Beach Day",
        location_id=patong.id,
        description="Full day of relaxation and water activities at Patong Beach",
        duration_minutes=360,
        price=0.00,  # Free activity
    )

    phuket_old_town_tour = Activity(
        name="Phuket Old Town Tour",
        location_id=phuket.id,
        description="Guided walking tour of Phuket's historic old town with Sino-Portuguese architecture",
        duration_minutes=180,
        price=25.00,
    )

    phi_phi_island_tour_from_phuket = Activity(
        name="Phi Phi Islands Day Trip",
        location_id=phuket.id,
        description="Full-day speedboat tour to Phi Phi Islands including snorkeling and lunch",
        duration_minutes=480,
        price=85.00,
    )

    big_buddha_visit = Activity(
        name="Big Buddha Visit",
        location_id=karon.id,
        description="Visit the famous 45-meter tall Big Buddha statue with panoramic views",
        duration_minutes=150,
        price=10.00,
    )

    # Krabi activities
    four_islands_tour = Activity(
        name="Four Islands Tour",
        location_id=ao_nang.id,
        description="Visit Chicken Island, Tup Island, Poda Island, and Phranang Cave Beach",
        duration_minutes=420,
        price=40.00,
    )

    tiger_cave_temple = Activity(
        name="Tiger Cave Temple Hike",
        location_id=krabi_town.id,
        description="Challenging hike up 1,260 steps to a sacred temple with stunning views",
        duration_minutes=240,
        price=15.00,
    )

    rock_climbing_railay = Activity(
        name="Rock Climbing at Railay",
        location_id=railay.id,
        description="Rock climbing session on Railay's world-famous limestone cliffs",
        duration_minutes=300,
        price=60.00,
    )

    phi_phi_viewpoint_hike = Activity(
        name="Phi Phi Viewpoint Hike",
        location_id=phi_phi.id,
        description="Hike to the famous viewpoint overlooking the twin bays of Phi Phi",
        duration_minutes=120,
        price=0.00,  # Free activity
    )

    db.add_all(
        [
            patong_beach_day,
            phuket_old_town_tour,
            phi_phi_island_tour_from_phuket,
            big_buddha_visit,
            four_islands_tour,
            tiger_cave_temple,
            rock_climbing_railay,
            phi_phi_viewpoint_hike,
        ]
    )
    db.commit()

    # Create itineraries
    print("Creating itineraries...")
    # 3-night Phuket itinerary
    phuket_short = Itinerary(
        name="Phuket Quick Escape",
        description="A short 3-night introduction to Phuket's highlights",
        region="Phuket",
        duration_nights=3,
        is_recommended=1,
    )
    db.add(phuket_short)
    db.commit()

    # Create itinerary days
    phuket_day1 = ItineraryDay(
        itinerary_id=phuket_short.id, day_number=1, transfer_id=phuket_to_patong.id
    )
    db.add(phuket_day1)
    db.commit()

    # Add hotel stay
    stay1 = HotelStay(itinerary_day_id=phuket_day1.id, hotel_id=patong_beach_hotel.id)
    db.add(stay1)
    db.commit()

    # Add activities to day 1
    phuket_day1.activities.append(patong_beach_day)
    db.commit()

    # Day 2
    phuket_day2 = ItineraryDay(itinerary_id=phuket_short.id, day_number=2)
    db.add(phuket_day2)
    db.commit()

    stay2 = HotelStay(itinerary_day_id=phuket_day2.id, hotel_id=patong_beach_hotel.id)
    db.add(stay2)
    db.commit()

    phuket_day2.activities.append(phuket_old_town_tour)
    db.commit()

    # Day 3
    phuket_day3 = ItineraryDay(itinerary_id=phuket_short.id, day_number=3)
    db.add(phuket_day3)
    db.commit()

    stay3 = HotelStay(itinerary_day_id=phuket_day3.id, hotel_id=patong_beach_hotel.id)
    db.add(stay3)
    db.commit()

    phuket_day3.activities.append(phi_phi_island_tour_from_phuket)
    db.commit()

    # 5-night Krabi itinerary
    krabi_medium = Itinerary(
        name="Krabi Explorer",
        description="A 5-night journey through Krabi's stunning landscapes",
        region="Krabi",
        duration_nights=5,
        is_recommended=1,
    )
    db.add(krabi_medium)
    db.commit()

    # Day 1
    krabi_day1 = ItineraryDay(
        itinerary_id=krabi_medium.id, day_number=1, transfer_id=krabi_to_ao_nang.id
    )
    db.add(krabi_day1)
    db.commit()

    stay_k1 = HotelStay(
        itinerary_day_id=krabi_day1.id, hotel_id=ao_nang_cliff_resort.id
    )
    db.add(stay_k1)
    db.commit()

    # Day 2
    krabi_day2 = ItineraryDay(itinerary_id=krabi_medium.id, day_number=2)
    db.add(krabi_day2)
    db.commit()

    stay_k2 = HotelStay(
        itinerary_day_id=krabi_day2.id, hotel_id=ao_nang_cliff_resort.id
    )
    db.add(stay_k2)
    db.commit()

    krabi_day2.activities.append(four_islands_tour)
    db.commit()

    # Day 3
    krabi_day3 = ItineraryDay(
        itinerary_id=krabi_medium.id, day_number=3, transfer_id=ao_nang_to_railay.id
    )
    db.add(krabi_day3)
    db.commit()

    stay_k3 = HotelStay(itinerary_day_id=krabi_day3.id, hotel_id=railay_beach_club.id)
    db.add(stay_k3)
    db.commit()

    krabi_day3.activities.append(rock_climbing_railay)
    db.commit()

    # Day 4
    krabi_day4 = ItineraryDay(itinerary_id=krabi_medium.id, day_number=4)
    db.add(krabi_day4)
    db.commit()

    stay_k4 = HotelStay(itinerary_day_id=krabi_day4.id, hotel_id=railay_beach_club.id)
    db.add(stay_k4)
    db.commit()

    # Day 5
    krabi_day5 = ItineraryDay(
        itinerary_id=krabi_medium.id, day_number=5, transfer_id=krabi_to_phi_phi.id
    )
    db.add(krabi_day5)
    db.commit()

    stay_k5 = HotelStay(
        itinerary_day_id=krabi_day5.id, hotel_id=phi_phi_island_village.id
    )
    db.add(stay_k5)
    db.commit()

    krabi_day5.activities.append(phi_phi_viewpoint_hike)
    db.commit()

    # 7-night Phuket & Krabi combined itinerary
    combined_long = Itinerary(
        name="Thailand Beach Paradise",
        description="The ultimate 7-night adventure combining Phuket and Krabi",
        region="Phuket-Krabi",
        duration_nights=7,
        is_recommended=1,
    )
    db.add(combined_long)
    db.commit()

    # Days 1-3 in Phuket
    # Day 1
    combined_day1 = ItineraryDay(
        itinerary_id=combined_long.id, day_number=1, transfer_id=phuket_to_patong.id
    )
    db.add(combined_day1)
    db.commit()

    stay_c1 = HotelStay(
        itinerary_day_id=combined_day1.id, hotel_id=patong_beach_hotel.id
    )
    db.add(stay_c1)
    db.commit()

    combined_day1.activities.append(patong_beach_day)
    db.commit()

    # Day 2
    combined_day2 = ItineraryDay(itinerary_id=combined_long.id, day_number=2)
    db.add(combined_day2)
    db.commit()

    stay_c2 = HotelStay(
        itinerary_day_id=combined_day2.id, hotel_id=patong_beach_hotel.id
    )
    db.add(stay_c2)
    db.commit()

    combined_day2.activities.append(phuket_old_town_tour)
    db.commit()

    # Day 3
    combined_day3 = ItineraryDay(itinerary_id=combined_long.id, day_number=3)
    db.add(combined_day3)
    db.commit()

    stay_c3 = HotelStay(
        itinerary_day_id=combined_day3.id, hotel_id=karon_beach_hotel.id
    )
    db.add(stay_c3)
    db.commit()

    combined_day3.activities.append(big_buddha_visit)
    db.commit()

    # Day 4 - Transfer to Krabi
    combined_day4 = ItineraryDay(
        itinerary_id=combined_long.id, day_number=4, transfer_id=patong_to_ao_nang.id
    )
    db.add(combined_day4)
    db.commit()

    stay_c4 = HotelStay(
        itinerary_day_id=combined_day4.id, hotel_id=ao_nang_cliff_resort.id
    )
    db.add(stay_c4)
    db.commit()

    # Day 5
    combined_day5 = ItineraryDay(itinerary_id=combined_long.id, day_number=5)
    db.add(combined_day5)
    db.commit()

    stay_c5 = HotelStay(
        itinerary_day_id=combined_day5.id, hotel_id=ao_nang_cliff_resort.id
    )
    db.add(stay_c5)
    db.commit()

    combined_day5.activities.append(four_islands_tour)
    db.commit()

    # Day 6 - Transfer to Railay
    combined_day6 = ItineraryDay(
        itinerary_id=combined_long.id, day_number=6, transfer_id=ao_nang_to_railay.id
    )
    db.add(combined_day6)
    db.commit()

    stay_c6 = HotelStay(
        itinerary_day_id=combined_day6.id, hotel_id=railay_beach_club.id
    )
    db.add(stay_c6)
    db.commit()

    combined_day6.activities.append(rock_climbing_railay)
    db.commit()

    # Day 7
    combined_day7 = ItineraryDay(itinerary_id=combined_long.id, day_number=7)
    db.add(combined_day7)
    db.commit()

    stay_c7 = HotelStay(
        itinerary_day_id=combined_day7.id, hotel_id=railay_beach_club.id
    )
    db.add(stay_c7)
    db.commit()

    print("Database seeded successfully!")


def init_db():
    print("Initialising Database...")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # Check if database is already seeded by checking for a location
        location = db.query(Location).first()
        if not location:
            seed_database(db)
    finally:
        db.close()
