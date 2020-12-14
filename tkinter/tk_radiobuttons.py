from tkinter import *
from PIL import ImageTk, Image


root = Tk() #our widget
root.title('Radio Buttons!')
root.iconbitmap(r'C:\Users\Aristos\Desktop\Aristos\random_pics\pacman.ico')

#r = IntVar() #declare it, so it can be tracked.
#r.set('2') #initialize it

PIZZA_LIST = [
    ('Pizza 1', 'Pepperoni'),
    ('Pizza 2', 'Cheese'),
    ('Pizza 3', 'Mushrooms'),
    ('Pizza 4', 'Greek'),
]

pizza = StringVar() #track the variable of the radio buttons!
pizza.set("Pepperoni") #set the 1st.

#Creating all the radio button options with a loop is way cleaner.
for pizza_num, flavor in PIZZA_LIST:
    Radiobutton(root, text = pizza_num + ' : ' + flavor, variable = pizza, value = flavor).pack(anchor=W)

def clicked(value):
    myLabel1 = Label(root, text = value)
    myLabel1.pack()

myButton = Button(root, text = 'Click Me!', command = lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()