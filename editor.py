import customtkinter as ctk
from imageWidgets import *
from PIL import Image, ImageTk

# main class that contains the main window.
class Editor(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry("1000x600")
        self.title("Photo Editor")
        self.minsize(800, 500)

        # Layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 2)
        self.columnconfigure(1, weight = 6)

        # Widgets
        self.image_Import = ImageImport(self, self.importImage)

        self.mainloop()

    # function for importing the image and placing it on the canvas
    def importImage(self, path):
        self.image = Image.open(path)
        self.imageRatio = self.image.size[0] / self.image.size[1]
        self.imageTK = ImageTk.PhotoImage(self.image)

        self.image_Import.grid_forget() # removes the import button
        self.imageOutput = ImageOutput(self, self.resizeImage)

        # calls the close button class 
        self.closeButton = CloseOutput(self, self.closeImage)


    # function for resizing the image
    def resizeImage(self, event):
        # Current canvas ratio
        canvasRatio = event.width / event.height

        # Resize image
        if canvasRatio > self.imageRatio: # Canvas is wider than the image
            imageHeight = int(event.height)
            imageWidth = int(imageHeight * self.imageRatio)
        else: # Canvas is taller than the image
            imageWidth = int(event.width)
            imageHeight = int(imageWidth / self.imageRatio)
        

        # places the image on the canvas
        self.imageOutput.delete("all")
        resizedImage = self.image.resize((imageWidth, imageHeight))
        self.imageTK = ImageTk.PhotoImage(resizedImage)
        self.imageOutput.create_image(event.width / 2, event.height / 2, image = self.imageTK)

    # function for closing the image
    def closeImage(self):
        # hides the image + close button
        self.imageOutput.grid_forget()
        self.closeButton.place_forget()

        # re-creates the import button
        self.image_Import = ImageImport(self, self.importImage)
Editor()