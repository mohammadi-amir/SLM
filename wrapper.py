import openai
import tkinter as tk

# Hauptfenster erstellen
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")
root.minsize(width=300, height=300)

# OpenAI-Client initialisieren
client = openai.OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="nokeyneeded",  # Für lokale Modelle ohne API-Schlüssel
)


# Funktion zum Senden und Empfangen von Nachrichten
def on_enter(event):
    user_input = e.get()  # Benutzer-Eingabe lesen
    if not user_input.strip():  # Leere Eingaben ignorieren
        return

    try:
        # API-Aufruf durchführen
        response = client.chat.completions.create(
            model="phi3",
            temperature=0.7,
            n=1,
            messages=[
                {"role": "system", "content": "Bitte antworte auf Deutsch."},
                {"role": "user", "content": user_input},
            ],
        )

        # Antwort im Fenster anzeigen
        chat_history.insert(tk.END, f"Answer: \n" ) #{user_input}\n", "user")
        chat_history.insert(tk.END, f"{response.choices[0].message.content}\n\n", "bot")

    except Exception as ex:
        chat_history.insert(tk.END, "Fehler: Konnte keine Antwort erhalten.\n", "error")

    e.delete(0, tk.END)  # Eingabefeld leeren


# Eingabefeld erstellen
e = tk.Entry(root, width=40)
e.pack(pady=10)

# Chatverlauf (Textfeld) erstellen
chat_history = tk.Text(root, wrap=tk.WORD, width=50, height=25)
chat_history.pack(pady=10)
chat_history.tag_config("user", foreground="blue")
chat_history.tag_config("bot", foreground="purple")
chat_history.tag_config("error", foreground="red")

# Enter-Taste binden
e.bind("<Return>", on_enter)

root.mainloop()


