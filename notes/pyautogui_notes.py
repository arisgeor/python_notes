#! python3

import pyautogui #pip install pyautogui

width, height = pyautogui.size()

###mouse controll
pyautogui.position()
pyautogui.moveTo(10,10) #moves the mouse to specified position.
pyautogui.moveTo(10,10, duration = 2)
pyautogui.moveRel(200,0) #moves the mouse from current position.
pyautogui.moveRel(200,0, duration = 2)

pyautogui.dragRel() #similart to moveRel but keeps the mouse clicked all the way. Helpfull for painting!

#pyautogui has a safety mechanism to prevent you from losing control of the programm.
#during each call there is a 1/10 second pause at the end, where you have control of the mouse. 
#if you manage to move it to the upperleft corner (0,0) then the programm will stop.

#to click
pyautogui.position() #get the position of the object you want to click.
pyautogui.click() #clicks to current cursor position.
pyautogui.click(500, 85)
pyautogui.doubleClick(790, 380)

pyautogui.displayMousePosition() #use this from the terminal to quickly see the X,Y .#CTRL+C to quit.


### Keyboard
pyautogui.click(200,50);pyautogui.typewrite('Hello World') #I need to use the ; otherwise my mouse will point elsewhere!
pyautogui.click(200,50);pyautogui.typewrite(['A', 'r','i','s'], interval = 1)
#the brackets [] work as inputs meaning single key hits on the keyboard.

#For example the command below works as if you hit the volume down key of your keyboard.
pyautogui.typewrite(['volumedown']) #decreases volume by 2 units! #might implement a bash script later...

#a simple func to decrease the volume!
def dec_vol(num = 2):
    for _ in range(int(num/2)):
        pyautogui.typewrite(['volumedown'])

#to view all the cool tricks u can do:
pyautogui.KEYBOARD_KEYS

pyautogui.typewrite(['enter'])#is the same as:
pyautogui.press('enter')    # press the Enter key
pyautogui.keyDown('shift')  # hold down the shift key #usufull for Shift+other_keys

###screenshots

pyautogui.screenshot()                              #this will return a Pillow object (PIL)
pyautogui.screenshot('c:\\screenshot_example.png')  #this will save the file.

pyautogui.locateOnScreen('c:\\my_screenshot.png')                 #where element is just the path of the image I want to locate on the screen.
pyautogui.locateCenterOnScreen('c:\\my_screenshot.png')           #returns just the first to values of the tuple. Then i can do:
pyautogui.moveTo((932,336), duration = 1) 
pyautogui.click((932,336))                          #or pyautogui.click(932,336)  works just as well without the ()     

