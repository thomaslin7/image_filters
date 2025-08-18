import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load the image and convert to grayscale
img = cv.imread('boxer.png')
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Display grayscale image
plt.imshow(grayscale, cmap='gray')
plt.title('Grayscale Image with Grids')
plt.axis('off')

# Image shape
nrows, ncols = grayscale.shape
step = 1  # 1x1 blocks

# Draw vertical grid lines every 1 pixel
for x in range(0, ncols + 1, step):
    plt.axvline(x - 0.5, color='white', linewidth=0.5)

# Draw horizontal grid lines every 1 pixel
for y in range(0, nrows + 1, step):
    plt.axhline(y - 0.5, color='white', linewidth=0.5)

plt.show()
