import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
img = cv.imread('opencv_logo.png')
assert img is not None, "file could not be read, check with os.path.exists()"
 
sobel_x = cv.convertScaleAbs(cv.Sobel(img, cv.CV_64F, 1, 0))  # Detects vertical edges
sobel_y = cv.convertScaleAbs(cv.Sobel(img, cv.CV_64F, 0, 1))  # Detects horizontal edges

plt.figure(figsize=(10,5))
plt.subplot(131), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(cv.cvtColor(sobel_x, cv.COLOR_BGR2RGB)), plt.title('sobel_x detects vertical edges')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(cv.cvtColor(sobel_y, cv.COLOR_BGR2RGB)), plt.title('sobel_y detects horizontal edges')
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
