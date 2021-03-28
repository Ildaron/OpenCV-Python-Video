import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)
x1=000
y1=100
x2=900
y2=100

while(cap.isOpened()):
    ret, image1 = cap.read()
    ret, image2 = cap.read()
    #current_frame1 = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    line_thickness = 2
    cv2.line(image1, (x1, y1+50), (x2, y2+50), (10, 155, 10), thickness=line_thickness)
    cv2.line(image1, (x1, y1-50), (x2, y2-50), (90, 55, 60), thickness=line_thickness)
    cv2.line(image1, (x1, y1+150), (x2, y2+150), (90, 55, 60), thickness=line_thickness)
    cv2.line(image1, (x1, y1), (x2, y2), (60, 70, 100), thickness=line_thickness)

    cv2.line(image1, (x1, y1+450), (x2, y2+450), (10, 155, 10), thickness=line_thickness)
    cv2.line(image1, (x1, y1+300), (x2, y2+300), (5, 15, 60), thickness=line_thickness)
    cv2.line(image1, (x1, y1+100), (x2, y2+100), (67, 45, 60), thickness=line_thickness)
    cv2.line(image1, (x1, y1+200), (x2, y2+200), (167, 145, 160), thickness=line_thickness)
    cv2.line(image1, (x1, y1+250), (x2, y2+250), (160, 170, 10), thickness=line_thickness)



    cv2.line(image2, (x1, y1+50), (x2, y2+50), (10, 155, 10), thickness=line_thickness)
    cv2.line(image2, (x1, y1-50), (x2, y2-50), (90, 55, 60), thickness=line_thickness)
    cv2.line(image2, (x1, y1+150), (x2, y2+150), (90, 55, 60), thickness=line_thickness)
    cv2.line(image2, (x1, y1), (x2, y2), (60, 70, 100), thickness=line_thickness)

    cv2.line(image2, (x1, y1+450), (x2, y2+450), (10, 155, 10), thickness=line_thickness)
    cv2.line(image2, (x1, y1+300), (x2, y2+300), (5, 15, 60), thickness=line_thickness)
    cv2.line(image2, (x1, y1+100), (x2, y2+100), (67, 45, 60), thickness=line_thickness)
    cv2.line(image2, (x1, y1+200), (x2, y2+200), (167, 145, 160), thickness=line_thickness)
    cv2.line(image2, (x1, y1+250), (x2, y2+250), (160, 170, 10), thickness=line_thickness)


    
    both = np.concatenate((image1, image2), axis=1)
    cv2.imshow('frame diff ',both)      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
