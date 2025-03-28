from tkinter import Tk, Frame, Label, Button, Entry, StringVar, Radiobutton, messagebox, ttk
import tkinter.font as tkFont
from services.api_service import list_parties, subscribe_to_party, start_solo_game

class WolfGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Loup-Garou")
        self.root.geometry("900x600")
        self.root.configure(bg="#2E2E2E")

        self.default_font = tkFont.Font(family="Helvetica", size=11)
        self.selected_role = StringVar(value="villageois")

        self.create_widgets()
        list_parties()  # Load parties on startup

    def create_widgets(self):
        title_frame = Frame(self.root, bg="#2E2E2E", pady=10)
        title_frame.pack(fill='x')
        Label(title_frame, text="Jeu du Loup-Garou", font=tkFont.Font(family="Helvetica", size=18, weight="bold"),
              bg="#2E2E2E", fg="#FFFFFF").pack()

        button_frame = Frame(self.root, bg="#2E2E2E", pady=5)
        button_frame.pack(fill='x')
        refresh_btn = Button(button_frame, text="Rafraîchir les parties", font=self.default_font,
                              command=list_parties, bg="#404040", fg="#FFFFFF",
                              activebackground="#505050", activeforeground="#FFFFFF")
        refresh_btn.pack(pady=5)

        self.parties_frame = Frame(self.root, bg="#363636", padx=10, pady=10)
        self.parties_frame.pack(fill='both', expand=True, padx=10, pady=5)

        bottom_frame = Frame(self.root, bg="#2E2E2E", padx=10, pady=10)
        bottom_frame.pack(fill='x', side='bottom')

        controls_frame = Frame(bottom_frame, bg="#2E2E2E")
        controls_frame.pack(fill='x', pady=5)

        left_column = Frame(controls_frame, bg="#2E2E2E")
        left_column.pack(side='left', fill='x', expand=True)

        right_column = Frame(controls_frame, bg="#2E2E2E")
        right_column.pack(side='right', fill='x', expand=True, padx=(10, 0))

        Label(left_column, text="Nom du joueur:", font=self.default_font, 
              bg="#2E2E2E", fg="#FFFFFF").pack(anchor='w', pady=(0, 5))
        
        self.entry_player = Entry(left_column, font=self.default_font, bg="#505050", fg="#FFFFFF",
                                  insertbackground="#FFFFFF")
        self.entry_player.pack(fill='x', pady=(0, 5))

        Label(right_column, text="Préférence de rôle:", font=self.default_font, 
              bg="#2E2E2E", fg="#FFFFFF").pack(anchor='w', pady=(0, 5))

        role_frame = Frame(right_column, bg="#2E2E2E")
        role_frame.pack(fill='x')

        villager_radio = Radiobutton(role_frame, text="Villageois", variable=self.selected_role, value="villageois",
                                      font=self.default_font, bg="#2E2E2E", fg="#FFFFFF", selectcolor="#505050",
                                      activebackground="#2E2E2E", activeforeground="#FFFFFF")
        villager_radio.pack(side='left', padx=(0, 10))

        werewolf_radio = Radiobutton(role_frame, text="Loup-Garou", variable=self.selected_role, value="loup-garou",
                                      font=self.default_font, bg="#2E2E2E", fg="#FFFFFF", selectcolor="#505050",
                                      activebackground="#2E2E2E", activeforeground="#FFFFFF")
        werewolf_radio.pack(side='left')

        buttons_frame = Frame(bottom_frame, bg="#2E2E2E")
        buttons_frame.pack(fill='x', pady=10)

        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        subscribe_btn = Button(buttons_frame, text="S'inscrire à la partie", font=self.default_font,
                               command=subscribe_to_party, bg="#404040", fg="#FFFFFF",
                               activebackground="#505050", activeforeground="#FFFFFF")
        subscribe_btn.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        solo_btn = Button(buttons_frame, text="Mode Solo", font=self.default_font,
                          command=start_solo_game, bg="#404040", fg="#FFFFFF",
                          activebackground="#505050", activeforeground="#FFFFFF")
        solo_btn.grid(row=0, column=1, padx=(5, 0), sticky="ew")

def main():
    root = Tk()
    app = WolfGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()