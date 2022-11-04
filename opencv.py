import cv2 as cv
import numpy as np
#image reading
#image resizing
img=cv.imread("/home/harshal/Downloads/test.jpg")
# img2=cv.resize(img,(500,500))
# img2=cv.resize(img,(1920,1080))
# #output
# cv.imshow("main",img)
# cv.imshow("2",img2)
# cv.waitKey(0)
#reading video
# vid=cv.VideoCapture("/home/harshal/Downloads/videoplayback.mp4")
# #reading webcam
# vid2=cv.VideoCapture(0)
# while True:
#     ret,frame=vid2.read()
#     #resizing video
#     frame2=cv.resize(frame,(500,500))
#     cv.imshow("test",frame)
#     cv.imshow("gg",frame2)
#     if cv.waitKey(20) & 0xFF==ord('s'):
#         break
# #reading a blank image
# img1=np.zeros((500,500,3), dtype='uint8')
# #coloring a portion
# img1[300:400, 300:400]=0,255,0
# cv.imshow("zvzv",img1)
# img2=np.zeros((500,500,3),dtype='uint8')
# cv.rectangle(img2,(0,0),(img2.shape[1]//2,img2.shape[0]//2),(0,255,0),thickness=cv.FILLED)
# cv.imshow('zz',img2)
# cv.circle(img2,(250,250), 40,(0,0,255),thickness=2)
# cv.imshow('circle',img2)
# grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('bb',grey)
# cv.putText(img2,"Harshal",(0,225),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
# cv.imshow('name',img2)
# vid2.release()
# blur=cv.GaussianBlur(img,(11,11), cv.BORDER_DEFAULT)
# cv.imshow('Black',blur)
vid2=cv.VideoCapture(0)
##translating an image
def translate(img,x,y):
        transMAT=np.float32([[1,0,x],[0,1,y]])
        dimensions=(img.shape[1],img.shape[0])
        return cv.warpAffine(img,transMAT, dimensions)
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint==None:
        rotpoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dim= (width,height)
    return cv.warpAffine(img,rotMat,dim)
##contour detection
img2=cv.imread('/home/harshal/Desktop/img.webp')
gray=cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
while True:
    ret,frame=vid2.read()
    #blur
    blur1=cv.GaussianBlur(frame,(3,3),cv.BORDER_DEFAULT)
    #canny
    canny=cv.Canny(blur1,90,90)
    #cropping
    cropp=blur1[0:50,0:50]
    # translating an image
    dd=translate(frame,100,100)
    ##rotation
    rott=rotate(frame,180)
    ##flipping
    flip=cv.flip(frame,1)
    ##contour detection
    cv.imshow("org",flip)
    if cv.waitKey(10) & 0xFF==ord('s'):
        break
vid2.release()
cv.waitKey(0)
cv.destroyAllWindows()
