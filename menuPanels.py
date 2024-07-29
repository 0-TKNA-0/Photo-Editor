import customtkinter as ctk
from tkinter import filedialog
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

        # tracing
        self.dataVar = dataVar
        self.dataVar.trace("w", self.updateText)

        # Labels
        ctk.CTkLabel(self, text = text).grid(column = 0, row = 0, sticky = "w", padx = 5)
        self.numberLabel = ctk.CTkLabel(self, text = dataVar.get())
        self.numberLabel.grid(column = 1, row = 0, sticky = "e", padx = 5)

        # Slider
        ctk.CTkSlider(
            self, 
            fg_color = sliderBackground, 
            variable = self.dataVar, 
            from_= minValue, 
            to = maxValue
            ).grid(column = 1, columnspan = 2, row = 1, sticky = "ew", padx = 5, pady = 5)
    
    # function to round the dataVar to 2 decimal points
    def updateText(self, *args):
        self.numberLabel.configure(text = f"{round(self.dataVar.get(), 2)}")

class SegmentedPanel(Panel):
    def __init__(self, parent, text, dataVar, options):
        super().__init__(parent = parent)

        ctk.CTkLabel(self, text = text).pack()
        ctk.CTkSegmentedButton(self, variable = dataVar, values = options).pack(expand = True, fill = "both", padx = 4, pady = 4)

class SwitchPanel(Panel):
    def __init__(self, parent, *args): # ((variable, text), (variable, text), (variable, text))
        super().__init__(parent = parent)

        for variable, text in args:
            switch = ctk.CTkSwitch(self, text = text, variable = variable, button_color = blue, fg_color = sliderBackground)
            switch.pack(side = "left", expand = True, fill = "both", padx = 5, pady = 5)

class FileNamePanel(Panel):
    def __init__(self, parent, nameString, fileString):
        super().__init__(parent = parent)

        self.nameString = nameString
        self.nameString.trace("w", self.updateText)
        self.fileString = fileString

        # entry widget
        ctk.CTkEntry(self, textvariable = self.nameString).pack(fill = "x", padx = 20, pady = 5)
        
        # frame with checkboxes
        frame = ctk.CTkFrame(self, fg_color = "transparent")
        jpgCheck = ctk.CTkCheckBox(
            frame, 
            text = "JPG", 
            variable = self.fileString, 
            command = lambda: self.click("jpg"), 
            onvalue = "jpg", 
            offvalue = "png")

        pngCheck = ctk.CTkCheckBox(
            frame, 
            text = "PNG", 
            variable = self.fileString, 
            command = lambda: self.click("png"),
            onvalue = "png", 
            offvalue = "jpg")

        jpgCheck.pack(side = "left", fill = "x", expand = True)
        pngCheck.pack(side = "left", fill = "x", expand = True)
        frame.pack(expand = True, fill = "x", padx = 20)


        # output / preview label
        self.output = ctk.CTkLabel(self, text = "")
        self.output.pack()

    def click(self, value):
        self.fileString.set(value)
        self.updateText()

    def updateText(self, *args):
        if self.nameString.get():
            text = self.nameString.get().replace(" ", "_")+ "." + self.fileString.get()
            self.output.configure(text = text) 

class FilePathPanel(Panel):
    def __init__(self, parent, pathString):
        super().__init__(parent = parent)
        self.pathString = pathString

        ctk.CTkButton(self, text = "Open Explorer", command = self.openFileDialog).pack(pady = 5)
        ctk.CTkEntry(self, textvariable = self.pathString).pack(expand = True, fill = "both", padx = 5, pady = 5)

    def openFileDialog(self):
        self.pathString.set(filedialog.askdirectory())
    

class DropDownPanel(ctk.CTkOptionMenu):
    def __init__(self, parent, dataVar, options):
        super().__init__(
            master = parent, 
            values = options, 
            fg_color = darkGray, 
            button_color = dropDownMainColour, 
            button_hover_color = dropDownHoverColour, 
            dropdown_fg_color = dropDownMenuColour,
            variable = dataVar)
        self.pack(fill = "x", pady = 4)

class RevertButton(ctk.CTkButton):
    def __init__(self, parent, *args):
        super().__init__(master = parent, text = "Revert", command = self.revert)
        self.pack(side = "bottom", pady = 10)
        self.args = args

    def revert(self):
        for variable, value in self.args:
            variable.set(value)

