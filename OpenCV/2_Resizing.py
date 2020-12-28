import cv2 as cv

#to resize the files I ll use the following method!
def rescaleFrame(frame, scale = 0.5):
    #Images, Videos and Live Video.
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimentions = (width, height)

    return cv.resize(frame, dimentions, interpolation = cv.INTER_AREA)

###Images###

img = cv.imread('Photos/cat.jpg')
img_resized = rescaleFrame(img)

cv.imshow('Cat', img)               #displayes an image (the argument img)
cv.imshow('Cat_resized', img_resized)

cv.waitKey(0)                       #waits for an inf amount of time

###Videos###

capture = cv.VideoCapture('Videos/flash_over_q.webm')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)       
    cv.imshow('Video Resized', frame_resized)       

    if cv.waitKey(33) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()


def changeRes(width, height):
    #works only on live video.
    capture.set(3,width)            #3 refers to the width and 4 to the height
    capture.set(4,height)           #ofc other codes of set() refer to other attributes such as brightenss etc.