__author__ = 'Ciaran'

def simple_interest(principle, rate, periods):
    return principle + (principle * rate * periods)

def compoundInterest(principle, rate, periods, n):
    return principle * ((1 + rate/n)**(n*periods))

def diffbetween_month_year(principle, rate, periods):
    yearly = principle * ((1 + rate/1)**(1*periods))
    monthly = principle * ((1 + rate/12)**(12*periods))
    return monthly - yearly

def main():
    principle = float(input("Enter original amount: "))
    interestRate = (float(input("Enter interest rate: "))/100)
    numberYears = int(input("Enter number of years: "))
    compundPeriods = float(input("Enter number of compounding periods: "))

    #newBankBal = simple_interest(principle, interestRate, numberYears)
    #print(newBankBal)

    compound = compoundInterest(principle, interestRate, numberYears, compundPeriods)
    print(round(compound, 2))

    #difference = diffbetween_month_year(principle, interestRate, numberYears)
    #print("Compound interest calculated monthly is ", round(difference, 2), "more than when calculated yearly")


    print(principle, "at", (interestRate * 100), "%", "compounded quarterly for", numberYears, "years yields",
          round(compoundInterest(principle, interestRate, numberYears, compundPeriods), 2))

    total = principle
    for x in range(1, numberYears*4 + 1):
        total += principle * (interestRate/compundPeriods)
        print("Quarter: ", x, "Balance: ", total)



main()