import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)  #matris ile siyah resim olusturma

#cv2.imshow("matris siyahi", img)


cv2.line(img, (0,0), (512,512),(255,255,255),3)

#cv2.imshow("matris cizgi", img)


cv2.rectangle(img, (40,40),(170,170),(0,255,0),3)
cv2.rectangle(img, (210,210),(330,330),(0,255,0),cv2.FILLED)
cv2.rectangle(img, (379,370),(500,500),(0,255,0),3)

#cv2.imshow("kare", img)

cv2.circle(img, (256,256), 8,(0,0,255),3)

#cv2.imshow("cember", img)


cv2.putText(img, "openCV",(300,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
cv2.imshow("text", img)
