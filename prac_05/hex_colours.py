COLOURS = {"aquamarine1": "#7fffd4", "chartreuse1": "#7fff00", "DarkOrchid": "#9932cc", "DeepPink1": "#ff1493",
           "GhostWhite": "#f8f8ff", "gold1": "#ffd700", "gray1": "#030303", "khaki": "#f0e68c", "lavender": "#e6e6fa",
           "LimeGreen": "#32cd32", "magenta": "#ff00ff"}

colour_code = input("What is the colour? ")
while colour_code != "":
    if colour_code in COLOURS:
        print("{} hex code is {}".format(colour_code, COLOURS[colour_code]))
    else:
        print("That colour is not here.")
    colour_code = input("What is the colour? ")


