import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import imutils

path = 'E:\\MCE-12\\DATA\\pic\\60A_8_02.jpg'
pic = cv2.imread(path)


def resizeimg(src,x):
    width = int(src.shape[1] *x)
    height = int(src.shape[0] * x)
    dim = (width, height)
    resized = cv2.resize(src, dim, interpolation = cv2.INTER_AREA)
    return(resized)

def preimg(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # img = cv2.blur(gray, )
    img = cv2.fastNlMeansDenoising(gray, 2, 21, 7, 21)
    # img = cv2.bilateralFilter(gray, 11, 17, 17)
    return(img)



def adjustLinghting(src, contrast, brightness):
    img = cv2.convertScaleAbs(src, alpha=contrast, beta=brightness)
    return(img)

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma
    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    return cv2.LUT(src, table)

def EDGE(src, th1, th2):
    edges = cv2.Canny(src, th1, th2)
    return(edges)

def invert(src):
    yarg = cv2.bitwise_not(src)
    return(yarg)


def THRESHOLD(src, th1, th2):
    ret,th = cv2.threshold(src,th1,th2,cv2.THRESH_BINARY)
    return(th)

def findrect(src, cont):
    # cnt = cv2.findContours(gray.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnt)
    # c = max(cnts, key=cv2.contourArea)
    # output = np.array(src)
    # output = cv2.cvtColor(output , cv2.COLOR_GRAY2BGR)
    # cv2.drawContours(output, [c], -1, (0, 255, 0), 3)
    # (x, y, w, h) = cv2.boundingRect(c)
    # text = "original, num_pts={}".format(len(c))
    # cv2.putText(output, text, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX,0.9, (0, 255, 0), 2)

    cnt = 0
    i = 7
    for c in cont:
        contour_perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * contour_perimeter, True)
        if len(approx) == 4:
            screenCnt = approx
            x, y, w, h = cv2.boundingRect(c)
            i += 1
            break

    # draws the license plate contour on original image
    cv2.drawContours(src , [screenCnt], -1, (0, 255, 0), 3)
    return(src)

def findcon(gray, lo, hi):
    contours, new = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
            area = cv2.contourArea(cnt)
            # print(area)
            if area > lo and area < hi:
                img = cv2.drawContours(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR), [cnt], -1, (0, 255, 0), 10)
                cnt = cnt
    return(img, cnt)


def boundRect(src,gray,hi,lo): 
    contour, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contour:
            area = cv2.contourArea(cnt)
            # print(area)
            if area > lo and area < hi:
                x, y, w, h = cv2.boundingRect(cnt)
                reg = cv2.rectangle(src, (x,y), (x+w,y+h) ,(0,0,0),0)
                cropped=reg[y:y+h, x:x+w]
    return(cropped)




#  DO
img = preimg(pic)
img = gammaCorrection(img, 0.5)
img = invert(img)
img = THRESHOLD(img,220,255)
img = boundRect(pic,img,5000000,100000)
img1 = img
img = preimg(img)
img = adjustLinghting(img, 5,1)
img = THRESHOLD(img, 240,255)
img, con =findcon(img, 100000, 50000000)
img = img1[con]

img = EDGE(img,10,255)
print(img)
     



# result = resizeimg(img, 0.2)
# cv2.imshow('result', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
