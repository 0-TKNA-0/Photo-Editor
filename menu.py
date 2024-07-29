import customtkinter as ctk
from menuPanels import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, posVars, colourVars, effectVars):
        super().__init__(master = parent)
        self.grid(row = 0, column = 0, sticky = "nsew", pady = 10, padx = 10)

        # Tabs
        self.add("Position")
        self.add("Colour")
        self.add("Effects")
        self.add("Export")

        # Places frame inside tab
        PositionFrame(self.tab("Position"), posVars)
        ColourFrame(self.tab("Colour"), colourVars)
        EffectFrame(self.tab("Effects"), effectVars)
        ExportFrame(self.tab("Export"))

class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, posVars):
        super().__init__(master = parent, fg_color = "transparent")
        self.pack(expand = True, fill = "both")
        
        # Places panels
        SliderPanel(self, "Rotation", posVars["rotate"], 0, 360)
        SliderPanel(self, "Zoom", posVars["zoom"], 0, 200)

        # Place segmented button panel
        SegmentedPanel(self, "Invert", posVars["flip"], flipOption)

        # Place revert button
        RevertButton(self, 
            (posVars["rotate"], rotateDefault), 
            (posVars["zoom"], zoomDefault), 
            (posVars["flip"], flipOption[0]))

class ColourFrame(ctk.CTkFrame):
    def __init__(self, parent, colourVars):
        super().__init__(master = parent)
        self.pack(expand = True, fill = "both")

        # Places Switch panels
        SwitchPanel(self, (colourVars["grayScale"], "B/W"), (colourVars["invert"], "Invert"))

        # Places panels
        SliderPanel(self, "Brightness", colourVars["brightness"], 0, 5)
        SliderPanel(self, "Vibrance", colourVars["vibrance"], 0, 5)

        # Place revert button
        RevertButton(self, 
            (colourVars["brightness"], brightnessDefault), 
            (colourVars["grayScale"], grayScaleDefault), 
            (colourVars["invert"], invertDefault), 
            (colourVars["vibrance"], vibranceDefault))

class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent, effectVars):
        super().__init__(master = parent)
        self.pack(expand = True, fill = "both")

        # Places drop down panel
        DropDownPanel(self, effectVars["effect"], effectOption)

        # Places panels
        SliderPanel(self, "Blur", effectVars["blur"], 0, 30)
        SliderPanel(self, "Contrast", effectVars["contrast"], 0, 10)

        # Place revert button
        RevertButton(self, 
            (effectVars["blur"], blurDefault), 
            (effectVars["contrast"], contrastDefault), 
            (effectVars["effect"], effectOption[0]))

class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent)
        self.pack(expand = True, fill = "both")
        
        # data
        self.nameString = ctk.StringVar()
        self.fileString = ctk.StringVar(value = "jpg")
        self.pathString = ctk.StringVar()

        # widgets
        FileNamePanel(self, self.nameString, self.fileString)
        FilePathPanel(self, self.pathString)

