import cv2 as cv

resim=cv.imread("comicspider.jpg")
print(resim.shape)
aynalananResim=cv.copyMakeBorder(resim,75,75,125,125,cv.BORDER_REFLECT )
#üst alt sağ sol sınırları verilir ve ne yapılıcağı fonksiyonu yazılır.

uzatilanResim=cv.copyMakeBorder(resim,75,75,120,125,cv.BORDER_REPLICATE )

tekrarResim=cv.copyMakeBorder(resim,100,70,120,125,cv.BORDER_WRAP )

cerceveResim=cv.copyMakeBorder(resim,100,70,120,125,cv.BORDER_CONSTANT, value=(75,50,225) )

cv.imshow("ayna",aynalananResim)
cv.imshow("uzatilan",uzatilanResim)
cv.imshow("TEKRARLANAN",tekrarResim)
cv.imshow("cerceve",cerceveResim)

cv.waitKey(0)
cv.destroyAllWindows()
