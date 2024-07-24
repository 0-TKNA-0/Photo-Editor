import customtkinter as ctk
from imageWidgets import *

class Editor(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry("1000x600")
        self.title("Photo Editor")
        self.minsize(800, 500)

        # Layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 2)
        self.columnconfigure(1, weight = 6)

        # Widgets
        ImageImport(self, self.importImage)

        self.mainloop()

    def importImage(self, path):
        pass

Editor()