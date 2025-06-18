import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# La contraseña va antes del "@" y el último corchete y paréntesis estaban faltando
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{os.environ['DATABASE_USER']}:"  # Usuario y dos puntos
    f"{os.environ['DATABASE_PASSWORD']}@"           # Contraseña y arroba
    f"{os.environ['DATABASE_HOST']}/"               # Host y barra
    f"{os.environ['DATABASE_NAME']}"                # Nombre de la BD (corchete de cierre)
) # Parentesis de cierre de la f-string

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()