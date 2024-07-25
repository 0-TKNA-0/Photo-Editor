import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, importFunction):
        super().__init__(master = parent)

        self.grid(column = 0, columnspan = 2, row = 0, sticky = "nsew")
        self.importFunction = importFunction

        ctk.CTkButton(self, text = "Import Image", command = self.openDialog).pack(expand = True)
    
    def openDialog(self):
        path = filedialog.askopenfile().name # gets the actual path of the image once the user has selected it
        self.importFunction(path)

class ImageOutput(Canvas):
    def __init__(self, parent, resizeImage):
        super().__init__(master = parent, background = backgroundColour, bd = 0, highlightthickness = 0, relief = "ridge")
        self.grid(row = 0, column = 1, sticky = "nsew")
        self.bind("<Configure>", resizeImage)