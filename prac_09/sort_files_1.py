"""
CP1404/CP5632 Practical
Sorting Files Version 1
"""
import os
import shutil


def main():
    """Create folders based on extensions and move files into folders based on their extensions"""
    os.chdir('FilesToSort')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    for filename in os.listdir('.'):
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(filename, "{}/{}".format(extension, filename))


main()
