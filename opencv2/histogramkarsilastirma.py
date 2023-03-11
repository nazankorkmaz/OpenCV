#resimler birbirine ne kadar benziyor ona bakıcaz matriksel olarak

#neden hsv ye çeviriyoruz çünkü daha kolay nesne takibi ve resimlerle renklerin kolay ayrılması yönünden

import cv2 as cv

src1=cv.imread("dw.jpg")
src2=cv.imread("comicspider.jpg")
src3=cv.imread("python.jpg")

hsv1=cv.cvtColor(src1,cv.COLOR_BGR2HSV)
hsv2=cv.cvtColor(src2,cv.COLOR_BGR2HSV)
hsv3=cv.cvtColor(src3,cv.COLOR_BGR2HSV)


hist1=cv.calcHist([hsv1],[0,1],None,[60,64],[0,180,0,256]) #0 ve 1 kullanılacak kanallar-----None taslak , mask kullanılmayacak
hist2=cv.calcHist([hsv2],[0,1],None,[60,64],[0,180,0,256]) #60,64 histogramın boyutları ve son değişken de rangeler yani aralıklar ifade edilmiştir
hist3=cv.calcHist([hsv3],[0,1],None,[60,64],[0,180,0,256])

#normalize __görüntünün konstratını arttırmak piksellerini değiştirmek

cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX) #0la 1 arası dönüşüm yapmak istiyorum
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

#compareHist
#görsellerin benzerliklerine bakıcaz
#HISTCMP_CORREL yöntemini kullanıcaz

print(cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL))
print(cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL))
print(cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL))

