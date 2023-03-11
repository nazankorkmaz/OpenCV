#renkleri tersine çevirme
import cv2 as cv
img= cv.imread("opencv.png")
cv.namedWindow("img",cv.WINDOW_AUTOSIZE)

h ,w ,ch = img.shape #yükseklik, yatay ve kanal sayılarını aldık
print("h, w, ch",h,w,ch)

for row in range(h):
    for col in range(w):
        b, g, r= img[row,col] #rgb kodunu aldık her bir pikselin
        b=255-b
        g=255-g
        r=255-r
        img[row,col]=[b,g,r]


cv.imshow("output",img)
cv.waitKey(0)
cv.destroyAllWindows()