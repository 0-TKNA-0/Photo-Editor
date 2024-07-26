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
        self.grid(row = 0, column = 1, sticky = "nsew", padx = 10, pady = 10)
        self.bind("<Configure>", resizeImage)

class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, closeImage):
        super().__init__(
            master = parent, 
            text = "X",
            command = closeImage, 
            text_color = white, 
            fg_color = "transparent", 
            width = 40, 
            height = 40,
            corner_radius = 0,
            hover_color = closeRed)
        self.place(relx = 0.99, rely = 0.01, anchor = "ne")