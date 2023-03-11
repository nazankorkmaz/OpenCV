import cv2 as cv

vid = cv.VideoCapture(0) #ana kamera demek 0

while True:
    ret, frame= vid.read()

    cv.imshow("frame",frame)

    kInp=cv.waitKey(1000) #0msde görüntü al dediğim için açtığı an resim gibi kalıcak

    if kInp==ord("q"):
        break

vid.release()
cv.destroyAllWindows()
