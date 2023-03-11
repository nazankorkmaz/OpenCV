
import cv2 as cv


cap= cv.VideoCapture("pixabay.mp4")

if cap.isOpened()==False:
    print("videoyaya erişilemiyor")

while cap.isOpened():
    #capture frame by frame
    ret,frame = cap.read()

    if ret==True: #ret dosya açılabildi miyi kontrol eder 1 döner açılırsa
        cv.imshow("frame",frame)
      

        kInp=cv.waitKey(24) #24 görüntü alır 1snde??
        
        if kInp==ord("q"):
            break
    
    else:break

cap.release()
cv.destroyAllWindows()
