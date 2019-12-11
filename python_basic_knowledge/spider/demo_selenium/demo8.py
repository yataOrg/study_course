#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-12-04 17:53:59
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-12-04 18:14:02
# 

import cv2
import numpy as np


img = cv2.imread('./captcha_58.png',0)


while (1):
    
    if cv2.waitKey(20) & 0xFF==27:
        break
    
    edge = cv2.Canny(img, 100, 400)
    cv2.imshow('res',edge)
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
    	print("----->", cv2.contourArea(contour), cv2.arcLength(contour, True))

    print("<<<<<<<<<<<<<>>>>>>>>>>>>")

cv2.destoryAllWindows()



'''
import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('res')

cv2.createTrackbar('max','res',0,500, nothing)
cv2.createTrackbar('min','res',0,500, nothing)

img = cv2.imread('./captcha_58.png',0)

maxVal=200
minVal=100

while (1):
    
    if cv2.waitKey(20) & 0xFF==27:
        break
    maxVal = cv2.getTrackbarPos('min','res')
    minVal = cv2.getTrackbarPos('max','res')
    if minVal < maxVal:
        edge = cv2.Canny(img,100,200)
        cv2.imshow('res',edge)
    else:
        edge = cv2.Canny(img, minVal, maxVal)
        cv2.imshow('res',edge)
cv2.destoryAllWindows()
'''
