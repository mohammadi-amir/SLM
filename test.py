import openai
import requests
from tkinter import Tk, Entry, Button, Label

from openai import base_url

# Hauptfenster erstellen
root = Tk()
root.title("API-Antwort in Ausgabe-Field")

# Eingabe-Entry erstellen (z.B. für Benutzereingaben oder Parameter)
entry_input = Entry(root)
entry_input.pack(pady=10)

# Ausgabe-Label erstellen
output_label = Label(root, text="", wraplength=400, justify="left", fg="green")
output_label.pack(pady=10)


# Funktion zur API-Abfrage und Anzeige der Antwort
def call_api():
    user_input = entry_input.get()

    # API-URL und Key (ersetze 'your_api_url' und 'your_api_key' mit echten Werten)
    api_url = "http://127.0.0.1:11434/v1"  # Setze deine URL ein
    api_key = "nokeyneeded" # Dein API-Schlüssel

    try:
        # API-Anfrage senden (z. B. mit GET)
        response = requests.get(api_url, params={"query": user_input}, headers={"Authorization": f"Bearer {api_key}"})
        response.raise_for_status()  # Fehler abfangen

        # Antwort anzeigen (z.B. JSON-Inhalt)
        api_response = response.json()
        output_text = api_response.get("message", "Keine Nachricht erhalten")  # Anpassen an deine API-Struktur

        # Antwort im Label anzeigen
        output_label.config(text=output_text)

    except requests.exceptions.RequestException as e:
        # Fehler anzeigen
        output_label.config(text=f"Fehler: {e}")


# Button zum Abrufen der API-Antwort erstellen
button = Button(root, text="API-Abfrage senden", command=call_api)
button.pack(pady=10)

# Haupt-Loop starten
root.mainloop()