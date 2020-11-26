#!python 3 
import pprint

print('what is your age?')
age = input() #input is a string value, thats why i can use it below without typecasting it
print("your age is " + age)
print('next year you will be ' + str(int(age) + 1) + \
	' years old') #notice how \ works as a line continuation!
if age != '': #since the input was a string i had to typecast it as an int, in order to perform arithmetic operations.
    print('YAY')
else:
    print('NOOOO')

#strings are immutable! (cannot be modified in place)

#lists are mutable datatypes! --> thats why i often turn the strings into lists.
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
#If you print either cheese or spam you will get the same result
# [0, 'Hello', 2, 3, 4, 5]

def listappend(list):
	list.append('Hello')

spam = ['1, 2, 3']
listappend(spam)
print(spam)
#changes made on a list inside a function will affect the 
#list outside the function as well!

#Dicts
my_dict = {'name': 'Aris', 'species': 'Human', 'age': '23'}
my_dict.get('age', 0)#return the age and if it doesnt exist return 0

message = 'It was a bright cold day in april'
count = {} #empty dict.

#counts how many times a character appears on the string.
for character in message.upper():
	count.setdefault(character, 0)
	count[character] = count[character] + 1
pprint.pprint(count) #pprint stands for prety print and prints the dict. values better!
