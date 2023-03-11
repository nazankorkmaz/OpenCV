# ---ROI---ilgilenen görüntünün bir bölümüne odaklanma
import numpy as np
import cv2 as cv

cap=cv.VideoCapture("yuruyeninsan.mp4")

fgbg=cv.createBackgroundSubtractorMOG2(history=500,varThreshold=100)
               
#boyutunu değiştirme
def rescale(frame, scale=0.3):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
 
    boyut = (width, height)
    return cv.resize(frame, boyut, interpolation=cv.INTER_AREA)


"""
Bu fonksiyon, bir görüntü üzerinde nesne algılama ve takip işlemleri gerçekleştirir. 
Fonksiyon girdi olarak bir görüntü alır ve çıkış olarak aynı boyutta bir görüntü döndürür, 
ancak üzerinde algılanmış nesnelerin elips ve daire şekilleriyle çizilmiş halleri vardır.

İlk olarak, girdi görüntü, bir arka plan çıkarımı uygulanarak işlenir.
 Daha sonra, bu işlenmiş görüntüye bir yapısal eleman uygulanarak gürültüler kaldırılır ve ardından konturlar bulunur.

Bulunan konturlar, belirli bir alandan daha küçük olanları filtreler ve daha büyük olanları ise
 bir çerçeve etrafına yerleştirilen bir elips ve merkezi bir daire çizerek işaretler. 
 Elips ve daire, algılanan nesnenin şeklini ve konumunu gösterir.
"""
def process(image):
    mask=fgbg.apply(image)
    line=cv.getStructuringElement(cv.MORPH_RECT,(1,5),(-1,-1))
    mask=cv.morphologyEx(mask,cv.MORPH_OPEN,line)
    cv.imshow("mask",mask)
    contours, hierarchy= cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in range(len(contours)):
        area= cv.contourArea(contours[c])
        if area<150:
            continue
        rect=cv.minAreaRect(contours[c])
        cv.ellipse(image, rect,(0,255,0),2,8)
        cv.circle(image,(np.int32(rect[0][0]), np.int32(rect[0][1])),2,(255,0,0),2,8,0)
    return image


#işlem sürekli olsun diye whilea giricek
while True:
    ret,frame= cap.read()
    frame = rescale(frame)
    cv.imshow("input",frame)
    result=process(frame)
    cv.imshow("result",result)
    k= cv.waitKey(0) & 0xff
    if k==24:
        break


    """
    Mask, bir görüntünün belirli bir bölgesini belirlemek için kullanılan bir siyah beyaz görüntüdür.
     Maskeler, bir görüntünün yalnızca belirli bir bölümünü işleme sokmak istediğimiz durumlarda sıkça kullanılır.
    bu işlemler arasında örneğin, belirli bir rengi, şekli ya da hareketi algılamak veya görüntüdeki arka planı ayırmak gibi işlemler
     yer alabilir. Maskeler, piksellerin belirli bir bölgesinde siyah veya beyaz bir değerle belirtilir 
    ve daha sonra bu maske görüntü üzerine uygulanarak, ilgilenilen bölgeye yönelik işlemler gerçekleştirilebilir
    """