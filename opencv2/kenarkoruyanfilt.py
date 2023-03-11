#kenardan kasıt resimdeki kenarlar yani çene  göz bölgeleri , kirpik gibi

import cv2 as cv
import numpy as np

src=cv.imread("yakincekim.jpg") 
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)

h,w=src.shape[:2]

dst=cv.edgePreservingFilter(src, sigma_s = 10, sigma_r=0.3, flags=cv.RECURS_FILTER)  #s: şiddet(0-200); r de kenarlara ne kadar uygulansın bu filtre (0-1)

#iki resmi yan yana koyduk
result=np.zeros([h, w*2 ,3] , dtype=src.dtype)
result[0:h, 0:w, :] =src
result[0:h, w:2*w, :]=dst

result= cv.resize(result, (w,h//2))
cv.imshow("result",result)
cv.waitKey(0)