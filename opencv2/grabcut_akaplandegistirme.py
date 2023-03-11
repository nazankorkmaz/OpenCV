#renkler karışıyor ve çok düzgün çalışmıyor. Bak buna tekrardan

import cv2 as cv
import numpy as np

src=cv.imread("insanlar.jpg")
src=cv.resize(src,(0,0),fx=0.2, fy=0.2)
r=cv.selectROI("input",src,False) #seçtik
#şimdi roi alanını belileyelim ve kopyalayalım
roi=src[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2]) ]
img=src.copy()
#çizim işlemini ifade etsin
cv.rectangle(img, (int(r[0]), int(r[1])),  (int(r[0]) + int(r[2]), int(r[1])+ int(r[3])), (255,0,0),2)
mask=np.zeros(src.shape[:2], dtype=np.uint8)
#arka plandan ayrılması için
rect=(int(r[0]),int(r[1]),int(r[2]),int(r[3]) )
bgdmodel=np.zeros((1,65), np.float64)
fgdmodel=np.zeros((1,65), np.float64)
#çıkması ve ayrışması için
cv.grabCut(src,mask,rect, bgdmodel, fgdmodel,11, mode=cv.GC_INIT_WITH_RECT)
#olası ön plan bölgelerini ayıklayalım
mask2=np.where((mask==1) + (mask==3),255,0).astype("uint8")

#arka plan resmi
background=cv.imread("avengers.jpg")

h, w,ch=src.shape
background=cv.resize(background,(w,h))
mask=np.zeros(src.shape[:2],dtype=np.uint8)
bgdmodel=np.zeros((1,65), np.float64)
fgdmodel=np.zeros((1,65), np.float64)

cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 5, mode=cv.GC_INIT_WITH_RECT )
mask2=np.where((mask==1)+(mask==3),255,0).astype('uint8')

#yapılandırıcaz
se=cv.getStructuringElement(cv.MORPH_RECT,(3,3))

#genişletme
cv.dilate(mask2,se,mask2)

#geçiş yumuşatma
mask2=cv.GaussianBlur(mask2,(5,5),0)

background=cv.GaussianBlur(background,(0,0),15)
mask2=mask2/255.0
a= mask[...,None]
result=a*(src.astype(np.float32)) + (1-a) * (background.astype(np.float32))

cv.imshow("result",result.astype(np.uint8))
cv.waitKey(0)