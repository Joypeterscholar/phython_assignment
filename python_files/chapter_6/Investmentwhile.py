rate = 0.05
amount = input("enter amount")
years = int(input("enter number of years"))
i = 0
while(i <= years):
        roi = amount * rate
        amount2: float = amount + roi
        amount = amount2
        i += 1
        print(f"in year  {i} return on investment is {roi} you will get {amount}")
