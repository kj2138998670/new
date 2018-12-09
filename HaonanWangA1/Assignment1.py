import csv
import pandas as pd



def main():
    Songs = pd.read_csv('songs.csv')
    print("Songs To Learn 1.0 - by Haonan Wang\n", len(Songs.index), "songs loaded")

    Goagain = "L" or "A" or "C"
    while Goagain == "L" or Goagain=="A" or Goagain=="C":
        Songs= pd.read_csv('songs.csv')
        menu = input("L - List songs""\nA - Add new song""\nC - Complete a song""\nQ - Quit").upper()
        Goagain = judgemenu(menu,Songs)







def judgemenu(menu,Songs):
    while menu != "L" and menu != "A" and menu != "C" and menu!="Q":
        print("Please input the correct choice.")
        menu = input("L - List songs""\nA - Add new song""\nC - Complete a song""\nQ - Quit").upper()
    if menu == "L":
        Learned = Songs.pop('Learned')
        Songs.insert(0, 'Learned', Learned)
        Songs_list=Songs.replace(['y', 'n'], ['*', ' '])
        print(Songs_list,'\n',len(Songs_list[Songs_list['Learned']==' ']),' songs learned',len(Songs_list[Songs_list['Learned']=='*']),' song still to learn')
        Goagain = "L"
    elif menu == "Q":
        print(len(Songs.index), "songs saved to songs.csv\nHave anice day :)")
        exit()
    elif menu== "A":
        title = input("Title: ")
        while title == "":
            title = input("Input can not be blank\nTitle: ")
        artist = input("Artist: ")
        while artist == "":
            artist = input("Input can not be blank\nArtist: ")
        loop=3
        while loop==3:
            year = input("Year: ")
            if year.isalpha():
                print("Invalid input; enter a valid number")
                loop=3
            elif int(year) <= 0:
                print("Number must be >= 0")
                loop=3
            else:
                loop=4
            Learned = "y"
            New_song = [title, artist, year, Learned]
            Songs_csv = open("songs.csv", "a", newline="")
            writer = csv.writer(Songs_csv)
            writer.writerow(New_song)
            Songs_csv.close()
            print(title, "by", artist, "(", year, ") added to song list")
        Goagain = "A"
    else:
        Songs = pd.read_csv('songs.csv')
        if "y" in list(Songs["Learned"]):
            Wrong = 1
            while Wrong == 1:
                Songs_Number=input("Enter the number of a song to mark as learned")
                if Songs_Number.isalpha():
                    print("Invalid input; enter a valid number")
                    Wrong=1
                elif int(Songs_Number) < 0:
                    print("Number must be > 0")
                    Wrong=1
                elif int(Songs_Number) > len(Songs)-1:
                    print("Invalid song number")
                    Wrong=1
                else:
                    Wrong=2

            if Songs.iat[int(Songs_Number), 3]!="y":
                print("You have already learned",Songs.iat[int(Songs_Number),0])

            else:
                Songs.iat[int(Songs_Number), 3]="n"
                Songs.to_csv("songs.csv", index=False)
                print(Songs.iat[int(Songs_Number), 0],"by",Songs.iat[int(Songs_Number), 1],"learned")

        else:
            print("No more songs to learn!")
        Goagain="C"
    return Goagain






main()