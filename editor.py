import customtkinter as ctk
from imageWidgets import *
from menu import Menu
from PIL import Image, ImageTk, ImageOps

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
        self.rotateFloat = ctk.DoubleVar(value = rotateDefault)
        self.zoomFloat = ctk.DoubleVar(value = zoomDefault)

        self.rotateFloat.trace("w", self.manipulateImage)
        self.zoomFloat.trace("w", self.manipulateImage)

    # function that manipulates the image
    def manipulateImage(self, *args):
        self.image = self.original

        # rotate
        self.image = self.image.rotate(self.rotateFloat.get())

        # zoom
        self.image = ImageOps.crop(image = self.image, border = self.zoomFloat.get())

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
        self.menu = Menu(self, self.rotateFloat, self.zoomFloat)

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

Editor()