import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Intentamos usar la variable DATABASE_URL completa (por ejemplo en Render)
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    # Si no está, armamos la URL con variables individuales (útil para local)
    DATABASE_URL = (
        f"postgresql://{os.environ.get('DATABASE_USER')}:"  
        f"{os.environ.get('DATABASE_PASSWORD')}@"           
        f"{os.environ.get('DATABASE_HOST')}/"               
        f"{os.environ.get('DATABASE_NAME')}"
    )

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
