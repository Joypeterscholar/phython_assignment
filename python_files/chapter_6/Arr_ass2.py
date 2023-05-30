def max_no():
  num = []
  total = 0
  for index in range(6):
    num1 = int(input("enter a number"))
    total = num1 + total
    num.append(num1)
  print(num)
  print('the maximum number of this list is', {max(num)})
max_no()


