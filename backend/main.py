from database import engine, Base
import models

def main():
    
    try:
        print("==================================================")
        print("Verifico la connessione al database")
        Base.metadata.create_all(bind=engine)
        print("Database configurato correttamente!")
        print("Avvio dell'applicazione...")
        print("==================================================")
        
    except Exception as e:
        print("\n[ERROR] Si è verificato un errore durante la connessione o la creazione delle tabelle:")
        print(f"[ERROR] {e}")
        print("\nVerifica che:")
        print("1. Il servizio MySQL sia avviato sul tuo computer.")
        print("2. La password in database.py sia corretta.")
        print("3. Tu abbia creato il database vuoto con il comando: CREATE DATABASE ecommerce_isa;")
        print("==================================================")

if __name__ == "__main__":
    main()