#! python3
import pprint

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
