#x ve y lerin yer değiştirmesi yani haritalanması demektir.
#piksellerin eski konumundan yeni konumuna taşınması

import cv2 as cv
import numpy as np

#shifting__kaydırma  

img=cv.imread("dw.jpg")

rows=img.shape[0] #satır sayısı
cols=img.shape[1] #sutün sayısı

M=np.float32([[1,0,250],[0,1,200]]) #çıktının nerde olacağı

shifted=cv.warpAffine(img,M,(cols,rows)) #kaynak matrisin nerde olacağını değiştiriyorum artık

cv.imshow('original',img)

cv.imshow('shifted',shifted)



#rotation___döndürme
#190 derece döndürdük
R=cv.getRotationMatrix2D((cols/2,rows/2),190,1)

dst=cv.warpAffine(img,R,(cols,rows))

cv.imshow('rotation',dst)



#scaling__resim boyutunu değiştirme
#büyültmek için 1den büyük sayı girin
res=cv.resize(img,None,fx=0.2,fy=0.2,interpolation=cv.INTER_CUBIC)
cv.imshow("scaling",res)


#bu işlemleri küçültülmüş resimde yapalım

rows=res.shape[0] 
cols=res.shape[1] 
M=np.float32([[1,0,200],[0,1,90]]) 

shifted=cv.warpAffine(res,M,(cols,rows)) 
cv.imshow('kshifted',shifted)
R=cv.getRotationMatrix2D((cols/2,rows/2),45,1)
dst=cv.warpAffine(res,R,(cols,rows))

cv.imshow('krotation',dst)
cv.waitKey(0)