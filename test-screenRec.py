import cv2
import numpy as np
import pyautogui



# display screen resolution, get it using pyautogui itself
SCREEN_SIZE = tuple(pyautogui.size())
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# frames per second
fps = 12.0
# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, fps, (SCREEN_SIZE))
# the time you want to record in seconds
record_seconds = 10