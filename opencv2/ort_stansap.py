import cv2 as cv
import numpy as np

src=cv.imread("opencv.png",0) #grisiz çaılşmıyor???

#minMaxLoc

min_value, max_value, min_loc,max_loc=cv.minMaxLoc(src)
print("min_value:%.2f,  max_value:%.2f" %(min_value, max_value))

print("min_loc: ",min_loc," max_loc: ",max_loc)

#meanStdDev standart sapması
#ortalama ve standart sapma
means, stddev= cv.meanStdDev(src)
print("means:%.2f , stddev:%.2f" %(means, stddev))

#şimdi ortalamadan küçük olan değerlere atama yapalım
src[np.where(src<means)]=0
src[np.where(src>means)]=255


cv.imshow("binary",src)
cv.waitKey(0)