#!python 3 
import pprint

#lists are mutable datatypes! --> thats why we often turn the strings into lists, to easily manipulate them!
my_string = "heeeey"
my_list = list(my_string)

#when I assign a list to a variable I actually assign a list reference (to memory).
my_list = [0, 1, 2, 3, 4, 5]
cheese = my_list
cheese[1] = 'Hello' #If you print either cheese or spam you will get the same result since they have the same reference.

### list methods

spam = ['cat', 'dog', 'bat']
spam.index('dog') #returns the index of the element starting from 0.
spam.append('Hello') #always appends at the end of the list.
spam.insert(3,'chicken') #inserts chicken at index 1 and shifts all the others to the right! 
# insert doesn't remove the element of that index!!!
#or I can simply replace the value with
spam[0] = 'snake' #or multiple values
spam[1:3] = ['cat', 'dog']
#on the same note of adding elements I can combine 2 lists with
spam.extend(my_list) # spam's elements will go first! extend() also accepts tuples.

#to remove elements:
spam.remove('bat') # Thats cool because it allows you to specify a value to be removed.
# .remove will only remove the first instance of the specified element, not all of them!
# you can always delete by index:
spam.pop(2) #if not specified, pop() removes the last item. 
del spam[2] #does the same 
del spam #deletes the entire list!
spam.clear() #clear() removes all items from the list! The list remains, but has no content!

spam.sort()
spam.sort(reverse=True)
#sort only works with elements of the same datatype.
#sort(), sorts based on ASCII values, meaning that Capital letters come before lowercase for example
spam.sort(key=str.lower) #to sort in real alphabetical order.

### List comprehension
# The syntax is:
# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

### Expressions
# The expression is the current item in the iteration, but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]