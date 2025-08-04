import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
img = cv.imread('afa_innovation.png')
assert img is not None, "file could not be read, check with os.path.exists()"
 
blur = cv.GaussianBlur(img,(21,21),50) # kernel size used for blurring

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
