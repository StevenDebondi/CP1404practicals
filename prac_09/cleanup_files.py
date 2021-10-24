"""
CP1404/CP5632 Practical
Cleanup Files
"""
import shutil
import os, os.path


def main():
    """Clean up files to be consistent naming"""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            name_name = os.path.join(directory_name, filename)
            print(name_name)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(name_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    spaced_name = filename.split(" ")
    print(spaced_name)
    new_name = "_".join(spaced_name)
    return new_name


main()
