

## ⚙️ How It Works

1. Convert video frame to **grayscale**
2. Apply **Gaussian blur** to reduce noise
3. Use **Canny edge detection**
4. Define **region of interest (ROI)** to mask unwanted parts
5. Apply **Hough Line Transform** to detect straight lines
6. **Average and extrapolate** the left/right lane lines
7. Overlay detected lanes onto the original frame


##  Technologies Used

- Python 3
- OpenCV
- NumPy

## 📦 Requirements

```bash
opencv-python
numpy
```
