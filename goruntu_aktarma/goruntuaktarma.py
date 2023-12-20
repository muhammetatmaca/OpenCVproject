import cv2


#içe aktarma 

img=cv2.imread("yol_resmi.jpg",0)#0 grayscale olarak aktarmamızı sagliyor
cv2.imshow("ilk resim",img)



k=cv2.waitKey(0) &0xFF

if k==32:
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("gray_yol.png", img)
    cv2.destroyAllWindows()

    