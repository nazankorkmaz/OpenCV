
#belirli bir videodaki renklerin yoğunluğunu tespit etme

import cv2 as cv
import numpy as np

#boyutunu değiştirme
def rescale(frame, scale=0.4):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
 
    boyut = (width, height)
    return cv.resize(frame, boyut, interpolation=cv.INTER_AREA)

cap=cv.VideoCapture("parti.mp4")
ret,  frame1=cap.read()
frame1 = rescale(frame1)

prvs=cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

#Bu işlem, RGB renk uzayında yüksek doyumlu piksellerin HSV uzayında daha belirgin hale gelmesini sağlar. 
hsv=np.zeros_like(frame1)
hsv[...,1]=255


def dense_opt_flow(hsv,prvs):
    while 1:
        ret,frame2=cap.read()
        frame2 = rescale(frame2)
        nextt=cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
        flow=cv.calcOpticalFlowFarneback(prvs,nextt,None,0.5,3,15,3,5,1.2,0)
        mag,ang=cv.cartToPolar(flow[...,0],flow[...,1])
        hsv[...,0]=ang*180/np.pi/2
        hsv[...,2]=cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
        bgr=cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
        cv.imshow("frame2",bgr)
        cv.imshow("frame1",frame2)
        k=cv.waitKey(24) & 0xff
        if k==24:
            break
        prvs=nextt

dense_opt_flow(hsv,prvs)


"""
Bu kod, optik akış hesaplamasını (optical flow) gerçekleştirir ve görselleştirir. 
İlk olarak, "dense_opt_flow" adlı bir fonksiyon tanımlanır ve bu fonksiyon "hsv" ve "prvs" değişkenleriyle çağrılır. 
Bu değişkenler, önceki kare (frame) ve HSV görüntüsünü tutarlar.

Daha sonra, bir döngü oluşturulur ve kameradan gelen yeni bir kare ("frame2") okunur ve yeniden boyutlandırılır.
 Ardından, "cv.cvtColor" işlevi kullanılarak, "frame2" görüntüsü BGR renk uzayından gri ölçekteki (gray scale) bir görüntüye dönüştürülür.

"cv.calcOpticalFlowFarneback" işlevi kullanılarak, optik akış vektörleri ("flow") hesaplanır. 
Bu işlevin argümanları, optik akış algoritmasının parametreleridir ve burada "calcOpticalFlowFarneback" işlevi, 
Farneback yöntemini kullanarak optik akışı hesaplar. Bu yöntem, piksel tabanlı bir yaklaşım kullanarak hareketin tespit edilmesini sağlar.

Sonra, "cv.cartToPolar" işlevi kullanılarak, "flow" dizisi kutup (polar) koordinatlara dönüştürülür. 
Bu işlev, her bir piksel için hareket yönü (angle) ve büyüklüğünü (magnitude) hesaplar ve "mag" ve "ang" değişkenlerinde saklar.

"hsv" dizisinin ton (hue) bileşeni, "ang" dizisinden elde edilen açı değerleriyle güncellenir.
 Bu işlem, piksellerin hareket yönüne göre renklendirilmesini sağlar. "hsv" dizisinin değer (value) bileşeni,"mag" dizisinin normalize edilmiş
(min-max normalizasyonu) değerleriyle güncellenir. Bu işlem, hareketin büyüklüğüne göre piksellerin parlaklığının ayarlanmasını sağlar.

Son olarak, "cv.cvtColor" işlevi kullanılarak, "hsv" görüntüsü BGR renk uzayına dönüştürülür 
ve "frame2" ve "bgr" görüntüleri "cv.imshow" işlevi kullanılarak ekrana yazdırılır. 
Döngü, bir tuşa basıldığında veya 24 ms geçtiğinde durdurulur.

"""
