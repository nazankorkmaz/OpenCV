import cv2 as cv
import numpy as np

img1=cv.imread("spiderreal.jpg")#("opencv.png")#
img2=cv.imread("spiderreal.jpg")#("comicspider.jpg")
print(img1.shape)
print(img2.shape)
cv.imshow("spider_real",img1)
cv.waitKey(1000)
cv.imshow("spider_comic",img2)
cv.waitKey(1000)

horizontal= np.hstack((img2, img1)) #numpy kütüphanesi birleştirdi resimleri
cv.imshow("spider_man",horizontal)
cv.waitKey(1000)
cv.destroyAllWindows()
#iki farkli resimi kabul etmiyor neden bilmiyorum belki boyutlardandır