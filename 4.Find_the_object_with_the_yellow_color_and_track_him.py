import numpy as np
import argparse
import cv2

colorLower = (24, 100, 100)
colorUpper = (44, 255, 255)
camera = cv2.VideoCapture(0)
while True:
 count=0  
 (grabbed, frame) = camera.read()
 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 mask = cv2.inRange(hsv, colorLower, colorUpper)
 mask = cv2.erode(mask, None, iterations=2)
 mask = cv2.dilate(mask, None, iterations=3)
 cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

 lengh_cnts=len(cnts)
 amount_figure= [1.0] *lengh_cnts 
 amount_axeX= [1.0] *lengh_cnts
 amount_axeY= [1.0] *lengh_cnts 

 for c in cnts:  
  
  ((x, y), radius) = cv2.minEnclosingCircle(c)
  amount_figure[count]=radius
  amount_axeX[count]= x
  amount_axeY[count]= y

  count = count+1

  newradius = int(radius)

  cv2.imshow("Frame", frame)
  key = cv2.waitKey(1) & 0xFF
  if radius > 0:
   cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)

 if len (amount_figure)>0:
  b=((amount_figure.index(max(amount_figure))))

  cv2.putText(frame, 'object was found', (int (amount_axeX[b]) , int (amount_axeY[b])), cv2.FONT_ITALIC, 0.8, 255) # # cv2.putText(frame,text,location,font,font size,font color, font weight, line)
  cv2.imshow("Frame", frame)
  key = cv2.waitKey(1) & 0xFF
  if key == ord("q"):
   break
