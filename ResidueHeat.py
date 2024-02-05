import cv2
import numpy as np

path = 'E:\\MCE-12\\current-lab\\8\\data\\100-1.avi'
cap = cv2.VideoCapture(path)

# object_detector = cv2.createBackgroundSubtractorMOG2()


X, Y, width, height = 255, 100, 120, 450

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    groi = gray[Y:Y+height, X:X+width]
    roi = frame[Y:Y+height, X:X+width]
    
    retval, TH1 = cv2.threshold(groi,155, 255, cv2.THRESH_BINARY)
    con1, _ = cv2.findContours(TH1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    retval, TH2 = cv2.threshold(groi, 150, 210, cv2.THRESH_BINARY)
    con2, _ = cv2.findContours(TH2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
    for cnt in con1:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        
        if area > 200:
            # cv2.drawContours(roi, [cnt], -1, (0, 0, 0), 5)
            x, y, w, h = cv2.boundingRect(cnt)
            # cv2.rectangle(roi, (x,y), (x+w,y+h) ,(0,0,0),3)
            
    for cnt in con2:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        print(area)
        if area < 200 and area >10 :
            # cv2.drawContours(roi, [cnt], -1, (0, 0, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x,y), (x+w,y+h) ,(0,0,255),1)
    
        
            
    
    
    # mask = object_detector.apply(frame)
    # cv2.imshow("frame", frame)
    # cv2.imshow("mask", mask)
    # cv2.imshow("gray", gray)
    # cv2.imshow("ROI", roi)
    # cv2.imshow("Thresh", TH1)
    # cv2.imshow("Thresh", TH2)
    # print(frame)
    cv2.waitKey(30)

    
cap.release()
cv2.destroyAllWindows()