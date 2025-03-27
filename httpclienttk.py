import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import requests
import json

BASE_URL = "http://localhost:8080"

def list_parties():
    try:
        response = requests.get(f"{BASE_URL}/list_parties")
        if response.status_code == 200:
            parties = response.json()["id_parties"]
            for widget in parties_frame.winfo_children():
                widget.destroy()
            if not parties:
                tk.Label(parties_frame, text="Aucune partie disponible.", font=default_font).pack(anchor='w', pady=2)
            else:
                for party in parties:
                    info = f"ID: {party['id_party']} | Lignes: {party['nb_rows']} | Colonnes: {party['nb_cols']} | Max Joueurs: {party['max_players']}"
                    tk.Label(parties_frame, text=info, font=default_font).pack(anchor='w', pady=2)
                    tk.Button(parties_frame, text="S'inscrire", font=default_font, 
                              command=lambda id=party['id_party']: subscribe_to_party(id)).pack(anchor='w', pady=2)
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
    global parties_frame, entry_player, default_font

    root = tk.Tk()
    root.title("Client HTTP Tkinter")
    root.geometry("600x400")  # fenêtre plus grande

    # Définition d'une police par défaut pour un style cohérent
    default_font = tkFont.Font(family="Helvetica", size=11)

    # Frame pour afficher les parties
    parties_frame = tk.Frame(root, padx=10, pady=10)
    parties_frame.pack(fill='both', expand=True)

    # Bouton pour lister les parties
    tk.Button(root, text="Lister les parties", font=default_font, command=list_parties).pack(pady=5)

    # Champ de saisie pour le pseudo du joueur
    tk.Label(root, text="Nom du joueur (optionnel):", font=default_font).pack(pady=3)
    entry_player = tk.Entry(root, font=default_font)
    entry_player.pack(pady=3)

    root.mainloop()

if __name__ == "__main__":
    create_gui()