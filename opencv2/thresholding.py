import cv2 as cv

src=cv.imread("opencv.png")

T=127

gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)

for i in range(5):
    ret, binary= cv.threshold(src, T, 255, i)  #src yerğne gray de koyabilirsin
    cv.imshow("binary_"+str(i),binary)

cv.waitKey(0)
cv.destroyAllWindows()