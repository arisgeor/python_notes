#! python3

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frames!')
root.iconbitmap(r'C:\Users\Aristos\Desktop\Aristos\random_pics\pacman.ico')

frame = LabelFrame(root, text = 'This is my Frame', padx = 50, pady=50)
frame.pack(padx = 10, pady = 10) #even though we packed the frame, we can still place elements inside of it!

b = Button(frame, text = "EXIT", command = frame.quit) #super carefull, instead of root, I placed it inside of the newly created grid!
b.grid(row = 0, column=0)

root.mainloop()