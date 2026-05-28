import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

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