import cv2
import matplotlib.pyplot as plt



img1=cv2.imread("sudoku1.png",0)
plt.figure()
plt.imshow(img1,cmap="gray")
plt.axis("off")
plt.show()


# x gradyanları

sobelx=cv2.Sobel(img1, ddepth=cv2.CV_16S, dx=1, dy=0,ksize=5)
plt.figure()
plt.imshow(sobelx,cmap="gray")
plt.title("x gradyans")
plt.axis("off")
plt.show()

#y gradyanları

sobely=cv2.Sobel(img1, ddepth=cv2.CV_16S, dx=0, dy=1,ksize=5)
plt.figure()
plt.imshow(sobely,cmap="gray")
plt.title("y gradyans")
plt.axis("off")
plt.show()

#x ve y beraber

lablas=cv2.Laplacian(img1, ddepth=cv2.CV_16S)
plt.figure()
plt.imshow(lablas,cmap="gray")
plt.title("X Y gradyans")
plt.axis("off")
plt.show()





