import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #creates a blank image. uint = datatype of an image. ,3 refers to the number of color channels.
cv.imshow('Black', blank)

#1 paint the img a certain colot.
blank[:] = 0,255,0                  #select all the pixels of the black img and turn them Green
cv.imshow('Green', blank)           #display it

blank[200:300, 200:300] = 0,0,255   #select all the pixels of the black img and turn them Green
cv.imshow('Red', blank)             #display it

#2 draw a rectangle
blank2 = np.zeros((500,500,3), dtype='uint8')                   #I ll make a new one so its all black again.
cv.rectangle(blank2, (0,0), (250,250), (0,255,0), thickness=2)  #if you click inside, it will help you fill the params.
cv.imshow('Rectangle', blank2)
#instead of giving it fixed values:
cv.rectangle(blank2, (0,0), (blank2.shape[1]//2,blank2.shape[0]//2), (0,255,0), thickness=2) #with this you get exactly 1/4th.
cv.imshow('Rectangle', blank2)
#to fill it just use thickness = -1 or cv.FILLED
cv.rectangle(blank2, (0,0), (blank2.shape[1]//2,blank2.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank2)

#3 draw a circle
cv.circle(blank2, (blank2.shape[1]//2,blank2.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank2)

#4 draw a line
cv.line(blank2, (0,0), (blank2.shape[1]//2,blank2.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank2)

#5 text on an image
cv.putText(blank2, 'Hello', (0,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank2)           

#always have this one, otherwise your pics wont show up.
cv.waitKey(0)                      