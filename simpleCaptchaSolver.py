# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:23:00 2021

@author: Aditya Manwar
"""
import numpy as np
import cv2
from PIL import Image
import pytesseract
from matplotlib import pyplot as plt
import imutils

image = cv2.imread("check.JPG")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray, img_bin = cv2.threshold(gray,120,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(gray, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
out_below = pytesseract.image_to_string(img,lang='eng', config='--psm 6 --oem 3 -c --tessdata-dir="C:/Program Files/Tesseract-OCR/tessdata"')
