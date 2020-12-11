#! python3

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My first encounter with images') #give a title.
root.iconbitmap(r'C:\Users\Aristos\Desktop\Aristos\random_pics\pacman.ico') #.ico file for the app icon-favicon.

#for images you need to use pillow, an improved version of python image library (PIL) 
#images are a 3step process
my_img = ImageTk.PhotoImage(Image.open(r'C:\Users\Aristos\Desktop\Aristos\random_pics\cutcat.png'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text = 'Exit Program', command = root.quit) #root.quit(closes)
button_quit.pack()

root.mainloop()