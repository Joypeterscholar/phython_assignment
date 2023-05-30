rate = 0.05
amount = input("enter amount")
years = input("enter number of years")
i = 0
try:
    while(i <= years):
      roi = amount * rate
      amount2: float = amount + roi
      amount = amount2
      i += 1
      print(f"in year  {i} return on investment is {roi} you will get {amount}")
except TypeError:
   print("alaye stop")

def interest(amount, years):
    rate = 0.05

    try:
        for year in range(1, years + 1):
         roi = amount * rate
         amount2: float = amount + roi
         amount = amount2
         print(f"in year  {year} return on investment is {roi} you will get {amount}")
         amount = input("enter amount")
         years = input("enter number of years")
    except TypeError:
        print("dont!")

interest(amount, years)