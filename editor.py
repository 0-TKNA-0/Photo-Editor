import customtkinter as ctk
from imageWidgets import *
from menu import Menu
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter

# main class that contains the main window.
class Editor(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry("1200x600")
        self.title("Photo Editor")
        self.minsize(800, 500)
        self.initParameters()

        # Layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 2, uniform = "a")
        self.columnconfigure(1, weight = 6, uniform = "a")

        # Canvas data
        self.imageWidth = 0
        self.imageHeight = 0
        self.canvasWidth = 0
        self.canvasHeight = 0

        # Widgets
        self.image_Import = ImageImport(self, self.importImage)

        self.mainloop()

    # function that contains all of the parameters that is related to the image that is imported
    def initParameters(self):
        self.posVars = {
            "rotate": ctk.DoubleVar(value = rotateDefault),
            "zoom": ctk.DoubleVar(value = zoomDefault),
            "flip": ctk.StringVar(value = flipOption[0])}

        self.colourVars = {
            "brightness": ctk.DoubleVar(value = brightnessDefault),
            "grayScale": ctk.BooleanVar(value = grayScaleDefault),
            "invert": ctk.BooleanVar(value = invertDefault),
            "vibrance": ctk.DoubleVar(value = vibranceDefault)}
        
        self.effectVars = {
            "blur": ctk.DoubleVar(value = blurDefault),
            "contrast": ctk.IntVar(value = contrastDefault),
            "effect": ctk.StringVar(value = effectOption[0])}

        # tracing
        for variable in list(self.posVars.values()) + list(self.colourVars.values()) + list(self.effectVars.values()):
            variable.trace("w", self.manipulateImage)

    # function that manipulates the image
    def manipulateImage(self, *args):
        self.image = self.original

        # rotate
        if self.posVars["rotate"].get() != rotateDefault:
            self.image = self.image.rotate(self.posVars["rotate"].get())

        # zoom
        if self.posVars["zoom"].get() != zoomDefault:
            self.image = ImageOps.crop(image = self.image, border = self.posVars["zoom"].get())

        # flip
        if self.posVars["flip"].get() != flipOption[0]:
            if self.posVars["flip"].get() == "X":
                self.image = ImageOps.mirror(self.image) # flips the image on the horizontal axis

            elif self.posVars["flip"].get() == "Y":
                self.image = ImageOps.flip(self.image) # flips the image on the vertical axis

            elif self.posVars["flip"].get() == "Both":
                self.image = ImageOps.mirror(self.image)
                self.image = ImageOps.flip(self.image)

        # brightness & vibrance
        if self.colourVars["brightness"].get() != brightnessDefault:
            brightnessEnhancer = ImageEnhance.Brightness(self.image)
            self.image = brightnessEnhancer.enhance(self.colourVars["brightness"].get())

        if self.colourVars["vibrance"].get() != vibranceDefault:
            vibranceEnhancer = ImageEnhance.Color(self.image)
            self.image = vibranceEnhancer.enhance(self.colourVars["vibrance"].get())    

        # grayscale & invert
        if self.colourVars["grayScale"].get(): # only works if grayscale is set to True
            self.image = ImageOps.grayscale(self.image)

        if self.colourVars["invert"].get():
            self.image = ImageOps.invert(self.image)

        # blur & contrast
        if self.effectVars["blur"].get() != blurDefault:
            self.image = self.image.filter(ImageFilter.GaussianBlur(self.effectVars["blur"].get()))

        if self.effectVars["contrast"].get() != contrastDefault:
            self.image = self.image.filter(ImageFilter.UnsharpMask(self.effectVars["contrast"].get()))
        
        # effects drop down box
        match self.effectVars["effect"].get():
            case "Emboss": self.image = self.image.filter(ImageFilter.EMBOSS)
            case "Find Edges": self.image = self.image.filter(ImageFilter.FIND_EDGES)
            case "Contour": self.image = self.image.filter(ImageFilter.CONTOUR)
            case "Edge Enhance": self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)


        self.placeImage()

    # function for importing the image and placing it on the canvas
    def importImage(self, path):
        self.original = Image.open(path) # original copy of the image
        self.image = self.original
        self.imageRatio = self.image.size[0] / self.image.size[1]
        self.imageTK = ImageTk.PhotoImage(self.image)

        self.image_Import.grid_forget() # removes the import button
        self.imageOutput = ImageOutput(self, self.resizeImage)

        # calls the close button class 
        self.closeButton = CloseOutput(self, self.closeImage)

        # calls the side menu widget
        self.menu = Menu(self, self.posVars, self.colourVars, self.effectVars, self.exportImage)

    # function for resizing the image
    def resizeImage(self, event):
        # Current canvas ratio
        canvasRatio = event.width / event.height

        # update canvas attributes
        self.canvasWidth = event.width
        self.canvasHeight = event.height

        # Resize image
        if canvasRatio > self.imageRatio: # Canvas is wider than the image
            self.imageHeight = int(event.height)
            self.imageWidth = int(self.imageHeight * self.imageRatio)
        else: # Canvas is taller than the image
            self.imageWidth = int(event.width)
            self.imageHeight = int(self.imageWidth / self.imageRatio)

        self.placeImage()

    # function that places the image on the canvas
    def placeImage(self):
        # places the image on the canvas
        self.imageOutput.delete("all")
        resizedImage = self.image.resize((self.imageWidth, self.imageHeight))
        self.imageTK = ImageTk.PhotoImage(resizedImage)
        self.imageOutput.create_image(self.canvasWidth / 2, self.canvasHeight / 2, image = self.imageTK)

    # function for closing the image
    def closeImage(self):
        # hides the image + close button
        self.imageOutput.grid_forget()
        self.closeButton.place_forget()
        self.menu.grid_forget()

        # re-creates the import button
        self.image_Import = ImageImport(self, self.importImage)

    # function to save the image
    def exportImage(self, name, file, path):
        exportString = f"{path}/{name}.{file}"

        self.image.save(exportString)


Editor()