import cv2
import matplotlib.pyplot as plt

import numpy as np

imgnotresized=cv2.imread("remosoft.png",0)
img=cv2.resize(imgnotresized,(500,534))


plt.figure()
plt.imshow(img,cmap="gray"),plt.axis("off")
plt.show()




#erezyon
kernel=np.ones((5,5),dtype=np.uint8)
sonuc=cv2.erode(img, kernel,iterations=2)
plt.figure()
plt.imshow(sonuc,"gray")
plt.axis("off")
plt.title("erezyon uygulanmıs hal")
plt.show()

#genisleme
sonuc2=cv2.dilate(img, kernel,iterations=1) #ayni kerneli kullanabiliriz
plt.figure()
plt.imshow(sonuc2, "gray")
plt.axis("off")
plt.title("genislemis hali")
plt.show()

#acılma öncesinde beyaz gurultu olusturup acılma yapmamız gerekiyorr
# def saltPepperNoise(image):
#     row,col,ch = image.shape
#     s_vs_p = 0.5
#     amount = 0.004
#     noisy = np.copy(image)
#     # Salt mode
#     num_salt = np.ceil(amount * image.size * s_vs_p)
#     coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
#     noisy[coords] = 1
    
#     return noisy
#acılma öncesinde beyaz gurultu olusturup acılma yapmamız gerekiyorr
whitenoisy=np.random.randint(0,2,size=img.shape[:2])*255
plt.figure()
plt.imshow(whitenoisy,cmap="gray")
plt.axis("off")
plt.title("beyaz gurultulu")
plt.show()


noise_img=whitenoisy+img
plt.figure()
plt.imshow(noise_img,cmap="gray")
plt.axis("off")
plt.title("beyaz gurultulu ile birlesmis hal")
plt.show()

#acılma islemi
opening=cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN, kernel)
plt.figure()
plt.imshow(opening,cmap="gray")
plt.axis("off")
plt.title("acılmıs hali")
plt.show()


#kapanma  öncesinde siyah gurultu olusturup kapama yapmamız gerekiyorr

blacknoisy=np.random.randint(0,2,size=img.shape[:2])*-255      #siyah gürültü için sadece -255 ile carpmamız yeterli
plt.figure()
plt.imshow(blacknoisy,cmap="gray")
plt.axis("off")
plt.title("siyah gurultulu")
plt.show()


blacknoisy_img=blacknoisy+img
blacknoisy_img[blacknoisy_img<=-245]=0
plt.figure()
plt.imshow(blacknoisy_img,cmap="gray")
plt.axis("off")
plt.title("siyah gurultulu img")
plt.show()


#kapatma 

kapamaimg=cv2.morphologyEx(blacknoisy_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(kapamaimg,cmap="gray")
plt.axis("off")
plt.title("kapanmıs hali")
plt.show()



#gradient uygulama 

gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT , kernel)
plt.figure()
plt.imshow(gradient,cmap="gray")
plt.axis("off")
plt.title("gradient uygulanmis img")
plt.show()

#gradient aslında bir kenar tespiti uygulamısıdir


 
