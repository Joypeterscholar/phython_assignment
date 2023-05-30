# my_list = [2, 4, 5, 6]
# for i in range(len(my_list)):
#     my_list[i] += 3
#     print(i)


# my_list = [2, 4, 5, 6]
# for i in range(len(my_list)):
#     my_list[i] = my_list[i] ** 2
#     print(i)
#
# print(my_list)


#
# my_list = [2, 4, 5, 6]
# sum = 0
#
# for i in my_list:
#  sum += i
# print(sum)
# print(sum/len(my_list))
#
# num = [i for i in range(1, 11)]
# print(num)
# for i in range(len(num)):
#  if i >= 3 and i <= 5:
#   num[i] *= 2
# print(num)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(numbers)
# numbers2 = numbers[1::2]
# print(numbers2)
# # numbers[5:9] = [0,0,0,0, 0]
# new_num = [0] * 5
# numbers[5:9] = new_num
# print(numbers)
# print(numbers[0:5])
# numbers.clear()
# print(numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
del numbers[6:]
print(numbers)