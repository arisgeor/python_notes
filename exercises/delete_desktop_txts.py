#! python3 

#Delete all .txt files from desktop 
import os
import send2trash
os.chdir('c:\\Users\\Aristos\\Desktop')
for filename in os.listdir():
    if filename.endswith('.txt'):    
        send2trash.send2trash(filename) #actually way better to just send them to the recycle bin instead. 
        #print(filename) #in case you need to check first.