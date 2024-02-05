import cv2
import numpy as np

path = 'E:\\MCE-12\\current-lab\\8\\data\\100-2.avi'
cap = cv2.VideoCapture(path)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(frame, maxLoc, 15, (0, 0, 0), 2)

    cv2.imshow("frame", frame)
    cv2.waitKey(30)
    print(minVal, maxVal, minLoc, maxLoc)
    
cap.release()
cv2.destroyAllWindows()