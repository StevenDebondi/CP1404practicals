"""
CP1404/CP5632 Practical
Hex Colours Program
"""


HEX_COLOURS = {"blueviolet": "#8a2be2", "cadetblue": "#5f9ea0", "hotpink": "#ff69b4", "lavender": "	#e6e6fa",
               "lawngreen": "#7cfc00", "mediumvioletred": "#c71585", "red4": "#8b0000", "salmon": "#fa8072",
               "yellow1": "#ffff00", "white": "#ffffff"}

colour = input("Enter a colour name: ").lower()
while colour != "":
    if colour in HEX_COLOURS:
        print("The hex code for {} is {}".format(colour, HEX_COLOURS[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter a colour name: ").lower()
