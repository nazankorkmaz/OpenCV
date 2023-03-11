import cv2 as cv
import numpy as np

#512ye 512 boyutunda 3 kanallı int tipinde array açtık
image=np.zeros((512,512,3),dtype=np.uint8)

cv.rectangle(image,(100,100),(200,200),(255,0,0),2,cv.LINE_8,0) #koordinat, uzunluk,renk
cv.circle(image,(100,100),50,(0,0,255),2,cv.LINE_8,0) #koordinat, yarıcap,renk
cv.ellipse(image,(100,100),(150,50),360,0,360,(0,255,0),2,cv.LINE_8,0) #hep koordinatlar

cv.imshow("image",image)
cv.waitKey(0)

#lineType--->hattın türü.
#shift--->Nokta koordinatlarındaki kesirli bitlerin sayısı.