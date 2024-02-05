import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import imutils

path = 'E:\\MCE-12\\current-lab\\BPT\\BPT (4).jpg'

pic = cv2.imread(path)


def resizeimg(src,x):
    width = int(src.shape[1] *x)
    height = int(src.shape[0] * x)
    dim = (width, height)
    resized = cv2.resize(src, dim, interpolation = cv2.INTER_AREA)
    return(resized)

def adjustLinghting(src, contrast, brightness):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    img = cv2.convertScaleAbs(gray, alpha=contrast, beta=brightness)
    return(img)

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)

def EDGE(src, th1, th2):
    edges = cv2.Canny(src, th1, th2)
    return(edges)


def THRESHOLD(src, th1, th2):
    # gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # yarg = cv2.bitwise_not(src)
    ret,th = cv2.threshold(src,th1,th2,cv2.THRESH_BINARY)
    return(th)



def findrect(src):
    th = THRESHOLD(src, 250, 255)
    cnt = cv2.findContours(th.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnt)
    c = max(cnts, key=cv2.contourArea)
    output = np.array(src)
    output = cv2.cvtColor(output , cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output, [c], -1, (0, 255, 0), 3)
    (x, y, w, h) = cv2.boundingRect(c)
    text = "original, num_pts={}".format(len(c))
    cv2.putText(output, text, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX,0.9, (0, 255, 0), 2)
    return(output)

img2 = gammaCorrection(pic, 0.5)
img1 = adjustLinghting(img2,2.8,20)

img = THRESHOLD(img1, 180,255)
# img =findrect(img1)


result = resizeimg(img3, 0.6)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
