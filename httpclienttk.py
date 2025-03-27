import tkinter as tk
from tkinter import messagebox
import requests
import json

# URL de base du serveur
BASE_URL = "http://localhost:8080"

def list_parties():
    try:
        response = requests.get(f"{BASE_URL}/list_parties")
        if response.status_code == 200:
            parties = response.json()["id_parties"]
            for widget in parties_frame.winfo_children():
                widget.destroy()
            for id_party in parties:
                tk.Label(parties_frame, text=f"Partie {id_party}:").pack(anchor='w')
                tk.Button(parties_frame, text="S'inscrire", command=lambda id=id_party: subscribe_to_party(id)).pack(anchor='w')
        else:
            messagebox.showinfo("Erreur", "Impossible de récupérer les parties.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la connexion au serveur: {e}")

def subscribe_to_party(id_party):
    player = entry_player.get() if entry_player.get() else f"Player_{id_party}"
    data = {
        "player": player,
        "id_party": id_party
    }
    try:
        response = requests.post(f"{BASE_URL}/subscribe", json=data)
        if response.status_code == 200:
            result = response.json()["response"]
            messagebox.showinfo("Inscription", f"Rôle: {result['role']}, ID Joueur: {result['id_player']}")
        else:
            messagebox.showinfo("Erreur", "Impossible de s'inscrire à la partie.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la connexion au serveur: {e}")

def create_gui():
    global parties_frame
    global entry_player

    root = tk.Tk()
    root.title("Client HTTP Tkinter")

    # Frame pour afficher les parties
    parties_frame = tk.Frame(root)
    parties_frame.pack(pady=5)

    # Bouton pour lister les parties
    tk.Button(root, text="Lister les parties", command=list_parties).pack(pady=5)

    # Champ de saisie pour le pseudo du joueur
    tk.Label(root, text="Nom du joueur (optionnel):").pack()
    entry_player = tk.Entry(root)
    entry_player.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
