import cv2
import numpy as np

path = 'E:\\MCE-12\\current-lab\\8\\data\\100-1.avi'
cap = cv2.VideoCapture(path)

def crack_detect(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
  
    # Set range for red color and  
    # define mask 
    lower = np.array([60, 180, 80], np.uint8) 
    upper = np.array([90, 220, 240], np.uint8) 
    mask = cv2.inRange(hsv, lower, upper) 
    kernel = np.ones((3, 3), "uint8") 
      
    # For red color 
    mask = cv2.dilate(mask, kernel) 
    res = cv2.bitwise_and(img, img, mask = mask) 

    con, hierarchy = cv2.findContours(mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE)
  
    for pic, contour in enumerate(con): 
        area = cv2.contourArea(contour) 
        if area > 10 :
            
            cv2.drawContours(img, [contour], -1, (255, 0, 255), 1)
            x, y, w, h = cv2.boundingRect(contour)
            # cv2.rectangle(img, (x,y), (x+w,y+h) ,(0,0,255),3)
        else: 
            img = img
    return(img)
    
    
    

while True:
    ret, frame = cap.read()
    crop = frame[0:400,100:500]
    gray = cv2.cvtColor(crop, cv2.COLOR_RGB2GRAY)
    
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    # cv2.circle(crop, maxLoc, 15, (0, 0, 0), 2)
    
    
    #rectangle
    upper_left = (maxLoc[0]-60,50)
    bottom_right = (maxLoc[0]+60, 380)
    # r = cv2.rectangle(crop, upper_left, bottom_right, (0, 0, 0), 2)
    rect_img = crop[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
    
    #polygon
    # pts = np.array([[maxLoc[0]-55,50], [maxLoc[0]+55,50], 
    #             [maxLoc[0]+70,380], [maxLoc[0]-70,380]],
    #            np.int32)
    # cv2.polylines(crop, [pts], 
    #                   True, (255,255,255), 1)
    
    roi = crop[50:380, maxLoc[0]-55:maxLoc[0]+70]
    
    
    area = roi
    area = crack_detect(roi)

    rgb_area = cv2.cvtColor(area, cv2.COLOR_HSV2BGR)

    crop[50:380, maxLoc[0]-55:maxLoc[0]+70] = rgb_area

    cv2.imshow("frame", frame)
    cv2.waitKey(30)

    
    # print(maxLoc)
    # print(minVal)
    # print(maxVal)
    # print(low_threshold)
    # print(high_threshold)



cap.release()
cv2.destroyAllWindows()