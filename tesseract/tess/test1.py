import os.path

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
from cairosvg import svg2png
from io import BytesIO
'''

https://answers.opencv.org/question/63847/how-to-extract-tables-from-an-image/
https://groups.google.com/g/tesseract-ocr/c/1244AQNB9tI

https://github.com/officialsiddharthchauhan/Table-Detection-in-a-Image/blob/master/table-detect.py.py
https://github.com/eihli/image-table-ocr
'''


if len(sys.argv) == 1:
    exit(1)
file = sys.argv[1]
if not os.path.exists(file):
    exit(1)

# print(cv2.getBuildInformation())

CV_LOAD_IMAGE_GRAYSCALE = 0
CV_LOAD_IMAGE_COLOR = 1

table_image_contour = cv2.imread(file, CV_LOAD_IMAGE_GRAYSCALE)
table_image = cv2.imread(file, CV_LOAD_IMAGE_COLOR)

ret, thresh_value = cv2.threshold(
    table_image_contour, 180, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
dilated_value = cv2.dilate(thresh_value, kernel, iterations=1)

contours, hierarchy = cv2.findContours(
    dilated_value, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
# bounding the images
if y < 700:
    table_image = cv2.rectangle(table_image, (x, y), (x + w, y + h), (0, 0, 255), 1)

plt.imshow(table_image)
plt.show()

cv2.imwrite(r'../resources/generated_image1.jpg', table_image)

### MISC

# Preprocessing for pytesseract
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
