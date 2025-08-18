# Computer Vision Fundamentals: Image Filters

A comprehensive collection of image filtering techniques using 2D convolution and various kernels. This repository serves as an educational resource for understanding fundamental computer vision concepts, particularly image filtering and convolution operations.

## 🎯 Learning Objectives

This repository demonstrates:
- **2D Convolution Operations**: Understanding how kernels slide over images
- **Different Filter Types**: Blurring, sharpening, edge detection, and noise reduction
- **Kernel Design**: How different kernel matrices produce different effects
- **Practical Applications**: Real-world use cases for each filter type

## 📚 Table of Contents

1. [Fundamentals](#-fundamentals)
2. [Filter Types](#-filter-types)
   - [Averaging Filter](#averaging-filter)
   - [Gaussian Filter](#gaussian-filter)
   - [Median Filter](#median-filter)
   - [Sharpening Filter](#sharpening-filter)
   - [Laplacian Filter](#laplacian-filter)
   - [Sobel Filter](#sobel-filter)
3. [Running the Examples](#-running-the-examples)
4. [Homework](#-homework)

## 🔬 Fundamentals

### What is Image Filtering?

Image filtering is a fundamental operation in computer vision where we apply mathematical operations to modify pixel values based on their neighbors. This is typically done using **convolution** - sliding a small matrix (called a **kernel** or **filter**) over the image.

### Convolution Process

1. **Kernel Placement**: Place the kernel over a region of the image
2. **Element-wise Multiplication**: Multiply corresponding elements
3. **Summation**: Sum all products to get the new pixel value
4. **Sliding**: Move the kernel to the next position and repeat

```
Kernel: [1/9  1/9  1/9]
        [1/9  1/9  1/9]
        [1/9  1/9  1/9]

This creates a 3x3 averaging filter
```

## 🎨 Filter Types

### Averaging Filter

**File**: `averaging_filter.py`

**Purpose**: Smoothing/blurring images by averaging pixel values in a neighborhood.

**Kernel**: Uniform weights (all elements equal)
```python
# 25x25 averaging kernel
averaging = cv.blur(img, (25, 25))
```

**Applications**:
- Noise reduction
- Pre-processing for other operations
- Creating soft, blurred effects

### Gaussian Filter

**File**: `gaussian_filter.py`

**Purpose**: Smoothing with weighted averaging based on Gaussian distribution.

**Kernel**: Gaussian weights (center pixels have higher influence)
```python
# Gaussian blur with 21x21 kernel, sigma=10
gaussian = cv.GaussianBlur(img, (21, 21), 10)
```

**Applications**:
- Advanced noise reduction
- Pre-processing for edge detection
- Creating natural-looking blur effects

### Median Filter

**File**: `median_filter.py`

**Purpose**: Noise reduction, especially effective against salt-and-pepper noise.

**Kernel**: Replaces each pixel with the median value of its neighborhood
```python
# 5x5 median filter
median = cv.medianBlur(noisy_img, 5)
```

**Applications**:
- Salt-and-pepper noise removal
- Preserving edges while reducing noise
- Medical imaging preprocessing

### Sharpening Filter

**File**: `sharpening_filter.py`

**Purpose**: Enhancing image details and edges.

**Kernel**: High-pass filter that emphasizes differences
```python
# Define sharpening kernel
kernel = np.array([[0, -1, 0],
                  [-1, 5,-1],
                  [0, -1, 0]])

# Apply sharpening filter
sharpened = cv.filter2D(img, -1, kernel)

```

**Applications**:
- Image enhancement
- Detail recovery after blurring
- Pre-processing for feature detection

### Laplacian Filter

**File**: `laplacian_filter.py`

**Purpose**: Edge detection using second-order derivatives.

**Kernel**: A filter that detects rapid intensity changes
```python
# Laplacian edge detection
laplacian = cv.Laplacian(img, cv.CV_64F)
```

**Applications**:
- Edge detection
- Zero-crossing detection
- Image segmentation

### Sobel Filter

**File**: `sobel_filter.py`

**Purpose**: Directional edge detection using first-order derivatives.

**Kernel**: Separate kernels for horizontal and vertical edges
```python
# Detects vertical edges
sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0)

# Detects horizontal edges
sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1)
```

**Applications**:
- Directional edge detection
- Gradient magnitude and direction
- Feature extraction

## 🚀 Running the Examples

### Prerequisites

```bash
pip install opencv-python numpy matplotlib
```

### Execution

Each filter can be run independently:

```bash
python averaging_filter.py
python gaussian_filter.py
python median_filter.py
python sharpening_filter.py
python laplacian_filter.py
python sobel_filter.py
```

### Expected Output

Each script will display:
- **Original Image**: The input image
- **Filtered Image**: The result after applying the filter
- **Comparison**: Side-by-side or multi-panel visualization

## 📝 Homework

Complete the following tasks to practice 2D convolution and classic image filters. Aim to finish in 60–90 minutes.

### Instructions

- Use `afa_innovation.png` (or your own image) as input.
- Install dependencies if needed: `pip install opencv-python numpy matplotlib`.
- Save intermediate results to a `results/` folder (create if missing).

### Tasks

1. Grayscale Conversion (5–10 min)
   - Convert the input image to grayscale using `rgb2grayscale.py` or OpenCV's `cv.cvtColor(img, cv.COLOR_BGR2GRAY)`.
   - Save as `results/grayscale.png`.

2. Blur Comparison: Averaging vs Gaussian (10–15 min)
   - Apply an averaging blur and a Gaussian blur with the same kernel size (e.g., 21×21).
   - Keep sigma for Gaussian reasonable (e.g., 10).
   - Save as `results/avg_blur.png` and `results/gauss_blur.png`.
   - Write 2–3 sentences comparing visual differences (edges, artifacts, smoothness).

3. Salt-and-Pepper Noise + Median Filtering (10–15 min)
   - Add salt-and-pepper noise to the grayscale image (e.g., 1–2% pixels flipped to 0 or 255).
   - Denoise using a median filter (e.g., 5×5) in `median_filter.py`.
   - Save `results/noisy.png` and `results/median_denoised.png`.
   - Briefly note why median performs better than averaging for this noise type.

4. Edge Detection: Sobel vs Laplacian (15–20 min)
   - Use `sobel_filter.py` to compute `sobel_x` and `sobel_y`; combine with magnitude `sqrt(sobel_x^2 + sobel_y^2)`.
   - Use `laplacian_filter.py` to compute Laplacian edges.
   - Optionally threshold both to produce binary edge maps.
   - Save `results/sobel_edges.png` and `results/laplacian_edges.png`.

5. Sharpening After Blur (10–15 min)
   - Slightly blur the original image (Gaussian, small kernel like 7×7), then apply `sharpening_filter.py`.
   - Compare with sharpening applied directly to the original.
   - Save `results/sharp_after_blur.png` and `results/sharp_direct.png`.
   - Note which looks better and why (ringing, noise amplification, edge clarity).

### Deliverables

- Images saved under `results/` for each task as specified.
- A short `HOMEWORK.md` (5–8 bullet points) summarizing:
  - Parameters used (kernel sizes, sigma, thresholds)
  - 2–3 insights from each comparison (blur vs blur, edges, sharpening)
  - Any challenges or questions

### Optional Challenge (if time permits)

- Build a simple pipeline: grayscale → Gaussian blur → Sobel magnitude → threshold. Save as `results/pipeline_edges.png`.
- Create a 2×3 figure comparing all outputs in one grid (e.g., using matplotlib or `draw_grids.py`).

---

**Happy Learning!** 🎯

*This repository serves as a foundation for understanding image processing fundamentals in computer vision and robotics applications.*
