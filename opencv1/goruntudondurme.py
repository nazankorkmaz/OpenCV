import cv2 as cv
import numpy as np

src=cv.imread("opencv.png")

#x ekseninde döndürme

dst1=cv.flip(src,0)  #x eksenine göre çevir
cv.imshow("x-flip",dst1)

#y-flip
dst2=cv.flip(src,1)
cv.imshow("y-flip",dst2)

#xy-flip
dst3=cv.flip(src,-1)
cv.imshow("xy-flip",dst3)

cv.waitKey(0)