import cv2
import numpy as np

img=cv2.imread("bozukperspektif.png")
cv2.imshow("normalhal", img)

width=400
height=500

pts1=np.float32([[159,4],[38,255],[321,78],[200,332]])
pts2=np.float32([[0,0],[0,height],[width,0],[width,height]])


matris=cv2.getPerspectiveTransform(pts1,pts2)
img2=cv2.warpPerspective(img,matris,(width,height))
cv2.imshow("duzeltilmis hali",img2)