import cv2
import numpy as np

path = 'E:\\MCE-12\\current-lab\\8\\data\\100-2.avi' 
cap = cv2.VideoCapture(path)
# object_detector = cv2.createBackgroundSubtractorMOG2()


X, Y, width, height = 240, 100, 140, 450

while True:
    ret, frame = cap.read()
    # print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    groi = gray[Y:Y+height, X:X+width]
    roi = frame[Y:Y+height, X:X+width]
    
    retval, Threshold = cv2.threshold(groi, 220, 255, cv2.THRESH_BINARY)
    contour, _ = cv2.findContours(Threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
   
    for cnt in contour:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 150:
            # cv2.drawContours(roi, [cnt], -1, (0, 0, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x,y), (x+w,y+h) ,(0,0,0),3)
            
    
        
            
    
    
    # mask = object_detector.apply(frame)
    cv2.imshow("frame", frame)
    # # cv2.imshow("mask", mask)
    # cv2.imshow("gray", gray)
    # cv2.imshow("ROI", roi)
    # cv2.imshow("Thresh", Threshold)
    
    cv2.waitKey(30)
    
    
cap.release()
cv2.destroyAllWindows()