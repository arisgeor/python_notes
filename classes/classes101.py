#! python

class Circle:
    """
    A simple class implementing a circle
    """

    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = (radius ** 2) * Circle.pi #inorder to use the Class Object Attribute, pi, i have to use the .pi syntax

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
print('\n')

#An example of Inheritance
"""
In this example, we have two classes: Animal and Dog. The Animal is the base class, the Dog is the derived class.

The derived class inherits the functionality of the base class.

It is shown by the eat() method.
The derived class modifies existing behavior of the base class.

shown by the whoAmI() method.
Finally, the derived class extends the functionality of the base class, by defining a new bark() method.
"""
class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.eat()
d.bark()