import random;
def main():
    lotteries = [];
    while len(lotteries)<6:
        number=random.randint(1,46)
        if number not in lotteries:
            lotteries.append(number)
    lotteries.sort()
    print(lotteries)




main()


