import cv2 as cv
import numpy as np

src=cv.imread("yakincekim.jpg")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)

edge=cv.Canny(src,20,500)
cv.imshow("mask image",edge)
cv.waitKey(0)

#resmin kenarlarını gösterir