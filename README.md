

## ⚙️ How It Works

1. Convert video frame to **grayscale**
2. Apply **Gaussian blur** to reduce noise
3. Use **Canny edge detection**
4. Define **region of interest (ROI)** to mask unwanted parts
5. Apply **Hough Line Transform** to detect straight lines
6. **Average and extrapolate** the left/right lane lines
7. Overlay detected lanes onto the original frame

## 🎥 Input vs Output Video




### 🔹 Original Input Video  



<video src="https://github.com/user-attachments/assets/dcae71c1-20ef-4f15-9829-aaebfd1a88b4
" width="400" controls></video>

### 🔸 Output Video with Lane Detection  
<video src="https://github.com/user-attachments/assets/26a92fd8-fa6a-4581-b0c5-3ac7790414dd
" width="400" controls></video>






##  Technologies Used

- Python 3
- OpenCV
- NumPy

## 📦 Requirements

```bash
opencv-python
numpy
```
