#! python3 

#when typing a windows path be sure to escape the backslash with another bachslash
print('\\') #this will print "\"
print('c:\\spam\\eggs.png')
#or alternative use raw strings 
print(r'c:\Python39\Python_Code\python_notes')

import os #path related functions
os.path.join('folder1','folder2','folder3') #joins the path according to your OS
os.getcwd() #get current directory
os.chdir('c:\\')
os.getcwd()

#Absolute file paths always begin with the c:\\ and gives the omplete location of the program
#relative file paths do not. Relative file paths are relative to the current working directory. 
#If i have 2 files named eggs.txt the relative path will refer to the eggs inside the cwd

os.path.isabs('c:\\folder\\folder')
os.path.dirname('c:\\folder1\\folder2\\spam.png') #will return the directory of the path, up to spam.png
os.path.basename('c:\\folder1\\folder2\\spam.png') #will return the last part of the path, after the final set of \\
os.path.exists('c:\\folder1\\folder2\\spam.png') #returns True if the path exists
os.path.isfile('c:\\windows\\system32\\calc.exe') #returns True if the final part of the path is a file.
os.path.isdir('c:\\windows\\system32\\calc.exe') #similarly this will return True is the final part of the path is a directory

os.path.getsize('c:\\windows\\system32\\calc.exe') #gets the size of the specified file 
os.listdir('c:\\') #return a list of strings with the files and folders contained in the folder 

#simple example
#calculates the size of all the files inside a directory
totalsize = 0
for filename in os.listdir('c:\\Python39\\Python_Code\\python_notes\\classes'):
    if not os.path.isfile(os.path.join('c:\\automatebook', filename)): #get rid of subfolders and just keep the files
        continue
    totalsize += os.path.getsize(os.path.join('c:\\automatebook', filename))

#this func will create all these folders 
os.makedirs('c:\\delicious\\walnut\\waffles') 

#there are 2 types of files
#plain text and
#binary (which you cannot open with a text editor)

#to open a file in python use the open() function, which will open it in READ MODE
helloFile = open('c:\\Python39\\Python_Code\\python_notes\\classes\\simple_text.txt')
content = helloFile.read() #if i want to read the file i ll need to reuse this line, so i ll save it in a variable
helloFile.close() #then i need to close the file
print(content)
print('\n\n\n')

#there is also a readlines method
helloFile = open('c:\\Python39\\Python_Code\\python_notes\\classes\\simple_text.txt')
helloFile.readlines() #This will return all of the lines as a list of strings
helloFile.close()

#if i want to write to a file i need to open it to write or append mode
#write mode will overwrite the file data, whereas append will add to the end of the file
#if the file doesn't exist, python will create it, as long as it has the w or a flag!
helloFile = open('c:\\Python39\\Python_Code\\python_notes\\classes\\simple_text2.txt', 'w') #the 'w' indicates the write mode
helloFile.write('Hello !!!\n')
helloFile.close() #don't forget to close the file!
helloFile = open('c:\\Python39\\Python_Code\\python_notes\\classes\\simple_text2.txt', 'a') #the 'a' indicates the write mode
helloFile.write('\n\nHello again!!!\n')


#I can save variables in my file using the shelve module, like list and dictionaries
import shelve
myFile = shelve.open('c:\\Users\\Aristos\\Desktop\\shelve_text.txt') #this will create the file if if doesnt exist already
#i can make changes to the shelve value as if it was a dict.
myFile['cats'] = ['Zophie', 'Pooka', 'Simon'] #so i saved a list of strings as a value to the key "cats"
#this will crete 3 binary files (.bak .dat .dir) and a db file on linux
myFile.close()

myFile = shelve.open('c:\\Users\\Aristos\\Desktop\\shelve_text.txt')
myFile['cats'] #this will return the Value of the key cats (the list of names)
myFile.close()

myFile = shelve.open('c:\\Users\\Aristos\\Desktop\\shelve_text.txt')
list(myFile.keys())
list(myFile.values())
myFile.close()

#copying and moving files
import shutil
mytext = open('c:\\Users\\Aristos\\Desktop\\text.txt','w')
mytext.write('I am a simple text')
shutil.copy('c:\\Users\\Aristos\\Desktop\\text.txt', 'c:\\delicious') #this will copy shelve_text.txt to the folder delicious
shutil.copy('c:\\Users\\Aristos\\Desktop\\text.txt', 'c:\\delicious\\spamspamspam.txt') #this will copy and rename the shelve_text.txt file to the delicious folder
mytext.close()
#to copy an entire folder (and rename it in this case)
shutil.copytree('c:\\delicious', 'c:\\delicious_backup') #this command will create a new folder named "delicious_backup"
#to move a file
shutil.move('c:\\delicious\\spamspamspam.txt', 'c:\\delicious\\walnut')
#if i want to rename a file i just move it to the same folder with a different name
shutil.move('c:\\delicious\\walnut\\spamspamspam.txt', 'c:\\delicious\\walnut\\eggs.txt')

#Deleting files and folders
os.makedirs('c:\\empty_folder') #first i ll create and empty folder for the purposes of this example
os.unlink('c:\\Users\\Aristos\\Desktop\\text.txt') #delete a file!
os.rmdir('c:\\empty_folder')
# python allows you to only delete empty folders as a safety mechanism!
# you will have to use shutil.rmtree() to entirely delete a folder with files
shutil.rmtree('c:\\delicious')
shutil.rmtree('c:\\delicious_backup')
# I deleted the folders and files I created previously, to be able to rerun the program without crashing it

# The best practice before deleting files is to do a "Dry Run"
import os
os.chdir('c:\\Users\\Aristos\\Desktop')
for filename in os.listdir():
    if filename.endswith('.txt'):    #before deleting I will print these files just to be sure. Then uncomment the unlink method and proceed
        #os.unlink(filename)
        print(filename) 

# It is always much safer to just send files to the recycle bin, rather than deleting them.
# First I ll need to pip install it to my folder before i use it, so open a terminal, go to 
# your destiunation folder and run pip.exe install send2trash

import send2trash
mytext = open('c:\\Users\\Aristos\\Desktop\\text2.txt','w') #create this short-life txt file.
mytext.close()
send2trash.send2trash('c:\\Users\\Aristos\\Desktop\\text2.txt') #send it to the recycle bin, where it belongs.

# the os.walk() function
for folderName, subfolders, filenames in os.walk('c:\\Python39\\Python_Code\\python_notes'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(subfolders))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)
        
    for file in filenames:
        if file.endswith('.py'):
            break
            #send2trash.send2trash(file)

#i can do a lot of cool stuff with os.walk()!