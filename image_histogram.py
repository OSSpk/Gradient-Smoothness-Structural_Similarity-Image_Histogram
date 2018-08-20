import cv2
import matplotlib.pyplot as plt  # import pyplot as plt
import numpy as np

plt.style.use("seaborn-whitegrid")

# you can change image name here
img = cv2.imread('v1.jpg')

color = ('b', 'g', 'r')

hists = []
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.xlabel("Intensity Value", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(fontsize=12)
plt.title('Image Histogram')
plt.yticks(fontsize=12)
plt.show()
