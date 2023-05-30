# from cmath import pi
#
# from python_files import Decimal
# from math import pi

class Circle:
    def __init__(self, r, pi):
        self.r = r
        self.pi = pi

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, number):
        if number < 0:
            raise ValueError("Radius cannot be negative")
        self.__r = number

    def area_of_a_circle(self):
        return f"the area of a circle is {self.pi * self.r ** 2}"

    def paremeter_of_a_circle(self):
        return f"the perimeter of the circle is {2 * self.r * self.pi}"

    def __str__(self):
        return f"{self.r} {self.pi}"


if __name__ == '__main__':
    circle1 = Circle(12.5, 5)
    print(circle1.area_of_a_circle())
    print(circle1.paremeter_of_a_circle())
