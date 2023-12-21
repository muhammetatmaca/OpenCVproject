import cv2
import numpy as np

img=cv2.imread("lorem.png")


hor=np.hstack((img,img))
cv2.imshow("birlestirme horizantal", hor)

ver=np.vstack((img,img))
cv2.imshow("birlestirme", ver)

