even_num = []
for number in range(21):
    if number % 2 == 0:
        even_num.append(number)

even_num2 = [i for i in range(21) if i % 2 == 0]  #list_comprehension
print(even_num)
print(even_num2)
even_num3 = [i for i in range(21) if i % 2 != 0]  #list_comprehension
print(even_num3)