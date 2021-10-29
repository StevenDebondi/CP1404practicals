"""
CP1404/CP5632 Practical
Cleanup Files

Unfinished program, was able to fix the spaces into underscores but I'm not sure how to fix it for the others.
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
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(name_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    spaced_name = filename.split(" ")
    new_name = "_".join(spaced_name).title()

    for i, character in enumerate(filename):
        new_name = ""
        print(i, character)
        if character.islower():
             character.isupper()

    return new_name


main()
