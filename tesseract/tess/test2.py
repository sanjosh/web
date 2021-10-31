'''
https://github.com/officialsiddharthchauhan/Table-Detection-in-a-Image/blob/master/table-detect.py.py
'''
try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import pytesseract
from pytesseract import Output
import sys
import os

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
custom_config = r'--oem 3--psm 11'

def arranging_text_output(text_positions):
    list_values = [i for i in text_positions.values()]
    unique_heights = list(set(list_values))
    unique_heights.sort()
    list_values.sort()
    list_items = []
    for i in text_positions.items():
        list_items.append(i)
    dict_unique_heights = {}
    for i in unique_heights:
        dict_unique_heights.update({i:[]})

    for heights in unique_heights:
        for element in list_items:
            if(element[1]==heights):
                dict_unique_heights[heights].append(element[0])

    for i in dict_unique_heights.keys():
        for j in dict_unique_heights[i]:
            print(j, " ", end=' ')
        print('')


def binarize(image_to_transform,threshold):
    output_image = image_to_transform.convert("L")
    for x in range(output_image.width):
        for y in range(output_image.height):
            if output_image.getpixel((x,y))<threshold:
                output_image.putpixel((x,y), 0)
            else:
                output_image.putpixel((x,y), 255)
    return output_image

def colored_image(file):
    image = cv2.imread(file)
    image_file = Image.open(file)
    for thresh in range(40, 180, 10):
        print("Trying with threshold " + str(thresh))
        #display(binarize(image_file, thresh))
        # d=(pytesseract.image_to_string(binarize(Image.open(file), thresh)))
        d = pytesseract.image_to_data(image=binarize(image_file, thresh), config=custom_config, output_type=Output.DICT)
        n_boxes = len(d['text'])
        pixel_list = []
        for i in range(n_boxes):
            if (float(d['conf'][i]) > 5):
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                pixel_list.append((x, y, w, h))
        text_positions = {}
        for i in range(0, n_boxes):
            temp = {d['text'][i]: d['top'][i]}
            text_positions.update(temp)
        arranging_text_output(text_positions)


def black_and_white(file):
    image = cv2.imread(file)
    d = pytesseract.image_to_data(image, config=custom_config, output_type=Output.DICT)
    n_boxes = len(d['text'])
    pixel_list = []
    for i in range(n_boxes):
        if (float(d['conf'][i]) > 5):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            pixel_list.append((x, y, w, h))

    text_positions = {}
    for i in range(0, n_boxes):
        temp = {d['text'][i]: d['top'][i]}
        text_positions.update(temp)
    arranging_text_output(text_positions)


def show_boxes(file):
    image = cv2.imread(file)
    d = pytesseract.image_to_data(image, config=custom_config, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if (float(d['conf'][i]) > 5):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('image', image)
    cv2.waitKey(0)


# ****BELOW ARE THE OUTPUT GENERATOR FUNCTIONS USE THEM ACCORDING TO INSTRUCTION IN THE COMMENTS****#

if len(sys.argv) == 1:
    exit(1)
file = sys.argv[1]
if not os.path.exists(file):
    exit(1)

black_and_white(file)  # Use this function for black and white image.
colored_image(file)  # use this function for colored image
show_boxes(file)  # use this function to see boxes

