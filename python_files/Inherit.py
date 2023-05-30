class Animal:
    def eat(self):
        print("Eating....")

class Mammal(Animal):
    def move(self):
        print("Moving....")

class Fish(Animal):
    def swim(self):
        print("Swimming...")


JOY =Mammal
JOY.eat('fish')

#from inheritance_ import Animal- to import a subclass