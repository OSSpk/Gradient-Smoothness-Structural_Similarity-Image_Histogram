# import the necessary packages
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import compare_ssim as ssim


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar" the two images are
    return err


# you can change the image names here
# NOTE: first resize the images to equal sizes [using some online tool]
img1 = cv2.imread("images/f1_equal.jpeg")
img2 = cv2.imread("images/v1_equal.jpeg")

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4),
                         sharex=True, sharey=True,
                         subplot_kw={'adjustable': 'box-forced'})

mse_1 = mse(img1, img1)
ssim_1 = ssim(img1, img1, multichannel=True)

mse_2 = mse(img1, img2)
ssim_2 = ssim(img1, img2, multichannel=True)

label = 'MSE: {:.2f}, SSIM: {:.2f}'

axes[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB), vmin=0, vmax=1)
axes[0].set_xlabel(label.format(mse_1, ssim_1))
axes[0].set_title('Figure 1')

axes[1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB), vmin=0, vmax=1)
axes[1].set_xlabel(label.format(mse_2, ssim_2))
axes[1].set_title('Figure 2')

plt.show()
