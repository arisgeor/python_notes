#! python3

### map
# map() is a built-in Python function that takes in two or more arguments: a function and one or more iterables, in the form:
# map(function, iterable, ...)

def fahrenheit(celsius):
    return (9/5)*celsius + 32
    
temps = [0, 22.5, 40, 100]

F_temps = map(fahrenheit, temps)
list(F_temps)
#In the example above, map() applies the fahrenheit function to every item in temps. 

# However, we don't have to define our functions beforehand; we can use a lambda expression instead:
list(map(lambda x: (9/5)*x + 32, temps))

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
list(map(lambda x,y,z:x+y+z,a,b,c))

### filter
# The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, 
# for which the function returns True.
# Like map(), filter() returns an iterator
# for now, since our examples are so small, we will cast filter() as a list to see our results immediately.

#First let's make a function
def even_check(num):
    if num%2 ==0:
        return True

lst =range(20)

list(filter(even_check,lst))

# filter() is more commonly used with lambda functions, because we usually use filter 
# for a quick job where we don't want to write an entire function

list(filter(lambda x: x%2==0,lst))

### zip()
# zip() makes an iterator that aggregates elements from each of the iterables
# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
# zip() should only be used with unequal length inputs when you don’t care about trailing

x = [1,2,3]
y = [4,5,6]
# Zip the lists together
list(zip(x,y))

#zip is defined by the shortest iterable length!
x = [1,2,3]
y = [4,5,6,7,8]
# Zip the lists together
list(zip(x,y))

#What happens if we try to zip together dictionaries?
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

list(zip(d1,d2))
#The result makes sense because simply iterating through the dictionaries will result in just the keys

list(zip(d2,d1.values()))

