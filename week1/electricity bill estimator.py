print("Electricity bill estimator")
cents=float(input("Enter cents per kWh: "))
daily=float(input("Enter daily use in kWh: "))
days=float(input("Enter number of billing days: "))

total=(cents*daily*days)/100
print("Estimated bill: $",total)