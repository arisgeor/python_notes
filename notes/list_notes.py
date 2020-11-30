#!python 3 
import pprint

print('what is your age?')
age = input() #input is a string value, thats why i can use it below without typecasting it
print("your age is " + age)
print('next year you will be ' + str(int(age) + 1) +  ' \
    years old') #i used the \ as an escape character to split the line
if age != '': #since the input was a string i had to typecast it as an int, in order to perform arithmetic operations.
    print('YAY')
else:
    print('NOOOO')

#strings are immutable! (cannot be modified in place)

#lists are mutable datatypes! --> thats why i often turn the strings into lists.
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello' #If you print either cheese or spam you will get the same result

#methods
spam = ['cat', 'dog', 'bat']
spam.index('dog')
spam.append('Hello')
spam.insert(1,'chicken') #inserts chicken at index 1 and shifts all the others to the right! 
# insert doesn't remove the element of that index!!!


def listappend(list):
	list.append('Hello')

spam = ['1, 2, 3']
listappend(spam)
print(spam)
#changes made on a list inside a function will affect the 
#list outside the function as well!