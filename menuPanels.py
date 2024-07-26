import customtkinter as ctk
from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color = darkGray)
        self.pack(fill = "x", pady = 4, ipady = 8)

class SliderPanel(Panel):
    def __init__(self, parent, text, dataVar, minValue, maxValue):
        super().__init__(parent = parent)
        
        # Gridded Layout
        self.rowconfigure((0,1), weight = 1)
        self.columnconfigure((0,1), weight = 1)

        # Labels
        ctk.CTkLabel(self, text = text).grid(column = 0, row = 0, sticky = "w", padx = 5)
        self.numberLabel = ctk.CTkLabel(self, text = dataVar.get())
        self.numberLabel.grid(column = 1, row = 0, sticky = "e", padx = 5)

        # Slider
        ctk.CTkSlider(
            self, 
            fg_color = sliderBackground,
            command = self.updateText, 
            variable = dataVar, 
            from_= minValue, 
            to = maxValue
            ).grid(column = 1, columnspan = 2, row = 1, sticky = "ew", padx = 5, pady = 5)
    
    # function to round the dataVar to 2 decimal points
    def updateText(self, value):
        self.numberLabel.configure(text = f"{round(value, 2)}")
