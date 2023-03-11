
import cv2 as cv

cap=cv.VideoCapture("parti.mp4")
fgbg=cv.createBackgroundSubtractorMOG2(history=2,varThreshold=100)  #gecikmeye ne kadar odaklanacğı ve hassasiyet

#yeniden boyutlandırma
def rescale(frame, scale=0.3):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
 
    boyut = (width, height)
    return cv.resize(frame, boyut, interpolation=cv.INTER_AREA)                         

while True:
    ret, frame=cap.read() #video bilgilerini tutacak
    frame = rescale(frame) #yeniden boyutlandırma***********************************
    fgmask=fgbg.apply(frame) #siyah arka plan burda elde edilir
    background=fgbg.getBackgroundImage() #arka plan görüntü hesaplaması ve arka plan resmi

    cv.imshow("input",frame)
    cv.imshow("mask",fgmask)
    cv.imshow("background",background)
    k=cv.waitKey(50) & 0xff
    if k==27:
        break

cap.release()
cv.destroyAllWindows()