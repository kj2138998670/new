import csv
import numpy as np
def main():
    Songs=open('songs.csv', mode='r')
    read_list=csv.reader(Songs)
    Songs_num=np.array(list(read_list)).shape[0]
    print("Songs To Learn 1.0 - by Haonan Wang\n",Songs_num,"songs loaded")

    Goagain = "L"
    while Goagain == "L":
        menu = input("Menu:""\nL - List songs""\nA - Add new song""\nC - Complete a song""\nQ - Quit").upper()
        Goagain = judgemenu(menu)
def judgemenu(menu):
    while menu != "L" and menu != "A" and menu != "C" and menu!= "Q":
        print("Please input the correct choice.")
        menu = input("Menu:""\nL - List songs""\nA - Add new song""\nC - Complete a song""\nQ - Quit").upper()
    if menu == "L":
        print()
        Goagain = "I"
    elif menu == "E":
        print("Welcome to use Tropical Airlines Ticket Ordering System,good bye!")
        exit()
    else:
        Goagain = "O"
    return Goagain











main()