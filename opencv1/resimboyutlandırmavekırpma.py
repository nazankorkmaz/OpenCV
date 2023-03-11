import cv2 as cv

img=cv.imread("roket.jpg")
print("original size: ",img.shape)

imgResized=cv.resize(img,(150,250))
print("resized size: ",imgResized.shape)

y, x,c=img.shape
imgResized2=cv.resize(img,(x+x//2,y+y//2))

cv.imshow("resized",imgResized)
cv.imshow("2resized",imgResized2)
cv.imshow("original",img)


imgCropped=img[50:160,70:150]
cv.imshow("cropped",imgCropped)

imgCropped2=img[0:y//2,0:x//2] #4te 1i aldık
cv.imshow("2cropped",imgCropped2)


cv.waitKey(0)
cv.destroyAllWindows()
