import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
img = cv.imread('afa_innovation.png')
assert img is not None, "file could not be read, check with os.path.exists()"
 
blur = cv.Laplacian(img, cv.CV_64F)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Laplacian')
plt.xticks([]), plt.yticks([])
plt.show()
