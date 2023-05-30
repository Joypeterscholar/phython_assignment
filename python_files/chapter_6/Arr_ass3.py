def max_no():
  num = []
  total = 0
  for index in range(6):
    num1 = int(input("enter a number"))
    total = num1 + total
    num.append(num1)
  print(total)

  print(f'the sum of a number in {num} is, {total}')
max_no()


