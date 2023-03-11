
import cv2 as cv

path="opencv.png"

img= cv.imread(path )

cv.namedWindow("colored",cv.WINDOW_AUTOSIZE)
cv.imshow("colored",img)
cv.waitKey(1000)
cv.destroyAllWindows()


#dönüştürmek istediğimiz format ve adını verelim 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(1000)

#kaydedelim yeni görseli

cv.imwrite("gray_opencv.png",gray)
cv.destroyAllWindows()


#hiç yukarıdaki gibi yapmadan direk resmi griye çevirmeyi
#nasıl yapardık--

img2=cv.imread(path, cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray2",cv.WINDOW_AUTOSIZE)
cv.imshow("gray2",img2)
cv.waitKey(1000)
cv.destroyAllWindows()



