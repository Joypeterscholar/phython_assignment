num = [3, 4, 5, 6, 7, 8, 9, 9, 5]
for i in range(10):
    if num[i] == num[0]:
        num[i] = num[0]
print(num)
