def interest(amount, years):
    rate = 0.05
    for year in range(1, years + 1):
        roi = amount * rate
        amount2: float = amount + roi
        amount = amount2
        print(f"in year  {year} return on investment is {roi} you will get {amount}")
amount = int(input("enter amount"))
years = int(input("enter number of years"))
interest(amount, years)