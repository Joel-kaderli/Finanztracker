import sqlite3

def get_total_spent():
    """Berechnet die Gesamtausgaben."""
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions")
    total = cursor.fetchone()[0] or 0
    conn.close()
    return total

def get_avg_spent_per_day():
    """Berechnet die durchschnittlichen Ausgaben pro Tag."""
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(daily_total) FROM (SELECT SUM(amount) as daily_total FROM transactions GROUP BY date)")
    avg = cursor.fetchone()[0] or 0
    conn.close()
    return avg

def get_top_category():
    """Findet die Kategorie mit den höchsten Ausgaben."""
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category ORDER BY SUM(amount) DESC LIMIT 1")
    top_category = cursor.fetchone()
    conn.close()
    return top_category if top_category else ("Keine Daten", 0)

def get_monthly_spending(year, month):
    """Berechnet die Ausgaben für einen bestimmten Monat."""
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE strftime('%Y', date) = ? AND strftime('%m', date) = ?",
                   (str(year), str(month).zfill(2)))
    total = cursor.fetchone()[0] or 0
    conn.close()
    return total