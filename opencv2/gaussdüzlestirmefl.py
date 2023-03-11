#görüntüyü yumuşatmak ve gürültüyü azaltmak

import cv2 as cv
import numpy as np

src=cv.imread("yakincekim.jpg")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)

h,w=src.shape[:2]

dst=cv.bilateralFilter(src,0,160,15) #0 piksel çapı; renk uzayı yani zıt renkler o kadar çok karışır; en sonda ne kadar pikselin birbirine karışacağını verir

#iki resmi yan yana koyduk
result=np.zeros([h, w*2 ,3] , dtype=src.dtype)
result[0:h, 0:w, :] =src
result[0:h, w:2*w, :]=dst

cv.imshow("result",result)
cv.waitKey(0)