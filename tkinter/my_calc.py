#! python3

from tkinter import *

root = Tk() #our widget

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan = 3, padx = 10, pady = 10) #columnspan is exactly what it means. 
#e.insert(0, '')

#buttons

def button_click(number):
    #e.delete(0, END) #if i delete the value then i ll never be able to type a number like 108 for example. Also if i want to type 108 it will print 801
    current = e.get() #that's why I will first get the value inside the box and concatinate it with the next value. 
    e.insert(0, str(current) + str(number)) #to add the 'current' with the number you click, you need to make sure there are strings! otherwise it will add the numeric values.
    pass 

#instead of passing a command parameter, I actually want to call it with a specific argument to each button, thats why i use lambda without any arguments! 
Button(root,text='7', padx=40, pady=20, command=lambda: button_click(7)).grid(row = 1, column = 0)
Button(root,text='8', padx=40, pady=20, command=lambda: button_click(8)).grid(row = 1, column = 1)
Button(root,text='9', padx=40, pady=20, command=lambda: button_click(9)).grid(row = 1, column = 2)

Button(root,text='4', padx=40, pady=20, command=lambda: button_click(4)).grid(row = 2, column = 0)
Button(root,text='5', padx=40, pady=20, command=lambda: button_click(5)).grid(row = 2, column = 1)
Button(root,text='6', padx=40, pady=20, command=lambda: button_click(6)).grid(row = 2, column = 2)

Button(root,text='1', padx=40, pady=20, command=lambda: button_click(1)).grid(row = 3, column = 0)
Button(root,text='2', padx=40, pady=20, command=lambda: button_click(2)).grid(row = 3, column = 1)
Button(root,text='3', padx=40, pady=20, command=lambda: button_click(3)).grid(row = 3, column = 2)

Button(root,text='0', padx=40, pady=20, command=lambda: button_click(0)).grid(row = 4, column = 0)
Button(root,text='Clear', padx=79, pady=20, command=lambda: button_click(7)).grid(row = 4, column = 1, columnspan = 2)

Button(root,text='+', padx=39, pady=20, command=lambda: button_click(7)).grid(row = 5, column = 0)
Button(root,text='=', padx=91, pady=20, command=lambda: button_click(7)).grid(row = 5, column = 1, columnspan = 2)


def myClick():
    myLabel = Label(root, text = "I clicked!")
    myLabel.grid(row = 3, column = 3)


root.mainloop() #constant loop