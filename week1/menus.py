name = str(input("Enter name:"))
menu = input("Invalid choice""\n(H)ello""\n(G)oodbye""\n(Q)uit").upper()
while menu!="H" and menu!="G" and menu!="Q":
    menu = input("Invalid choice""\n(H)ello""\n(G)oodbye""\n(Q)uit").upper()
if menu="H":
    print("Hello ",name)
    menu = input("Invalid choice""\n(H)ello""\n(G)oodbye""\n(Q)uit").upper()
elif menu="G":
    print("Goodbye "name)