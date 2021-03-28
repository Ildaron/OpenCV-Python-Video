import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, current_frame = cap.read()

    both = np.concatenate((current_frame, current_frame), axis=1)  
    cv2.imshow('frame diff ',both)      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
