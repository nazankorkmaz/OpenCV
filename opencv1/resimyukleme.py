import cv2 as cv


path="roket.jpg"

#imread--> resimi alır okur ve img değişkenine atar. bunun için resmin dizinine ihtiyacı vardır
img= cv.imread(path)

print(type(img)) #numpy tipinde
cv.namedWindow("open_cv_test", cv.WINDOW_AUTOSIZE) #resmi otomatik boyutunda açtık ve ona bir isim verdik pencereye
cv.imshow("open_cv_test",img) #resmi bu adda bu yoldan aç dedik
print(img.shape)
cv.waitKey(1000) #konsolu bu kadar saniye oyala demek
cv.destroyAllWindows() #bütün açıktaki pencereleri kapa dedik. bu çoklu pencere açımında önemlidir. 
#bellekte yer tutmanın önüne de geçer.

#eğer böyle kullanırsan 0 dediğinde renkleri kullanma anlamına gelir


resim=cv.imread("opencv.png",0)
print(resim) #matrislerini yazdırır
cv.imshow("Ozengineer",resim)
print(resim.size) #resmin boyutunu yazdırır
print(resim.dtype) #tipini yazdırır
print(resim.shape) #genişlik yükseklik ve kaç kanal kullanımı
#ama bir gride olduğumuz için 1 kanal var onu da yazmıyor
cv.imwrite("yenigri.png",resim)
cv.waitKey(1000)
cv.destroyAllWindows()