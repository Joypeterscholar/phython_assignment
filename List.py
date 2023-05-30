# my_list = []
# name = ["sultan", "maraim", "victor", "joy"]
# print(name)
# students = [["sultan", 35, 200, 72], ["mariam", 24, 100, 99]]
# print(students[0])
# list2 = name + students
# print(students[::-1])
# name[0] = 56
# print(name)
# print(name[::-1])
#
# # numbers = []
# # for i in range(0, 51, 2):
# #     numbers.append(i)
# # print(numbers)
# #
# # even_number = list(range(0, 51, 2))
# # print(even_number)
# #
numbers = [1, 2, 3, 4, 5]
#print(len(numbers))
x = numbers[3]
y = numbers[1]
#print(x + y)
a, b, c, d, e = numbers #which is [1,2,3,4,5]
#print(f"the sum of the elements in the array is {a+b+c+d+e}")
x, y, *others = [1, 2, 3, 4, 5]
#print(x, y, others)
#print(x, others, y)
letters = list("hello c16")
print(letters)
for i in letters:
  print(letters)

for index, i in enumerate(letters):
 print(index, i)
lettera = ["a", "b", "c", "d", "e"]
letterb = list("abcde")
print(lettera)
print(letterb)
lettera.append("f")
print(lettera)
lettera.insert(0, "z")
print(lettera)
#prompt_engineering
lettera.remove("c")
print(lettera)
del lettera[0:2]  #to take out more than one element
print(lettera)
lettera.clear()
print(lettera)
