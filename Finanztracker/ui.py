import tkinter as tk
from tkinter import messagebox, ttk
import database
import analysen
from analys import analyse_ausgaben


# GUI-Setup
def setup_ui():
    root = tk.Tk()
    root.title("Finanztracker")

    # Eingabefelder
    tk.Label(root, text="Betrag").grid(row=0, column=0)
    entry_amount = tk.Entry(root)
    entry_amount.grid(row=0, column=1)

    tk.Label(root, text="Kategorie").grid(row=1, column=0)
    entry_category = tk.Entry(root)
    entry_category.grid(row=1, column=1)

    # Transaktion hinzufügen
    def handle_add():
        amount = entry_amount.get()
        category = entry_category.get()
        if not amount or not category:
            messagebox.showerror("Fehler", "Bitte alle Felder ausfüllen")
            return
        try:
            database.add_transaction(float(amount), category)
            entry_amount.delete(0, tk.END)
            entry_category.delete(0, tk.END)
            messagebox.showinfo("Erfolg", "Eintrag hinzugefügt")
            load_transactions()
        except ValueError:
            messagebox.showerror("Fehler", "Ungültiger Betrag")

    tk.Button(root, text="Hinzufügen", command=handle_add).grid(row=2, column=0, columnspan=2)

    # Transaktionen anzeigen
    tree = ttk.Treeview(root, columns=("ID", "Betrag", "Kategorie", "Datum"), show="headings")
    tree.grid(row=3, column=0, columnspan=2)
    tree.heading("ID", text="ID")
    tree.heading("Betrag", text="Betrag (€)")
    tree.heading("Kategorie", text="Kategorie")
    tree.heading("Datum", text="Datum")

    def load_transactions():
        for row in tree.get_children():
            tree.delete(row)
        for trans in database.get_transactions():
            tree.insert("", "end", values=trans)

    tk.Button(root, text="Aktualisieren", command=load_transactions).grid(row=4, column=0, columnspan=2)

    def show_total_spent():
        total = analysen.get_total_spent()
        messagebox.showinfo("Gesamtausgaben", f"Du hast insgesamt {total:.2f} CHF ausgegeben.")

    tk.Button(root, text="Gesamtausgaben", command=show_total_spent).grid(row=6, column=0, columnspan=2)



    # Neuen Button hinzufügen
    tk.Button(root, text="Ausgaben analysieren", command=analyse_ausgaben).grid(row=5, column=0, columnspan=2)

    load_transactions()
    root.mainloop()
