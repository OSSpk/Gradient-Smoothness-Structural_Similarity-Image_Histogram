import cv2
from matplotlib import pyplot as plt


# You can change the image name here
img = cv2.imread('images/v1.jpg', 0)


laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
plt.subplot(1, 2, 1), plt.imshow(img, cmap=plt.cm.gray)
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(laplacian, cmap=plt.cm.gray)
plt.title('Gradient'), plt.xticks([]), plt.yticks([])

plt.show()
