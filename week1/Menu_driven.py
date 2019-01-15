choice = int(input("\n1.	Show the even numbers from x to y\n2.	Show the odd numbers from x to y\n3.	Show the squares from x to y\n4.	Exit the program"))
while choice!= 1 and choice != 2 and choice != 3 and choice != 4:
    print("Invalid choice")
    choice = int(input("\n1.	Show the even numbers from x to y\n2.	Show the odd numbers from x to y\n3.	Show the squares from x to y\n4.	Exit the program"))
while choice == 1 or choice == 2 or choice == 3 or choice == 4:
    if choice == 1:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        for i in range(x, y, 1):
            if i % 2 != 0:
                print(i, end=' ')
        choice = int(input("\n1.	Show the even numbers from x to y\n2.	Show the odd numbers from x to y\n3.	Show the squares from x to y\n4.	Exit the program"))
    elif choice == 2:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        for i in range(x, y, 1):
            if i % 2 == 0:
                print(i, end=' ')
        choice = int(input("\n1.	Show the even numbers from x to y\n2.	Show the odd numbers from x to y\n3.	Show the squares from x to y\n4.	Exit the program"))
    elif choice == 3:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        for i in range(x, y, 1):
            if i % 90 == 0:
                print(i, end=' ')
        choice = int(input("\n1.	Show the even numbers from x to y\n2.	Show the odd numbers from x to y\n3.	Show the squares from x to y\n4.	Exit the program"))
    elif choice == 4:
        break
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("Invalid choice")
        choice = int(input("\n1.	Show the even numbers from x to y\n2.	Show the odd numbers from x to y\n3.	Show the squares from x to y\n4.	Exit the program"))
print("Finished")