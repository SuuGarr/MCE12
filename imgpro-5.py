import cv2
import numpy as np

path = 'E:\\MCE-12\\current-lab\\8\\data\\100-3.avi'
cap = cv2.VideoCapture(path)

def crack_detect_hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

    lower = np.array([60, 180, 80], np.uint8) 
    upper = np.array([90, 220, 240], np.uint8) 
    mask = cv2.inRange(hsv, lower, upper) 
    kernel = np.ones((3, 3), "uint8") 
      

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
            # print(h)
            # cv2.rectangle(img, (x,y), (x+w,y+h) ,(0,0,255),3)
            if h > 60:
                cv2.putText(img, 'crack!!!', (50, 200), cv2.FONT_HERSHEY_SIMPLEX,  
                   0.6, (0, 0, 255) , 1, cv2.LINE_AA)
        else: 
            img = img
    return(img)
    
def crack_detect(img):
    # image_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # image_grayscale_blurred = cv2.GaussianBlur(image_grayscale, (5,5), 0)
    # image_canny = cv2.Canny(image_grayscale_blurred, 10, 80)
    # _, mask = image_canny_inverted = cv2.threshold(image_canny, 70, 255, cv2.THRESH_BINARY_INV)
    # return mask
    # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, TH1 = cv2.threshold(img,150, 200, cv2.THRESH_BINARY)
    con1, _ = cv2.findContours(TH1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in con1:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        
        if area > 50 and area < 800 :
            
            cv2.drawContours(img, [cnt], -1, (255, 0, 255), 1)
            x, y, w, h = cv2.boundingRect(cnt)
            
            # if h > 1:
            #     cv2.putText(img, 'crack!!!', (50, 250), cv2.FONT_HERSHEY_SIMPLEX,  
            #        1, (0, 0, 255) , 2, cv2.LINE_AA)
            # cv2.rectangle(img, (x,y), (x+w,y+h) ,(0,0,255),3)
        # else: 
        #     img = img
    return(img)
    


while True:
    ret, frame = cap.read()
    crop = frame[0:400,100:500]
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    upper_left = (maxLoc[0]-60,50)
    bottom_right = (maxLoc[0]+60, 380)
    rect_img = crop[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
    roi = crop[50:380, maxLoc[0]-55:maxLoc[0]+70]
    area = roi

    #uptodetectfunc
    area = crack_detect_hsv(area)
    # rgb_area = cv2.cvtColor(area, cv2.COLOR_GRAY2BGR)
    rgb_area = cv2.cvtColor(area, cv2.COLOR_HSV2BGR)

    crop[50:380, maxLoc[0]-55:maxLoc[0]+70] = rgb_area
    

    cv2.imshow("frame", frame)
    cv2.waitKey(30)

cap.release()
cv2.destroyAllWindows()