import cv2 as cv

img=cv.imread("opencv.png")

#item    
#koordinatlardaki hangi rengin ne kadar değerde olduğunu verir
#img.item(y,x,color) color RGB 210 ile verilir

print("Blue ",img.item(10,10,0))
print("green ",img.item(200,200,1))
print("red ",img.item(10,10,2))

print(img[200,200]) #2.gösterim

#itemset
#oradaki rengi değiştirebiliyorsun
#img.itemset((y,x,color),value)

for y in range(50):
    for x in range(50):
        img.itemset((y,x,0),0)
        img.itemset((y,x,1),0)
        img.itemset((y,x,2),0)  #siyah olacak hepsi 50pxlik yer başlangıçtan
        #img[y,x]=[0,0,0] 2.gösterim


#shape
#boyutlarını ve kaç renk var onu verir
print(img.shape)
y,x,c=img.shape
print("x: ",x,"y: ",y)


#datatype
print(img.dtype) #uint8 yani unsigned int tipinde değer olduğunu verir


#ROI
#bir yeri kesip yapıştırabilirsin
#roi=img[y1:y2, x1:x2]

roi=img[100:110, 45:60]
cv.imshow("f",roi)
img[200:210,190:205]=roi #yapıştırdım



#renk filtresi
#img[:,:,0]=0 gibisinden

img[:,:,0]=255 #maviyi fulledi (b,g,r) eşitliğiyle de yapılabilir
#img[:,:,1]=255
#img[:,:,2]=255

cv.imshow("a",img)
cv.waitKey(0)
cv.destroyAllWindows()