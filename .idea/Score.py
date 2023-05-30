score = int(input("Enter your score: "))
if score >= 80:
    print("A")
elif score >= 65 and score< 81:
    print("B")
elif score > 50 and score < 66:
    print("C")
elif score >= 40 and score < 51:
    print("D")
else:
 if score <= 40:
  print("F")