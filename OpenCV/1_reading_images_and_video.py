import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)               #displayes an image (the argument img)
cv.waitKey(0)                       #waits for an inf amount of time

