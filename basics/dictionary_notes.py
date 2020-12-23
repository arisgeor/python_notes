#! python3
import pprint

###Dicts

my_dict = {                    
	'name': 'Aris', 
	'species': 'Human',  #its much prettier to write it this way! just don't forget the ','
	'age': 22,
	'nationality': 'Greek'
	}
my_dict['name'] #will return 'Aris' and is the same as
my_dict.get('name') #this looks a bit more elegant.
my_dict.get('age', 0)#return the age and if it doesnt exist return 0

x = my_dict.keys() #returns all the keys!
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
#similarly:
my_dict.values() #returns all the values!
my_dict.items() #returns all items as tuples in a list.
#You can always check if an item is in a dict by:
if "name" in my_dict:
  print("Yes, 'name' is one of the keys in the \'my_dict\' dictionary")

# to change/create a key-value:
my_dict['name'] = 'Aristos' #I can use this to update a key-value pair.
my_dict.update({"age": 23}) #this looks a bit more elegant.
#these commands will create the key-value pair if it doesn't exist.

#to delete a key-value:
my_dict.pop('age')
my_dict.popitem() #will delete the last item of the dict.
#alternatively:
del my_dict['age'] #The del keyword can also delete a dictionary completely:
del my_dict
my_dict.clear() #completely clears a dictionary.

#to loop a dict:
for x in my_dict:
	print(x) #print the keys
	print(my_dict[x]) #print the values

#I can also loop through they keys or values or both
for x in my_dict.keys():
  print(x)
for x in my_dict.values():
	print(x)
for x, y in my_dict.items():
  print(x, y)

#copy
new_dict = my_dict.copy()

#I can combine 2 lists into a dict!
x = ('key1', 'key2', 'key3')
y = 0 
thisdict = dict.fromkeys(x, y) #y is optional. Default value is None
print(thisdict)

#the setdefault() method
my_dict.setdefault('name', "None") #this returns 'Aris'
my_dict.setdefault('Gender', "Male") #If the key does not exist, insert the key, with the specified value

message = 'It was a bright cold day in april'
count = {} #empty dict.

#counts how many times a character appears on the string!
for character in message.upper():
	count.setdefault(character, 0)
	count[character] += 1
pprint.pprint(count) #pprint stands for prety print and prints the dict. values better!
