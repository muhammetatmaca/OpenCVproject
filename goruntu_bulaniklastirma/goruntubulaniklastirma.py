import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")



imgnotresized = cv2.imread("NYC.jpg")

img=cv2.resize(imgnotresized,(543,543))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orjinal Görüntü")


dst2 = cv2.blur(img, ksize = (3,3))
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("Ortalama Bulanıklaştırma")


gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gauss Bulanıklaştırma")



mb = cv2.medianBlur(img, ksize = 3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Medyan Bulanıklaştırma")

def gaussianNoise(image):
    
    row,col,ch= image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
  
    return noisy

img = cv2.imread("NYC.jpg")
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")

gaussianNoisyImage = gaussianNoise(img)
plt.figure()
plt.imshow(gaussianNoisyImage)
plt.axis("off")
plt.title("Image with Gaussian Noise")

spImage = saltPepperNoise(img)
plt.figure()
plt.imshow(spImage)
plt.axis("off")
plt.title("Image with Salt and Pepper Noise")


# gaussian blurring
gb = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Image with Gaussian Blurring")

# median blurring
mb = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Image with Median Blurring")
    
    






        
    



