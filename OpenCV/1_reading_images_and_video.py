import cv2 as cv

###Images###

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)               #displayes an image (the argument img)

cv.waitKey(0)                       #waits for an inf amount of time

###Videos###

#capture = cv.VideoCapture(0) #0 references the webcam
#now we ll examine an already existing video, so,
capture = cv.VideoCapture('Videos/flash_over_q.webm')
while True:
    isTrue, frame = capture.read()  #reads the specified video, frame by frame.
    cv.imshow('Video', frame)       #so its like projecting all images that compose the video.

    if cv.waitKey(33) & 0xFF==ord('q'): #closes when you press 'q', #waitkey controlls the playback speed of the video! 33seems about right.
        break

#Error -215:Assertion failed is when the video runs out of frames to show!

capture.release()
cv.destroyAllWindows()


