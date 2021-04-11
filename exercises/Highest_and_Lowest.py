#! python3 

def high_and_low(numbers):
    #lst = list(numbers)  #initial mistake... list() will also include the spaces!
    new = numbers.split(' ') #split gives me the elements without the spaces
    new = list(map(int, new)) #however it gives string elements and i need integers!
    a = int(max(new))
    b = int(min(new))
    return str(a) + " " + str(b)

#The reason i need to map the new list is because when i call max, min
#it will compare string values of the numbers and not int values. So i
#make the turn the list of strings into a list of integers and i 

#Best solution!
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
