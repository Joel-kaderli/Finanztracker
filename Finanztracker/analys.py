# analyse.py
import sqlite3
import matplotlib.pyplot as plt

def analyse_ausgaben():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("Keine Daten vorhanden.")
        return

    kategorien, betraege = zip(*data)
    plt.figure(figsize=(6, 4))
    plt.bar(kategorien, betraege, color='teal')
    plt.title("Ausgaben nach Kategorie")
    plt.xlabel("Kategorie")
    plt.ylabel("CHF")
    plt.tight_layout()
    plt.show()
