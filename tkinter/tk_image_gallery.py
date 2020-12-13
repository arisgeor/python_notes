#! python3

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My first encounter with images') #give a title.
root.iconbitmap(r'C:\Users\Aristos\Desktop\Aristos\random_pics\pacman.ico') #.ico file for the app icon-favicon.

#for images you need to use pillow, an improved version of python image library (PIL) 
#images are a 3step process
my_img1 = ImageTk.PhotoImage(Image.open(r'C:\Users\Aristos\Desktop\Aristos\random_pics\cutcat.png'))
my_img2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Aristos\Desktop\Aristos\random_pics\Cover.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open(r'C:\Users\Aristos\Desktop\Aristos\random_pics\IMPERFECT.png'))
my_img4 = ImageTk.PhotoImage(Image.open(r'C:\Users\Aristos\Desktop\Aristos\random_pics\grammar.png'))
my_img5 = ImageTk.PhotoImage(Image.open(r'C:\Users\Aristos\Desktop\Aristos\random_pics\salonica.jpg'))

image_list =[my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text = 'Image 1 out of ' + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E) 
#bd defines the border and relief will make it sunken, almost 3D like. Finaly anchor will 'anchor' it to one side, here to the East.
#finally as with the images, this label needs to be updated each time I press the forward or back buttons.

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):              #everytime the function is called I rebuild the entire Window!
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() #get rids of the label
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text = '>>', command = lambda: forward(image_number+1))
    button_back = Button(root, text = '<<', command = lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text = '>>', state = DISABLED)

    #finaly when everything is checked I place the elements.
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row = 1, column = 2)
    button_back.grid(row = 1, column = 0)

    #update the status bar as well
    status = Label(root, text = 'Image ' + str(image_number) + ' out of ' + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E) 
    status.grid(row = 2, column = 0 , columnspan = 3, sticky = W+E) 

    

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() #get rids of the label
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text = '>>', command = lambda: forward(image_number+1))
    button_back = Button(root, text = '<<', command = lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text = '<<', state = DISABLED)

    #finaly when everything is checked I place the elements.
    button_forward.grid(row = 1, column = 2)
    button_back.grid(row = 1, column = 0)
    my_label.grid(row=0, column=0, columnspan=3)

    #update the status bar as well
    status = Label(root, text = 'Image ' + str(image_number) + ' out of ' + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E) 
    status.grid(row = 2, column = 0 , columnspan = 3, sticky = W+E)


#This is where I Click the first time and then the above functions take over!
button_back = Button(root, text = '<<', command = back, state = DISABLED)
button_exit = Button(root, text = 'EXIT', command = root.quit)
button_forward = Button(root, text = '>>', command = lambda: forward(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 10)
status.grid(row = 2, column = 0 , columnspan = 3, sticky = W+E) #Tkinter has a compass like navigation system NESW, and here I told it to stick to West and East.

root.mainloop()