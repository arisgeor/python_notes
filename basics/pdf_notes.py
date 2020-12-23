#! python 3 

### PDFs
#pip install PyPDF2 

import PyPDF2
import os

os.chdir('c:\\Users\\Aristos\\Desktop\\Aristos')
pdfFile = open('meetingminutes.pdf', 'rb') #we need to read in binary mode
reader = PyPDF2.PdfFileReader(pdfFile) #and then create a reader object, uppon which we can call any function.
reader.numPages
page = reader.getPage(0) #now i have selected the page and I can call methods uppon it.
page.extractText() #returns the text from the page 0

#to get all the text
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

#to combine 2 pdfs

pdf1File = open('meetingminutes1.pdf', 'rb') #open
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File) #create reader object
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter() #create the final #so far this only exists here. It hasn't been created yet.
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page) #the newly created pdf has the method .addPage which can add pages from different pdfs.

# I ll do the same for 
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb') #Here is where i "physicaly" create the combined file. Carefull with 'wb'
writer.write(outputFile) #and I pass it to my "writer" object
outputFile.close()
pdf1File.close()
pdf2File.close()

#that it for now!