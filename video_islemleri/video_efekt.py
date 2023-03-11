import cv2 as cv

capture= cv.VideoCapture(0)
height=capture.get(cv.CAP_PROP_FRAME_HEIGHT) #Video akışındaki karelerin yüksekliği.
width=capture.get(cv.CAP_PROP_FRAME_WIDTH) #Video akışındaki karelerin genişliği.
count=capture.get(cv.CAP_PROP_FRAME_COUNT)  #Video dosyasındaki kare sayısı.
fps=capture.get(cv.CAP_PROP_FPS)        #Kare hızı.

#get---->Belirtilen VideoWriter özelliğini döndürür.

print(height,width,count,fps)

def process(image,opt=1):
    dst=None
    if opt==0:
        dst=cv.bitwise_not(image)  #tersine çevir
    if opt==1:
        dst=cv.GaussianBlur(image,(0,0),10) # bulanıklaştır new size 10dan ileriye
    if opt==2:
        dst=cv.Canny(image,100,200) #kenarları belirle
    return dst

index =0
while True:
    ret,frame=capture.read()
    if ret is True:
        cv.imshow("video-input",frame)
        c=cv.waitKey(50)
        if c>=49:
            index=c-49
        result=process(frame,index)
        cv.imshow("result",result)

        if c==27:
            break
    else:
        break

cv.waitKey(1)