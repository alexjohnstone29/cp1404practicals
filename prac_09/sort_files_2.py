import os


def main():
    extension_type = {}
    os.chdir("FilesToSort")
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue
        extension = os.path.splitext(filename)[1]
        if extension not in extension_type:
            new_directory = input("What category would you like to sort {} files into? ".format(extension))
            extension_type[extension] = new_directory
            try:
                os.mkdir(new_directory)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(extension_type[extension], filename))


main()
