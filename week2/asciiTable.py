def get_number(lower, upper):
    number = int(input("Enter a number(10-50):\n>>>"))
    while number < 10 or number > 50:
        print("Please enter a valid number")
        number = int(input(">>>"))



def get_Input_character():
    Input_character = input(format("Enter a character:"))
    return Input_character

def get_num():
    lower = 33
    upper = 127
    num = input(format("Enter a number({} - {}):".format(lower,upper)))
    return num

def main():
    Input_character = get_Input_character()
    num = get_num()
    print("The ASCII code for", Input_character, "is", ord(Input_character))
    num2 = chr(int((num)))
    print("\tThe character for", num, "is", num2)
main()