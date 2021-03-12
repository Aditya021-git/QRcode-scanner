# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:17:31 2021

@author: Aditya Manwar
"""


import cv2
from pyzbar import pyzbar
import numpy as np

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()
    
    decodedObj = pyzbar.decode(frame)
    for obj in decodedObj:
        print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50,50), font, 3, (255,0,0),3)
    
    cv2.imshow('Frame',frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break