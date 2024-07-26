import customtkinter as ctk
from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color = darkGray)
        self.pack(fill = "x", pady = 4, ipady = 8)


class SliderPanel(Panel):
    def __init__(self, parent, text):
        super().__init__(parent = parent)
        
        # Gridded Layout
        self.rowconfigure((0,1), weight = 1)
        self.columnconfigure((0,1), weight = 1)

        # Labels
        ctk.CTkLabel(self, text = text).grid(column = 0, row = 0, sticky = "w", padx = 5)
        ctk.CTkLabel(self, text = 0.0).grid(column = 1, row = 0, sticky = "e", padx = 5)

        # Slider
        ctk.CTkSlider(self, fg_color = sliderBackground).grid(column = 1, columnspan = 2, row = 1, sticky = "ew", padx = 5, pady = 5)