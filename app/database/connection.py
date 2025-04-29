from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator, Union

SQLALCHEMY_DATABASE_URL = "sqlite:///./travel_itinerary.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db(mcp: bool = False) -> Union[Session, Generator[Session, None, None]]:
    db = SessionLocal()
    try:
        if mcp:
            return db
        else:
            yield db
    finally:
        if not mcp:
            db.close()
