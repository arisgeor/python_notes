#! python3 

#I want to run it from the command line directly so I 'll create a batch file too.
import sys, webbrowser, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.'] 
# we want all the system arguments after the first one which is the executable

#check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#thankfully google is smart enough to figure it out.
#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)

