# Face Detection with OpenCV

This repository contains a simple Python script that performs **face detection** using OpenCV’s Haar Cascade classifier. The script loads an image, converts it to grayscale, and detects faces by drawing bounding boxes around them.

## 📸 Features

* Reads an image from a specified path
* Converts the image to grayscale
* Uses OpenCV’s built-in Haar Cascade for frontal face detection
* Draws rectangles around detected faces
* Displays the original and processed images

## 🛠️ Requirements

Make sure you have the following installed:

```bash
pip install opencv-python
```

I ran this in **Google Colab**, so if you're doing the same, `cv2_imshow` is already available through:

```python
from google.colab.patches import cv2_imshow
```

## 📂 How It Works

1. Load an image (`visage.jpg`) from the `/content/` directory
2. Convert it to grayscale
3. Load Haar Cascade:

   ```
   haarcascade_frontalface_default.xml
   ```
4. Detect faces with `detectMultiScale()`
5. Draw green rectangles around each detected face
6. Display the result

## ▶️ Running the Script

Make sure your image exists at:

```
/content/visage.jpg
```

Then run the Python script. In Google Colab, all display windows appear inline.

## 🧪 Sample Code 

```python
import cv2
from google.colab.patches import cv2_imshow

path = "/content/visage.jpg"
img = cv2.imread(path)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 200, 23), 2)

cv2_imshow(img)
```

## 📅 Original Work Date

This script was originally created on **September 9, 2022**, in my Google Colab, as an introductory experiment with computer vision and learning about using OpenCV for face detection.

