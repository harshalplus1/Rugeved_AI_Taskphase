import numpy as np
import cv2 as cv
vid=cv.VideoCapture("/home/harshal/Desktop/pothole.webm")
while True:
    ret,frame=vid.read()
    frame1=frame[83:576,3:853]
    gray=cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(23,23),11)
    blur1=cv.medianBlur(blur,15)
    blur2=cv.blur(blur1,(23,23))
    blur3=cv.bilateralFilter(blur2,15,25,25)
    # cv.imshow("Blur",blur3)
    threshold,bw=cv.threshold(blur3,137,153,cv.THRESH_BINARY)
    # cv.imshow("Binary_IMG",bw)
    kernel = np.ones((5,5), np.uint8)  
    img_erosion = cv.erode(bw, kernel, iterations=1)
    img_dilation = cv.dilate(img_erosion, kernel, iterations=1)  
    contours,hierarchies=cv.findContours(img_dilation,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    # cv.imshow("BLUR",bw)
    blank=np.zeros(frame.shape,dtype="uint8")
    canny=cv.Canny(img_dilation,120,175)
    cv.drawContours(frame1,contours,-1,(0,0,255),3)
    cv.imshow("Pothole",frame1)
    if cv.waitKey(1) & 0xFF==ord("s"):
         break
vid.release()
# img1=cv.imread("/home/harshal/Desktop/pothole1.png")
cv.waitKey(0)
