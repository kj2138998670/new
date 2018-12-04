def main():
    numbers=[]
    for time in [1,2,3,4,5]:
        number = float(input("Enter number " + str(time) + ": "))
        numbers.append(number)

    print("the largest number is",max(numbers),"\nthe minimum number ",min(numbers))












main()