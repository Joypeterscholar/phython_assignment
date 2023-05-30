from hashlib import new
import random

roll1 = 0
roll2 = 0
roll3 = 0
roll4 = 0
roll5 = 0
roll6 = 0
for roll in range(600_000):
    outcome = random.randrange(1,7)
    if outcome == 1:
      roll1 += 1
    elif outcome == 2:
        roll2 += 1
    elif outcome == 3:
        roll3 += 1
    elif outcome == 4:
        roll4 += 1
    elif outcome == 5:
        roll5 += 1
    elif outcome == 6:
        roll6 += 1


print("Outcome\tRoll")
print(f"1\t{roll1}\n2\t{roll2}\n3\t{roll3}\n4\t{roll4}\n5\t{roll5}\n6\t{roll6}")






