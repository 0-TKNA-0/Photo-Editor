import customtkinter as ctk
from imageWidgets import *
from PIL import Image, ImageTk

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
        self.image_Import = ImageImport(self, self.importImage)

        self.mainloop()

    def importImage(self, path):
        self.image = Image.open(path)

        self.image_Import.grid_forget() # removes the import button
        self.imageOutput = ImageOutput(self)
        self.imageTK = ImageTk.PhotoImage(self.image)

        self.resizeImage()
        
    def resizeImage(self):
        self.imageOutput.create_image(0, 0, image = self.imageTK)

Editor()