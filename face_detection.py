# Importing OpenCV package
import cv2
from google.colab.patches import cv2_imshow
# Reading the image


import os

# Download a random picture, preferably a headshot to view detection results, and name the picture visage with .jpg extension
path = "/content/visage.jpg"
if os.path.exists(path):
  img = cv2.imread(path)
  print(img)

else:
  print("Path does not exist:", path)

cv2_imshow(img)
cv2.waitKey(0)

# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Applying the face detection method on the grayscale image
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

# Iterating through rectangles of detected faces
for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 200, 23), 2)

cv2_imshow(img)

cv2.waitKey(0)
