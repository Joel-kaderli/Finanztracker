import sqlite3
from datetime import datetime

# Verbindung zur Datenbank herstellen
def get_db_connection():
    return sqlite3.connect("finance.db")

# Tabelle erstellen (falls nicht vorhanden)
def setup_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL,
                        category TEXT,
                        date TEXT)''')
    conn.commit()
    conn.close()

# Eintrag hinzufügen
def add_transaction(amount, category):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (amount, category, date) VALUES (?, ?, ?)",
                   (amount, category, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()

# Alle Transaktionen abrufen
def get_transactions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    data = cursor.fetchall()
    conn.close()
    return data
