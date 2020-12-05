#! python 3 

from tkinter import *                   #that way i can use button() instead of tkinter.button()


window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6

    #Empty the Text box if it had text from the previous use and fill it again
    t1.delete("1.0", END)                                       #Deletes the content of the Text box from start to END
    t1.insert(END, miles)                                       #END places the text at the end of the file

b1 = Button(window, text = 'Execute', command = km_to_miles)    
b1.grid(row=0,column=0)                                         

e1_value=StringVar()                                            #Create a special StringVar object
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0,column=1)

t1 = Text(window, height=1, width=20)           #I need to specify width and height because the default values are huge!
t1.grid(row=0, column=2)

window.mainloop()                               #I ll write my code between the Tk() object and the mainloop()
