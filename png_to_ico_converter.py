
""" Pillow or PIL is a python image
processing library that provides extensive
file format support an efficient internal
representation, and fairly powerful image
processing capabilities.it is fork from
Python Imaging Library(PIL)

"""
import os

from PIL import Image


def png_to_ico_converter(image_file) -> None:
    """
    fucntion for converting png format
    to ico format.It takes file from the
    user,convert it into ico and return
    icon  file
    """

    try:
        # Check the existing of the File
        if os.path.isfile(image_file):
         # Open the image file using Image class instance of the Pillow library
            file = Image.open(image_file)
            # Resizing the image
            new_image = file.resize((400, 400))
            # Saving image file in ICO format
            new_image.save('icon_file.ico')
            print("Successfully converted into required Format")
        else:
            print("Please select correct directory")

    except FileNotFoundError:
        print("image file does not exists")


if __name__ == "__main__":
    print("**** Welcome to the Png to Icon Converter ****")
    image_path = input("Choose image file from the directory: ")

    png_to_ico_converter(image_path)
