def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month_num in range(1, months + 1):
        income = float(input("Enter income for month_num " + "{:.0f}".format(month_num) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month_num in range(1, months + 1):
        income = incomes[month_num - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month_num, income, total))


main()