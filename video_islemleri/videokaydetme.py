import cv2 as cv

vid= cv.VideoCapture(0)

w=int(vid.get(3))#float gelir bu değerler bu width parametresini alır
h=int(vid.get(4)) #bu da heightını alır

size=(w,h)

result=cv.VideoWriter("record.avi",cv.VideoWriter_fourcc(*"XVID"),24,size) #yazmayı yaoıcak ve fourcc kendi içinde otomatik değer atıuor galiba sıkıştırma pixel falan için

"""
Videoyu yazmak için 5 adet parametreye ihtiyacı vardır, bu parametreler; 
videonun kaydedileceği dizin, codec,  frame boyutu (genişlik, yükseklik), 
fps değeri ve videonun renkli mi yoksa siyah beyaz mı kayıt edileceğini belirten boolean bir bayrak değişken.
"""

while True:
    ret, frame= vid.read() #kareleri yakalar

    if ret== True:
        result.write(frame)
        cv.imshow("frame",frame)
        
        kInp=cv.waitKey(1)
        if kInp== ord("q"):
            break
    else:
        break

vid.release() #serbest bırakma
result.release() #geçici bellekte kaplanan alan da boşaltılıyor
cv.destroyAllWindows()