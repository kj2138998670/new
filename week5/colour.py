COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0"}
colour = input("Enter a colour: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    elif colour=="ALL":
        for key in COLOUR_NAMES:
            print(key,"is", str(COLOUR_NAMES[key]))
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ")
