# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pikepdf


a=pikepdf.open('C:/Users/Aditya Manwar/Downloads/Eaadhar.pdf',password='ADIT1999')

a.save('C:/Users/Aditya Manwar/Downloads/Eaadhar1.pdf')
b = a.pages[0]
 
import fitz

doc = fitz.open('C:/Users/Aditya Manwar/Downloads/Eaadhar1.pdf')
page = doc[0]

c= page.get_pixmap()
d= page.get_text()

list = list(map(str,d.split('\n')))
