"""
CP1404/CP5632 Practical
"""
import os

def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for name in filenames:
            old_name = os.path.join(directory_name, name)
            new_name = os.path.join(directory_name, get_fixed_filename(name))
            os.rename(old_name, new_name)
            print(new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    word = []
    for i, letter in enumerate(filename):
        if letter.isupper():
            word.append("_{}".format(letter))
        else:
            word.append(letter)
    fixed = word[0].strip("_")
    word = [fixed] + word[1:]
    filename = "".join(word)
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt").replace("__", "_")
    return new_name


main()
