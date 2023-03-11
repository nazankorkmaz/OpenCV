#amaç bir görüntüdeki belirli şekli özelliklerini izaole etmek

import cv2 as cv
import numpy as np

def canny_demo(image):
    t=100
    canny_output=cv. Canny(image,t,t*2)
    cv.imshow("canny_output",canny_output)
    return canny_output


src=cv.imread("s2.jpg")

cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)

binary= canny_demo(src)
cv.imshow("binary",binary)


#**************************************çalış
lines= cv.HoughLines(binary, 1, np.pi/180, 150, None,0,0)
if lines is not None:
    for i in range(0,len(lines)):
        rho=lines[i][0][0]
        theta=lines[i][0][1]
        a=np.cos(theta)
        b=np.sin(theta)
        x0=a* rho
        y0= b* rho
        pt1=(int(x0 + 1000 * (-b)), int(y0 +1000 * (a)))
        pt2=(int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv.line(src, pt1, pt2, (0,0,255),3,cv.LINE_AA)

cv.imshow("hough",src)
cv.waitKey(0)

#rho	Akümülatörün piksel cinsinden mesafe çözünürlüğü.
#theta	Akümülatörün radyan cinsinden açı çözünürlüğü.

#cv.HoughLines" işlevi kullanılarak Hough dönüşümü uygulanır ve
#  doğru çizgileri bulmak için bir eşik değeri (150) belirtilir.
#  Daha sonra, bulunan doğru çizgileri çizmek için bir döngü kullanılır.
#  Her doğru çizgi için, rho ve theta değerleri alınır ve bunlardan x0 ve y0 değerleri hesaplanır.
#  Daha sonra, bu değerler kullanılarak iki nokta (pt1 ve pt2) hesaplanır ve 
# "cv.line" işlevi kullanılarak doğru çizgisi görüntüye çizilir. 
