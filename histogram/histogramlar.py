import cv2
import matplotlib.pyplot as plt
import numpy as np

img1=cv2.imread("yellow_black.png")
img1_rgb=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img1_rgb,cmap="gray")
plt.axis("off")
plt.title("rgb fotom")
plt.show()

print(img1.shape)
#normalde köseli paranteze almadıgımız degerleri bu sefer aldık cünkü hesap icin yapılacak bu islem [] liste degiskeni olarak alınacak ezbere yapmaaa!
img1_histogram=cv2.calcHist([img1], channels=[0],mask=None, histSize=[256], ranges=[0,256]) 
print(img1_histogram.shape)
plt.figure()
plt.plot(img1_histogram)

color=("b","g","r")
plt.figure()

for i,c in enumerate(color): #b nin indeksini i ye b nin stringini c ye esitliyor v dönüyor
    hist=cv2.calcHist([img1], channels=[i],mask=None, histSize=[256], ranges=[0,256]) 
    plt.plot(hist, c)
    
    
m_picchu=cv2.imread("machapicchu.jpg")
m_picchu_rgb=cv2.cvtColor(m_picchu, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(m_picchu_rgb,cmap="gray")
plt.title("m_picchu rgb")
plt.show()

print(m_picchu_rgb.shape)

mask=np.zeros(m_picchu_rgb.shape[:2],np.uint8)
plt.figure()
plt.imshow(mask,cmap="gray")

mask[200:500,600:900]=255
plt.figure(),plt.imshow(mask,cmap="gray")


masked_img_vis=cv2.bitwise_and(m_picchu_rgb,m_picchu_rgb,mask=mask)

plt.figure()
plt.imshow(masked_img_vis,cmap="gray")

masked_img=cv2.bitwise_and(m_picchu, m_picchu,mask=mask)
plt.figure()
plt.imshow(masked_img,cmap="gray")

histogt=cv2.calcHist([masked_img], channels=[0],mask=mask, histSize=[256], ranges=[0,256]) 
plt.figure(),plt.plot(histogt)



#histogram esitleme islemi

imghistv1=cv2.imread("hist_equ.jpg",0)
plt.figure(),plt.imshow(imghistv1,cmap="gray")

imghistv2=cv2.calcHist([imghistv1], channels=[0],mask=None, histSize=[256], ranges=[0,256]) 
plt.figure(),plt.plot(imghistv2)

eq_hist=cv2.equalizeHist(imghistv1)
plt.figure(),plt.imshow(eq_hist,cmap="gray")

eq_hist_img=cv2.calcHist([eq_hist], channels=[0],mask=None, histSize=[256], ranges=[0,256]) 
plt.figure(),plt.plot(eq_hist_img)



