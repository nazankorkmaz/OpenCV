import cv2 as cv

img=cv.imread("opencv.png",0)

cv.imshow("opencv",img)

kInp=cv.waitKey(0)
print(kInp)

if kInp== ord("a"): #kInp == 97:   İşlev ord(), Unicode karakterini temsil eden bir tamsayı döndürür
    print("a tuşuna basıldı")
else:
    print("başka bir tuşa basıldı")

#cv.waitKey(0)
cv.destroyAllWindows()