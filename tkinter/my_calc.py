#! python3

from tkinter import *

root = Tk() #our widget

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan = 3, padx = 10, pady = 10) #columnspan is exactly what it means. 
#e.insert(0, '')

###functions.

def button_click(number):
    #e.delete(0, END) #if i delete the value then i ll never be able to type a number like 108 for example. Also if i want to type 108 it will print 801
    current = e.get() #that's why I will first get the value inside the box and concatinate it with the next value. So after I get the first value:
    e.delete(0,END)
    e.insert(0, str(current) + str(number)) #to add the 'current' with the number you click, you need to make sure there are strings! otherwise it will add the numeric values.
    
def button_clear():
    e.delete(0,END)

def button_add():
    first_num = e.get()
    global f_num
    global math 
    f_num = int(first_num) #now first_number became a global var, and can be used outside of the function.
    math = 'addition'      #same for the math flag
    e.delete(0, END)

def button_subtract():
    first_num = e.get()
    global f_num
    global math 
    f_num = int(first_num) 
    math = 'subtraction'
    e.delete(0, END)

def button_multiply():
    first_num = e.get()
    global f_num
    global math 
    f_num = int(first_num) 
    math = 'multiplication'
    e.delete(0, END)

def button_divide():
    first_num = e.get()
    global f_num
    global math 
    f_num = int(first_num) 
    math = 'division'
    e.delete(0, END) 

#equal needs to know the previous number entered as well as the previous operation! That's why I used global variables.
def button_equal(): 
    second_number = e.get() #get whatever number was the input before you hit "="
    e.delete(0,END)
    if math == 'addition':
        e.insert(0, f_num+int(second_number)) #and then insert the new result
    elif math == 'subtraction':
        e.insert(0, f_num-int(second_number))
    elif math == 'multiplication':
        e.insert(0, f_num*int(second_number))
    elif math == 'division':
        e.insert(0, f_num/int(second_number))

###Buttons

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

Button(root,text='Clear', padx=79, pady=20, command=button_clear).grid(row = 4, column = 1, columnspan = 2) #ofc here I dont need lambda.
Button(root,text='+', padx=39, pady=20, command=button_add).grid(row = 5, column = 0)
Button(root,text='=', padx=91, pady=20, command=button_equal).grid(row = 5, column = 1, columnspan = 2)

Button(root,text='-', padx=41, pady=20, command=button_subtract).grid(row = 6, column = 0)
Button(root,text='*', padx=41, pady=20, command=button_multiply).grid(row = 6, column = 1)
Button(root,text='/', padx=41, pady=20, command=button_divide).grid(row = 6, column = 2)


root.mainloop() #constant loop