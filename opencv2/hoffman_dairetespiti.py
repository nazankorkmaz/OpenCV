
import cv2 as cv
import numpy as np


src=cv.imread("para.jpg")

gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)

gray= cv.GaussianBlur(gray,(9,9),2,2) #gürültü gidermek için

circles=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,dp=1, minDist=10, param1=20 ,param2=20,minRadius=0,maxRadius=20)
#2.si yöntemi ; dp resmin çözünürlüğü 1 ise girdiyle aynı çözünürlük olsun
#minDist- dairenin merkezi ile min uzaklığı ; param1 kenar saptama 2 daire saptama 
#sonuncuları min max yarıçap için
for c in circles[0,:]:  #dairelerin etrafını renklendirme işlemi
    print(c)
    cx ,cy ,r=c
    #cv.circle(src, (cx,cy),2 ,(0,255,0),2,8,0)
    #cv.circle(src, (cx,cy),r ,(0,0,255),2,8,0)
    cv.circle(src, (int(cx),int(cy)), 2, (0,255,0), 2)
    cv.circle(src, (int(cx),int(cy)), int(r), (0,0,255), 2)



cv.imshow("hough",src)
cv.waitKey(0)


