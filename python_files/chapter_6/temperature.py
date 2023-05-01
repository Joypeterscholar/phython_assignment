celsius = int(input("Enter a temperature in degrees Celsius: "))


def convert_far_cel(far):
    c = (far - 32) * 5 / 9
    return c


print(f"{celsius} C = {convert_far_cel(celsius):.2f}")

fahrenheit = int(input("Enter a temperature in degrees Fahrenheit: "))


def convert_cel_far(cel):
    f = cel * 9 / 5 + 32
    return f


print(f"{fahrenheit} F = {convert_cel_far(fahrenheit):.2f} C")
