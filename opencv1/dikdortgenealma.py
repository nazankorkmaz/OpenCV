import cv2 as cv

resim=cv.imread("avengers.jpg")

print(resim.shape)
resim2=cv.resize(resim,(720,540))
cv.imshow("resim2",resim2)

#(x,y) koordinatları girilir önce karenin sol alt köşesi sonra da sağ üst köşesi 
#karenin rengi ve kenarının kalınlığı girilir
cv.rectangle(resim,(200,370),(350,220),(0,0,255),2)

cv.imshow("2avengers",resim)

cv.waitKey(0)
cv.destroyAllWindows()