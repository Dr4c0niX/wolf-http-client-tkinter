import tkinter as tk
from gui.interface import create_gui

def main():
    root = tk.Tk()
    root.title("Client Loup-Garou")
    create_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()