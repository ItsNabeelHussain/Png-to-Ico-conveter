
""" Pillow or PIL is a python image 
processing library that provides extensive 
file format support an efficient internal 
representation, and fairly powerful image
processing capabilities.it is fork from 
Python Imaging Library(PIL)
"""
import os

from PIL import Image


def png_to_ico_converter():
    """
    fucntion for converting png format 
    to ico format.It takes file from the 
    user,convert it into ico and return 
    icon  file 
    """

    image_file = input("Choose image file from the directory")
    if os.path.isfile(image_file):
        file = Image.open(image_file)
        icon_file = file.save('file.ico')
        print("Successfully converted into required format")
        
    else:
        print("Invalid File path")
 if __name__ == "__main__":
    png_to_ico_converter()
