# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:30:17 2021

@author: Aditya Manwar
"""

from pyaadhaar.utils import Qr_img_to_text
from pyaadhaar.deocde import AadhaarOldQr
from pyaadhaar.deocde import AadhaarSecureQr

# reading the image file and getting the data in the QRCODE
data = (Qr_img_to_text("secure.JPG"))

#If unsecure
if data[0][0] == '<':
    obj  = AadhaarOldQr(data[0])
    data1 = obj.decodeddata()
    name = data1['name']
    uid = data1['uid']
    dob = data1['dob']
    address = data1['loc'] + ' ' + data1['lm']+' ' + data1['dist'] + data1['state']
    pincode = data1['pc']
    co = data1['co']
    gender = data1['gender']

#if secure   
else:
    obj  = AadhaarSecureQr(int(data[0]))
    data1 = obj.decodeddata()
    name = data1['name']
    refid = data1['referenceid']
    dob = data1['dob']
    address = data1['location'] + ' ' + data1['landmark']+' ' + data1['district'] + data1['state']
    pincode = data1['pincode']
    co = data1['careof']
    gender = data1['gender']
    image = obj.image()
    """
    #verifying the emailid or phone number for KYC
    obj.verifyEmail("example@gmail.com"))
    obj.verifyMobileNumber(9999999999))
    """