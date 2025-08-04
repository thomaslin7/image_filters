import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv.imread('afa_innovation.png')
assert img is not None, "file could not be read, check with os.path.exists()"

# Add salt-and-pepper noise (50% of pixels corrupted)
def add_salt_pepper_noise(image, amount=0.5):
    noisy = image.copy()
    total_pixels = image.shape[0] * image.shape[1]
    num_salt = int(amount * total_pixels / 2)
    num_pepper = int(amount * total_pixels / 2)

    # Salt noise
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = [255, 255, 255]

    # Pepper noise
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = [0, 0, 0]

    return noisy

# Add noise
noisy_img = add_salt_pepper_noise(img, amount=0.5)

# Apply median blur
median = cv.medianBlur(noisy_img, 5)

# Show results
plt.figure(figsize=(10,5))
plt.subplot(131), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(cv.cvtColor(noisy_img, cv.COLOR_BGR2RGB)), plt.title('Noisy (Salt & Pepper)')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(cv.cvtColor(median, cv.COLOR_BGR2RGB)), plt.title('Median Blurred')
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
