import cv2 as cv 

img1=cv.imread("opencv.png")
img2=cv.imread("roket.jpg")
print(img1.shape)
print(img2.shape)
img1=cv.resize(img1,(200,180))
img2=cv.resize(img2,(200,180))
print(img1.shape)
print(img2.shape)

#resimlerin boyutlarının aynı olması lazım 
#belirli pixeldeki değerleri toplar totalde ama max 255 yapar

totalImg=cv.add(img1,img2)
cv.imshow("totalImg",totalImg)

print("img1:    ",img1[120,80])
print("img2:    ",img2[120,80])
print("totalImg:    ",totalImg[120,80])

print("******aritmatik toplama*****************")

totalWeightedImg=cv.addWeighted(img1,0.7,img2,0.3,0) #bu resimlerden bu oranda pixelini al
print("img1:    ",img1[120,80])
print("img2:    ",img2[120,80])
print("totalWeightedImg:    ",totalWeightedImg[120,80])

cv.imshow("2totalWeightedImg",totalWeightedImg)

print("******aritmatik toplama2222222222222222222222222222222222222222*****************")

totalWeightedImg2=cv.addWeighted(img1,0.7,img2,0.3,50) #sonra da hepsine 50şer ekle
print("img1:    ",img1[120,80])
print("img2:    ",img2[120,80])
print("totalWeightedImg:    ",totalWeightedImg2[120,80])

cv.imshow("32totalWeightedImg",totalWeightedImg2)
cv.waitKey(0)
cv.destroyAllWindows()