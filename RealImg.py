import cv2
import numpy as np

 
cap = cv2.VideoCapture('000.avi')

def adjustLinghting(src, contrast, brightness):
    img = cv2.convertScaleAbs(src, alpha=contrast, beta=brightness)
    return(img)


while True:
    ret, frame = cap.read()
    
    frame2 = adjustLinghting(frame, 0.1, 1)
    
    cv2.imshow("Original", frame2)
    
    
    cv2.waitKey(30)
    
    
cap.release()
cv2.destroyAllWindows()
