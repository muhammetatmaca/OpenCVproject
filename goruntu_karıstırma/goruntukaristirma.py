import cv2
import matplotlib.pyplot as plt

img1notresized=cv2.imread("foto1.jpg")
img1notresized=cv2.cvtColor(img1notresized, cv2.COLOR_BGR2RGB)

img2notresized=cv2.imread("foto2.jpg")
img2notresized=cv2.cvtColor(img2notresized, cv2.COLOR_BGR2RGB)

img1=cv2.resize(img1notresized, (178,167))
img2=cv2.resize(img2notresized,(178,167))

#plt.figure()
#plt.imshow(img1) #imshow edilen foto rgb degil bgr formatında

#plt.figure()
#plt.imshow(img2)

blend=cv2.addWeighted(src1=img1,alpha=0.5,src2=img2,beta=0.5,gamma=0.5)
plt.figure()
plt.imshow(blend)    