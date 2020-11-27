#! python3

### Decorators
#Decorators can be thought of as functions which modify
#the functionality of another function. They help to make 
#your code shorter and more "Pythonic".

def func():
    return 1

#We can check for local variables and global variables 
#with the locals() and globals() functions. For example:
s = 'Global Variable'

def check_for_locals():
    print(locals())

    
print(globals()) #returns a dict with lots of info
print(globals().keys())
globals()['s'] # --> returns the "Global Variable" text from s"

check_for_locals() #doesn't return anything

#Remember that in Python everything is an object. That means functions 
#are objects which can be assigned labels and passed into other functions.

def hello(name='Aris'):
    return 'Hello '+ name
greet = hello
greet # Returns <function hello at 0x000002CB35294AF0>
greet()

del hello
greet()

#Even though we deleted the name hello, the name greet still points to our 
#original function object. It is important to know that functions are objects 
#that can be passed to other objects!

### Functions as arguments

def hello():
    return 'Hi Jose!'

def other(func):  #notice how the func is passed as an argument (without())
    print('Other code would go here')
    print(func()) #here it gets executed with ()
#technicaly we creted a decorator!

other(hello)

#Creating a Decorator

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

#So what just happened here? A decorator simply wrapped the function and 
#modified its behavior. Now let's understand how we can rewrite this code 
#using the @ symbol, which is what Python uses for Decorators:

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

#Decorators are oftenly used in Web Development, in frameworks such as Flask or Django! 