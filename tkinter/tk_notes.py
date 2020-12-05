#! python3

from tkinter import *

root = Tk() #our widget

#create a label widget and shove it into the screen 
myLabel1 = Label(root, text = 'Hello World!')
myLabel2 = Label(root, text ='My name is Aris Geor')
#myLabel1.pack() #the first most unsophisticated method to add stuff.

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1) #grid is static and doesn't move when resizing.

#Everything is a 2-step process where you create and then place on screen.
#However you can always type in a more pythonesque way. There is no good and bad.
#label 3 
Label(root, text = 'third label!').grid(row = 1, column = 2)

#I can create a fun just as in every python program.
def myClick():
    myLabel = Label(root, text = "I clicked!")
    myLabel.grid(row = 3, column = 3)

#Button (to execute a command) 
my_button = Button(root, text = 'Click Me!', padx = 30, pady = 20, command = myClick) #state = DISABLED, bg = 'red', fg = 'blue', etc. 
#there are many more methods to use. Also make sure you pass the func. as an arg. and not call it with () !
my_button.grid(row = 1, column = 4)

#entries
e = Entry(root, width = 50, borderwidth = 10)
e.grid(row = 4, column = 1)
e.insert(0,'Enter your name: ')                         #classic to give advice on the entry field.
#e.get()                                                #gets whatever i have typed inside the entry field

def myClick2():
    myLabel = Label(root, text = 'My name is ' + e.get())
    myLabel.grid(row = 5, column = 1)

my_button2 = Button(root, text = 'Click Me!', padx = 30, pady = 20, command = myClick2) 
my_button2.grid(row = 4, column = 2)

root.mainloop() #its a constant loop (thats how I can move my mouse while the window stays open)
