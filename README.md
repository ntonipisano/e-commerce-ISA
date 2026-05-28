# Configurazione Database e Avvio del Backend

## 2. Creare il Database su MySQL Workbench

Apri MySQL Workbench, connettiti al tuo server locale ed esegui la seguente query per creare il database vuoto:

```sql
CREATE DATABASE ecommerce_isa;
```

---

# 🚀 Installazione e Avvio

## 1. Clonare il progetto e posizionarsi nella cartella

```bash
git clone https://github.com/ntonipisano/e-commerce-ISA.git
cd e-commerce-ISA/backend
```

---

## 2. Configurare le variabili d'ambiente (.env)

Crea un file chiamato `.env` nella radice della cartella `backend/`.

Questo file è inserito nel `.gitignore` e **non deve essere caricato su GitHub** poiché contiene la tua password MySQL.

Inserisci la tua stringa di connessione specificando la password del tuo MySQL:

```env
DATABASE_URL=mysql+pymysql://root:LA_TUA_PASSWORD_DI_MYSQL@localhost:3306/ecommerce_isa
```

---

## 3. Installare le dipendenze

Grazie a `uv`, puoi sincronizzare istantaneamente l'ambiente virtuale e installare tutte le librerie necessarie.  
`uv` creerà automaticamente un ambiente virtuale locale (`.venv/`) in cui installerà tutte le dipendenze necessarie definite nel file `uv.lock`.  
Eseguire il seguente comando per fare quanto scritto su (se non presente sulla vostra macchina installare uv):

```bash
uv sync
```

---

## 4. Avviare l'applicazione

Lancia lo script principale. Al primo avvio, SQLAlchemy verificherà la connessione e creerà automaticamente tutte le tabelle sul tuo MySQL di Windows se non sono già presenti:

```bash
uv run main.py
```

Se l'inizializzazione va a buon fine, vedrai comparire il messaggio di conferma sul terminale e le tabelle saranno visibili su MySQL Workbench.