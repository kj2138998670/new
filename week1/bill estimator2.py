ARIFF_11 = 0.244618
TARIFF_31 = 0.136928
def main():
    print("Electricity bill estimator 2")
    Taiff=input("Which tariff? 11 or 31")
    if Taiff==11:
        taiff=TARIFF_11
    else:
        taiff=TARIFF_31
    daily=float(input("Enter daily use in kWh: "))
    days=float(input("Enter number of billing days: "))

    total=(taiff*daily*days)
    print("Estimated bill: $","%.2f"%total)
main()