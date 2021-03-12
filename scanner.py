# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:32:26 2021

@author: Aditya Manwar
"""

import cv2
from pyzbar import pyzbar
from PIL import Image
from pyzbar.pyzbar import ZBarSymbol
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample1.png')

#img2 =cv2.imread('Sample.png')


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
detector = cv2.QRCodeDetector()
data, bbox, qr = detector.detectAndDecode(img)
"""

gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


qrcode = pyzbar.decode(img)
for qrcod in qrcode:
    x,y,w,h = qrcod.rect
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
    qdata = qrcod.data.decode("utf-8")
    qtype = qrcod.type
    text = f"{qdata},{qtype}"
    cv2.putText(img,text,(x,y-10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.5,(0,255,0),1)
"""
qrcode2 = pyzbar.decode(img2)
for qrcod in qrcode2:
    x,y,w,h = qrcod.rect
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),4)
    qdata = qrcod.data.decode("utf-8")
    qtype = qrcod.type
    text = f"{qdata},{qtype}"
    cv2.putText(img2,text,(x,y-10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.5,(0,255,0),1)
"""    
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
