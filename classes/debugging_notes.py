#! python3

### raise Exception('This is the error message')
#The message og the Exception is called a traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width<2) or (height<2):
        raise Exception('"width" and "height" must be greateror equal to 2')
    print(symbol * width)

    for _ in range(height - 2):  #when the variable is not used later, its best to use '_' instead of 'i', since it wont raise a warning!
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)
    

boxPrint('*', 15, 5)
boxPrint('**', 15, 5) #this will trigger the first exception

#traceback.format_exc()
import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback indo was written in error_log.txt')

#Assert 
#these are used for programming errors, not user errors
assert False, 'This is the error message' #--> this will always type the message

#generally assertions are used to check whether a simple yet not obvious condition is true in our program

### logging
#these are the two de-facto lines i place at the beginning of the file
import logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) #i ll explain this line later

#example of error caught with logging.

logging.debug('Start of the program')

def factorial(n):
    logging.debug('Start of factorial (%s)' %(n))
    total = 1
    for i in range(n+1): #here is where the error happens, since i begins from 0
        total *= i       #so total becomes 0 on the first iteration
        logging.debug('i is %s, total is %s!' %(i, total))

    logging.debug('Return value is %s' %(total))
    return total

print(factorial(5))
logging.debug('End of the program')

#now that i' ve included logging messages, these will be displayed even if the program runs smoothly
# to disable them i ll use the command from the beginning: logging.disable(logging.CRITICAL) which disables 
# all logging messages from CRITICAL and below (meaning all of them)

#there are 5 Log Levels: debug(lowest), info, warning, error, critical(highest)

#if i wanna write all those logging messages to a file i just have to add the "filename" to the command:
logging.basicConfig(filename = 'myProgrammingLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
