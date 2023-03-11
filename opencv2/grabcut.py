import cv2 as cv
import numpy as np

src=cv.imread("insanlar.jpg")
src=cv.resize(src,(0,0),fx=0.2, fy=0.2)

r=cv.selectROI("input",src,False) #seçtik #ilgi alanı seçtik

#şimdi roi alanını belirleyelim ve kopyalayalım
roi=src[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2]) ] #alanı çıkarttık seçtiğimiz
img=src.copy()

#çizim işlemini ifade etsin
cv.rectangle(img, (int(r[0]), int(r[1])),  (int(r[0]) + int(r[2]), int(r[1])+ int(r[3])), (255,0,0),2)



#arka plandan ayrılması için
#"cv.grabCut" işlevini kullanarak bir maske oluşturarak ROI'nin ön planını ve arka planını ayırın.
#Bu işlev, girdi görüntüsü, "cv.GC_BGD" (arka plan), "cv.GC_FGD" (ön plan) ile başlatılmış bir maske gerektirir.


mask=np.zeros(src.shape[:2], dtype=np.uint8)
rect=(int(r[0]),int(r[1]),int(r[2]),int(r[3]) )

bgdmodel=np.zeros((1,65), np.float64)
fgdmodel=np.zeros((1,65), np.float64)


#çıkması ve ayrışması için

cv.grabCut(src,mask,rect, bgdmodel, fgdmodel,11, mode=cv.GC_INIT_WITH_RECT)

#olası ön plan bölgelerini ayıklayalım

mask2=np.where((mask==1) + (mask==3),255,0).astype("uint8")

result=cv.bitwise_and(src,src, mask=mask2) #maskeyi orijinal görüntüye uygulayarak son sonucu elde eder

cv.imshow("roi",roi)
cv.imshow("result",result)
cv.waitKey(0)


#cv.grabCut" işlevini kullanarak bir maske oluşturarak ROI'nin ön planını ve arka planını ayırır 
# ve maskeyi orijinal görüntüye uygulayarak son sonucu elde eder.
