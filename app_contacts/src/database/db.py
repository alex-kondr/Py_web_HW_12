import configparser
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


path = Path(__file__).parent
config = configparser.ConfigParser()
config.read(path.joinpath("config.ini"))
db_url_elefant = config.get("DB", "url_elefant")
# db_url_postgres = config.get("DB", "url_postgres")
engine = create_engine(db_url_elefant)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    
    try:
        yield db
        
    finally:
        db.close()