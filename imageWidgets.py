import customtkinter as ctk

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, importFunction):
        super().__init__(master = parent)

        self.grid(column = 0, columnspan = 2, row = 0, sticky = "nsew")
        self.importFunction = importFunction

        ctk.CTkButton(self, text = "Import Image", command = self.openDialog).pack(expand = True)
    
    def openDialog(self):
        path = "test"
        self.importFunction(path)