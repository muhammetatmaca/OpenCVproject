import cv2

img=cv2.imread("lorem.png",0)

resimboyutu=img.shape
cv2.imshow("boyutlandirmamis hali",img)

imgResized=cv2.resize(img,(800,800))
cv2.imshow("resiz edilmis hali",imgResized)  #0x0 full ekran için yazılır

imgCropped=img[:200,:200]
cv2.imshow("kirpilmis foto", imgCropped)


