# giriş olrak verilen görüntüyü binarye çevirir
#pikselleri siyah veya beyaza döndürür
#bir theshold belirleyerek bunların altında kalanlara beyaz üstündekilere siyah ekler

import cv2 as cv
import numpy as np

src=cv.imread("yakincekim.jpg")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)

gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)

ret,binary=cv.threshold(gray,15,250,cv.THRESH_BINARY | cv.THRESH_OTSU) 
#ret-- thresholdu ; binary-- binaryi zaten temsil eder
#binary eşikleme otsu yöntemine göre gerçekleştirilir

h,w= src.shape[:2]
cv.imshow("binary",binary)
cv.waitKey(0)