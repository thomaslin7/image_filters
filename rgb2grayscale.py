import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('boxer.png')
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

plt.imshow(grayscale, cmap='gray')  # Display grayscale correctly
plt.title('Grayscale Image')
plt.axis('off')
plt.show()
