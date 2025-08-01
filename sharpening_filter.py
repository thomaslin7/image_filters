import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv.imread('opencv_logo.png')
assert img is not None, "Image file not found"

# Define sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

# Apply sharpening filter
sharpened = cv.filter2D(img, -1, kernel)

# Show images
plt.figure(figsize=(10,5))
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv.cvtColor(sharpened, cv.COLOR_BGR2RGB)), plt.title('Sharpened')
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
