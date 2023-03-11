import cv2 as cv

img=cv.imread("opencv.png")
cv.namedWindow("rgb",cv.WINDOW_AUTOSIZE)
cv.imshow("rgb",img)

#RGB to gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

cv.waitKey(0)
cv.destroyAllWindows()