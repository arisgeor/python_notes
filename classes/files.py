#! python3

#when typing a windows path be sure to escape the backslash with another bachslash
print('\\') #this will print "\"
print('c:\\spam\\eggs.png')
#or alternative use raw strings 
print(r'c:/Python39/Python_Projects/Simple_Stuff')

import os #path related functions
os.path.join('folder1','folder2','folder3') #joins the path according to your OS
os.getcwd() #get current directory
os.chdir('c:\\')
os.getcwd()

#Absolute file paths always begin with the c:\\ and gives the omplete location of the program
#relative file paths do not. Relative file paths are relative to the current working directory. 
#If i have 2 files named eggs.txt the relative path will refer to the eggs inside the cwd

os.path.isabs('c:\\folder\\folder')
os.path.dirname('c:\\folder1\\folder2\\spam.png') # will return the directory of the path, up to spam.png
os.path.basename('c:\\folder1\\folder2\\spam.png')# will return the last part of the path, after the final set of \\
os.path.exists('c:\\folder1\\folder2\\spam.png') #returns True if the path exists
os.path.isfile('c:\\windows\\system32\\calc.exe') #returns True if the final part of the path is a file.
os.path.isdir('c:\\windows\\system32\\calc.exe') #similarly this will return True is the final part of the path is a directory

os.path.getsize('c:\\windows\\system32\\calc.exe') #gets the size of the specified file 
os.listdir('c:\\') #return a list of strings with the files and folders contained in the folder 

#simple example
#calculates the size of all the files inside a directory
totalsize = 0
for filename in os.listdir('c:\\automatebook'):
    if not os.path.isfile(os.path.join('c:\\automatebook', filename)): #get rid of subfolders and just keep the files
        continue
    totalsize += os.path.getsize(os.path.join('c:\\automatebook', filename))

os.makedirs('c:\\delicious\\walnut\\waffles') #this func will create all these folders to complete the path!

