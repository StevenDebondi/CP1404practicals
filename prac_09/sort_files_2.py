"""
CP1404/CP5632 Practical
Sorting Files Version 2
"""
import os
import shutil


def main():
    """Move files into a folder based on user inputs"""
    extensions = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        extension = filename.split('.')[-1]
        if extension not in extensions:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extensions[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(filename, "{}/{}".format(extensions[extension], filename))


main()
