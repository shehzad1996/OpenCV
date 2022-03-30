#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 22:39:25 2022

@author: user
"""


# This programs calculates the orientation of an object.
# The input is an image, and the output is an annotated image
# with the angle of otientation for each object (0 to 180 degrees)
 
import cv2 as cv
from math import atan2, cos, sin, sqrt, pi
import numpy as np
 
# Load the image
img = cv.imread("/Users/user/Desktop/angle2.png")
 
#img1 = Image.open("/Users/user/Desktop/angle2.png")

#img1.size
# Was the image there?
if img is None:
  print("Error: File not found")
  exit(0)
 
#cv.imshow('Input Image', img)
 
# Convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 
# Convert image to binary
_, bw = cv.threshold(gray, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
 
# Find all the contours in the thresholded image
_,contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
 
contours.index

area_ls =[]
#contours=contours[0:1]
for i, c in enumerate(contours):
    area = cv.contourArea(c)
    if area < 3700 or 300000 < area:
      continue
    area = cv.contourArea(c)
    area_ls.append(area)
    
myarea = max(area_ls)

for i, c in enumerate(contours):
    
    # Calculate the area of each contour
    area = cv.contourArea(c)
    
    # Ignore contours that are too small or too large
    if area < 3700 or 100000 < area:
      continue

    
    if area == myarea:#draw rectangle only for the largest contour
            
        # cv.minAreaRect returns:
        c1 = c.copy()
        # (center(x, y), (width, height), angle of rotation) = cv2.minAreaRect(c)
        rect = cv.minAreaRect(c)
        
        box = cv.boxPoints(rect)
        
        box = np.int0(box)
           
        # Retrieve the key parameters of the rotated bounding box
        center = (int(rect[0][0]),int(rect[0][1])) 
        width = int(rect[1][0])
        height = int(rect[1][1])
        angle = int(rect[2])
           
           
        if width < height:
          angle = 90 - angle
        else:
          angle = -angle
               
        label = "  Rotation Angle: " + str(angle) + " degrees"
        textbox = cv.rectangle(img, (center[0]-35, center[1]-25), 
          (center[0] + 295, center[1] + 10), (255,255,255), -1)
        cv.putText(img, label, (center[0]-50, center[1]), 
          cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 1, cv.LINE_AA)
        cv.drawContours(img,[box],0,(0,0,255),2)
           

# Save the output image to the current directory
cv.imwrite("min_area_rec_output.jpg", img)



x,y,w,h = cv2.boundingRect(c1)
#cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# center line
cv2.line(img, (x+w//2, y), (x+w//2, y+h), (0, 0, 255), 2)
# below circle to denote mid point of center line
center = (x+w//2, y+h//2)
radius = 2
cv2.circle(img, center, radius, (255, 255, 0), 2)


cv.imwrite("min_area_rec_output.jpg", img)
