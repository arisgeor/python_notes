#! python3

message = "Call me at 415-555-1011 tomorrow, or 415-555-9999 for office"

import re #regular expressions
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #this holds the pattern we are looking for
#we need to use r for raw string because regular expressions have a lot of backslashes
mo = phoneNumRegex.search(message) #'search()' to print one instance.
#the .search() will return a match object. If i want to view it i ll need to group it first!
print(mo.group())

#i can use parenthesis inside the re to define groups (hence the .group() command before)
#if no groups are defined (like in the previous example), search will return the entire string inside .compile()
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #i made 2 goups
mo = phoneNumRegex.search(message)
print(mo.group(1)) #this yields 415
print(mo.group(2)) #this yields 555-1011
#since parenthesis are used to identify groups, in the case i m looking for an actuall parenthesis 
#i ll need to escape it with a backslash \( .

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #the pipe | can match one of many possible groups!
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# ? (0 or 1) (optional character)
batRegex2 = re.compile(r'Bat(wo)?man') #the ()? means this can appear 0-1 time(s). If there were was than one
#appearance of wo, then mo == None
mo = batRegex2.search('The adventures of Batman')
print(mo.group())

#similarly
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') #i made the first 3 digits optional
mo = phoneNumRegex.search('Call me at 415-555-1011 tomorrow')
print(mo.group())
mo = phoneNumRegex.search('or 555-9999 for office')
print(mo.group())
#i can always search for an actual question mark using the escape character \?

# * ( 0 or more)
batRegex3 = re.compile(r'Bat(wo)*man') #The * indicates 0 or more times
mo = batRegex3.search('The adventures of Batman')
print(mo.group())
mo = batRegex3.search('The adventures of Batwowowowowoman')
print(mo.group())

# + (1 or more)
batRegex4 = re.compile(r'Bat(wo)+man') #The + indicates 1 or more times
try:
	mo = batRegex4.search('The adventures of Batman') #this yields None so i dont want the program to crash here :P 
	print(mo.group())
except:
	print('No appearance of "wo" at all')
mo = batRegex4.search('The adventures of Batwowowowowoman')
print(mo.group())

# {} (exact number)
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said HaHaHa')
print(mo.group())

#greedy and non-greedy
digitRegex = re.compile(r'(\d){3,5}') #greedy
mo = digitRegex.search('1234567890')
print(mo.group()) #yields 12345
digitRegex = re.compile(r'(\d){3,5}?') #non-greedy with the optional ?
mo = digitRegex.search('1234567890')
print(mo.group()) #yields 123

##############

message = "Call me at 415-555-1011 tomorrow, or 415-555-9999 for office"
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message)) #i can use 'findall()' to print all instances of the re.
#findall() returns a list so i can instantly print it.
#that works fine as long as there is 0 or 1 groups in regular expression
#if there are more (2 or more)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #2 groups here
phoneNumRegex.findall(message) #this will return a list of tuple of strings, not a list of strings

#############

# \d is any numeric digit
# \D is any character that is NOT a numeric digit
# \w any letter, digit or underscore (w for word)(capital is the opposite)
# \s any space tab or newline (capital is the opposite)

#I can create my own character classes with []!
vowelRegex = re.compile(r'[aeiouAEIOU]')# will search for all the vowels
vowelRegex.findall('Robocop eats baby food')
#and i can also create NEGATIVE character classes with ^ (caret)
vowelRegex = re.compile(r'[^aeiouAEIOU]') #returns all consonants 
vowelRegex.findall('Robocop eats baby food')

#with the caret ^ i can also indicate that the r.e. must start with whatever follows
beginsWithHelloRegex = re.compile(r'^Hello') #not only am i looking for Hello, it has to begin with it
beginsWithHelloRegex.search('Hello there!') #--> this yields Hello!
#similarly with $ i achieve the opposite!
endsWithWorldRegex = re.compile(r'world!$')
endsWithWorldRegex.search('Hello world!')
#that means that if i Use both of them i can specify the entire text!
allDigitsRegex = re.compile(r'^\d+$') #starts with digit, ends with digit and anything in between is a digit!
allDigitsRegex.search('23424242535464564')

# . any character (except new line!)
atRegex = re.compile(r'.at') #this will return anything ending in 'at'
atRegex.findall('The cat in the hat sat on the flat mat')

# .* ( . == any character at all, * == 0 or more ) so that reads " zero or more of anything!"
#so .* means anything! anythig at all!

name = "First name: Aris Last name: Georgoulas"
nameRegex = re.compile(r'First name: (.*) Last name: (.*)') #so i have defined the pattern and the 2 groups i am looking for!
nameRegex.findall(name)

# remember .* is greedy
#          .*? is not greedy

#if i want "." to mean anything including new lines i can do
dotStar = re.compile(r'.*', re.DOTALL)
#similarly i can make the search case Insensitive with re.I
vowelRegex = re.compile(r'[aeiou]', re.I)


############ 
#sub() method
message = 'Agent Alice gave the secrets to Agent Bob.'
namesRegex = re.compile(r'Agent \w+')
namesRegex.findall(message)
namesRegex.sub('REDACTED', message)

namesRegex = re.compile(r'Agent (\w)\w*')
namesRegex.findall(message)
namesRegex.sub(r'Agent \1****', message) # \1 refers to the first groups (and i use raw strings because i have a backslash \)

###### Verbose mode to read (easily) and add docummentation in a realy complicated r.e.!
re.compile(r'''
	\d\d\d 		# area code
	-			# first dash
	\d\d\d\d 	#first 3 digits
	-			#second dash
	\d\d\d\d''', re.VERBOSE) #so we can add comments by line, which makes the code alot better!
# i can also add more with the pipe | character as such --> re.DOTALL | re.VERBOSE)
# note that this kind of syntax is only used in "re.compile" function (its not a python thing)
