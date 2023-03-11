import cv2 as cv
import numpy as np

img=cv.imread("python.jpg")
cv.namedWindow("image_create",cv.WINDOW_AUTOSIZE)
cv.imshow("image_create",img)


m1=np.copy(img) #kopyasını oluşturduk
m2=img
print(m2.shape)
img[100:225, 200:400, :]=0
cv.imshow("m2",m2)



m3=np.zeros(img.shape ,img.dtype)
cv.imshow("m3",m3)


m4=np.zeros([312,512],np.uint8) #bu boyutlarda olsun dedik
m4[:, :]=255 #rengini bu yapsın
cv.imshow("m4",m4)
cv.waitKey(0)
cv.destroyAllWindows()
