#kenarları yakalamak demek renk geçişlerine odaklanmak demektir

import cv2 as cv
import numpy as np

src= cv. imread("opencv.png")

h,w=src.shape[:2]

# x ve y eksenlerine göre türev aldım

x_grad= cv.Sobel(src, cv.CV_32F,1,0) #dikey çekirdek
y_grad= cv.Sobel(src, cv.CV_32F,0,1) #yatay çekirdek

#bunları ölçeklendirelim ve standart formata getirelim

x_grad= cv.convertScaleAbs(x_grad)
y_grad= cv.convertScaleAbs(y_grad)

cv.imshow("x_grad",x_grad)  #yakalanan yerler farklı
cv.imshow("y_grad",y_grad)


#şimdi bunları birleştirelim

dst=cv.add(x_grad, y_grad, dtype=cv.CV_16S)    # Çıktı görüntüsünün derinliği. Taşmayı önlemek için CV_16S olarak ayarladık .
dst= cv.convertScaleAbs(dst)
cv.imshow("gradient",dst)

cv.waitKey(0)
