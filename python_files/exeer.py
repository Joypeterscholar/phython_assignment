name= 'hippopotamus'
print(name[::-1])
print(name[::-2])
print(name[::-3])
print(name[::1])
print(name[5::-1])
def multiply():
    return 3 * 10

print(multiply())

def multiply(a, b):
    return a * b

print(multiply(9,8))

def multiply(a:int, b:int) -> int:
    return a / b

print(multiply(9,2))