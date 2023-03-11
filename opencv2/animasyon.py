import cv2 as cv
import numpy as np

image=np.zeros((512,512,3),dtype=np.uint8)

for i in range(100000):
    image[:,:,:]=0
    x1=np.random.rand()*512 #rastgele x ve y eksenleri
    y1=np.random.rand()*512
    x2=np.random.rand()*512
    y2=np.random.rand()*512

    b=np.random.randint(0,256) #rastgele renkler
    g=np.random.randint(0,256)
    r=np.random.randint(0,256)

    cv.line(image,(int(x1),int(y1)),(int(x2),int(y2)),(b,g,r),4,cv.LINE_8,0)
    cv.rectangle(image,(int(x1),int(y1)),(int(x2),int(y2)),(b,g,r),1,cv.LINE_8,0)
    cv.imshow("image",image)
    c=cv.waitKey(20)
    if c==27:
        break

cv.destroyAllWindows()