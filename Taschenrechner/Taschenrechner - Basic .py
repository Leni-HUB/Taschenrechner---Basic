import tkinter as tk
from tkinter import messagebox

# Funktion zur Berechnung
def berechne():
    try:
        zahl1 = float(entry1.get())
        zahl2 = float(entry2.get())
        zeichen = operation.get()

        if zeichen == "+":
            ergebnis = zahl1 + zahl2
        elif zeichen == "-":
            ergebnis = zahl1 - zahl2
        elif zeichen == "*":
            ergebnis = zahl1 * zahl2
        elif zeichen == "/":
            if zahl2 == 0:
                raise ZeroDivisionError("Division durch Null ist nicht erlaubt.")
            ergebnis = zahl1 / zahl2
        else:
            messagebox.showerror("Fehler", "Ungültiges Rechenzeichen!")
            return

        messagebox.showinfo("Ergebnis", f"Das Ergebnis ist: {ergebnis}")
    except ValueError:
        messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben!")
    except ZeroDivisionError as e:
        messagebox.showerror("Fehler", str(e))

# Hauptfenster erstellen
root = tk.Tk()
root.title("Taschenrechner")

# Eingabefelder und Labels
tk.Label(root, text="Erste Zahl:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Zweite Zahl:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Dropdown-Menü für Rechenzeichen
tk.Label(root, text="Rechenzeichen:").grid(row=2, column=0, padx=10, pady=10)
operation = tk.StringVar(root)
operation.set("+")  # Standardwert
dropdown = tk.OptionMenu(root, operation, "+", "-", "*", "/")
dropdown.grid(row=2, column=1, padx=10, pady=10)

# Berechnen-Button
button = tk.Button(root, text="Berechnen", command=berechne)
button.grid(row=3, column=0, columnspan=2, pady=20)

# Hauptfenster starten
root.mainloop()