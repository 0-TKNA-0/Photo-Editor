import customtkinter as ctk
from menuPanels import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, rotation, zoom):
        super().__init__(master = parent)
        self.grid(row = 0, column = 0, sticky = "nsew", pady = 10, padx = 10)

        # Tabs
        self.add("Position")
        self.add("Colour")
        self.add("Effects")
        self.add("Export")

        # Places frame inside tab
        PositionFrame(self.tab("Position"), rotation, zoom)
        ColourFrame(self.tab("Colour"))

class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, rotation, zoom):
        super().__init__(master = parent, fg_color = "transparent")
        self.pack(expand = True, fill = "both")
        
        # Places panels
        SliderPanel(self, "Rotation", rotation, 0, 360)
        SliderPanel(self, "Zoom", zoom, 0, 200)

class ColourFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent)
        self.pack(expand = True, fill = "both")
