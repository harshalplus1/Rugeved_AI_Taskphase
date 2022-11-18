import numpy as np
import cv2 as cv
img=cv.imread("/home/harshal/Desktop/pothole.jpg")
# img1=cv.imread("/home/harshal/Desktop/pothole1.png")
cv.imshow("ROAD",img)
roi=img[83:576,3:853]
# crop_img=img[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
# cv.imwrite("Crop",crop_img)
# cv.imshow("Cropped Image",crop_img)
gray=cv.cvtColor(roi,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(23,23),11)
blur1=cv.medianBlur(blur,15)
blur2=cv.blur(blur1,(23,23))
blur3=cv.bilateralFilter(blur2,15,25,25)
# cv.imshow("Blur",blur3)
threshold,bw=cv.threshold(blur3,112,153,cv.THRESH_BINARY)
# cv.imshow("Binary_IMG",bw)
kernel = np.ones((5,5), np.uint8)  
img_erosion = cv.erode(bw, kernel, iterations=1)
img_dilation = cv.dilate(img_erosion, kernel, iterations=1)  
contours,hierarchies=cv.findContours(img_dilation,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# cv.imshow("BLUR",bw)
blank=np.zeros(roi.shape,dtype="uint8")
canny=cv.Canny(img_dilation,120,175)
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("Pothole",blank)
cv.waitKey(0)
