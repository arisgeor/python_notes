#! python

class Circle:
    """
    A simple class implementing a circle
    """
    #the avove lines starting with triple quotes, are called a docstring. 
    #docstrigs contain usufull info about the class or function and act as documentantion
    #Type help(Circle) to return the docstring

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
    #The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, name = 'doggo'): 
        #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        Animal.__init__(self) # super().__init__() super doesnt need the self, only the arguments.
        self.name = name
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

    def speak(self):
        return self.name + ' says Woof' # this method is used in the next example


d = Dog()
d.eat()
d.bark()
print('\n')

### Polymorphism
#In Python, polymorphism refers to the way in which different object classes can share the same method name, 
#and those methods can be called from the same place even though a variety of different objects might be passed in. 
#The best way to explain this is by example:

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    

niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())
print('\n')

for pet in [niko,felix]:
    print(pet.speak())

print('\n')

#Special Methods
#Classes in Python can implement certain operations with special method names. 
#These methods are not actually called directly but by Python specific language syntax. For example:

class Book:

    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Arisgeor", 169)

#Special Methods
print(book)
print(len(book))
del book

