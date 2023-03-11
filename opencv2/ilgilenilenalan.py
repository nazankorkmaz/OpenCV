#ROI (REGİON OF İNTEREST)

import cv2 as cv

src=cv.imread("dw.jpg")

h,w=src.shape[:2]

img=src.copy()

roi=img[500:800,200:550, :] #y1den y2 ye ve x1den x2ye

print(src.shape)
cv.imshow("roi",roi)
print(roi.shape[:2])

img[0:300,0:350,:]=roi  #copyaya kestiğim yeri yapıştırdım
cv.imshow("neewimg",img)
cv.waitKey(0)