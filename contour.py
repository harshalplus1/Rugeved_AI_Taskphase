#contour detection
import cv2 as cv
import numpy as np
# img=cv.imread("/home/harshal/Desktop/index.jpeg")
# cv.imshow("IMG",img)
# blank=np.zeros(img.shape, dtype="uint8")
# cv.imshow("blank",blank)
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# canny=cv.Canny(gray,125,175)
# cv.imshow("canny",canny)
# contour,hierarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# cv.drawContours(blank,contour,-1,(0,0,255),1)
# cv.imshow("Counter Drawn",blank)
vid=cv.VideoCapture(0)
while True:
    ret,frame=vid.read()
    blank=np.zeros(frame.shape, dtype="uint8")
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    canny=cv.Canny(gray,125,175)
    contour,hierarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    cv.drawContours(blank,contour,-1,(0,0,255),2)
    cv.imshow("Counter Drawn",blank)
    if cv.waitKey(1) & 0xFF==ord("s"):
        break
vid.release()
cv.destroyAllWindows