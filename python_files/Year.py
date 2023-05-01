# x = int(input("enter amount in naira:#"))
# print(f" ${x//750}")
import datetime


def convert(yr):
    x = datetime.datetime.now()
    return x.year - yr
print(convert(1998))
