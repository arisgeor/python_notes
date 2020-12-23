#! python3 

### Iterators and Generators

#Generators allow us to generate as we go along, 
#instead of holding everything in memory.

# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)
#since we have a generator function we don't have to 
#keep track of every single cube we created.



#example generator which calculates fibonacci numbers:
def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)

#as a normal function, this would look like:
def fibon(n):
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
        
    return output

fibon(10)