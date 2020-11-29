#! python3

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;\
Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"

#given that long string of names return them sorted by surname in
#the format (SURNAME, NAME) and if the surnames are the same, sort 
# them by name. 
#the final list should be 
#"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"


def meeting(s):
    names = s.upper().split(';')
    return ''.join(sorted('({1}, {0})'.format(*(n.split(':'))) for n in names))

###How it works:
#First of all I make the string uppercase and split it into a list of fullnames divided by ':'
#seperated by ':' This part could instantly be placed in the line below (to save a line :P)
#print(*any_list) line is passing all of the items in the list into the
#format function call as separate arguments.
#in this case n.split(':') returns ['FRED', 'CORWILL'], for the first iterrantion
#Thus, so far I 've gotten the '(SURNAME, NAME)' for every name in names.
#Then I sort the strings (returns a sorted list) and finaly I join the strings of the list 
#in a single string without spaces

#more elegantly:
def elegant_meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(n.split(':'))) for n in s.upper().split(';')))

###What I 've learned:
#1)The * in lists, that can be used to pass each element of the list into a function as an argument
#2)The "single line syntax" which is oftenly encountered in python. Instead of running a "for loop", 
#  I iterate it and pass each result into another function immediately 
#3)The use of the sorted() function. 
