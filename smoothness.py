import cv2
import numpy as np
from matplotlib import pyplot as plt

# you can change the image name here
img = cv2.imread('v1.jpg')

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Smoothened Image')
plt.xticks([]), plt.yticks([])
plt.show()
