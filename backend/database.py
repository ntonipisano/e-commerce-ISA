import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Carica le variabili dal file .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("ERRORE: La variabile DATABASE_URL non è impostata nel file .env!")

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "mysql+pymysql://root:28112002@localhost:3306/ecommerce_isa"
)

# L'Engine gestisce la connessione fisica al database
engine = create_engine(
    DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# La classe Base da cui ereditano tutti i modelli in models.py
Base = declarative_base()

def get_db():
    """Funzione di utilità per aprire e chiudere la sessione del DB in sicurezza"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()