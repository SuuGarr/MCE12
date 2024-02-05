import cv2
import numpy as np
import os
import moviepy.editor as moviepy

path = "D:\\MCE-12\\PrelimResult"

files = os.listdir(path)

for file in files:
    # print(file)
    clip = moviepy.VideoFileClip(path+'\\'+file)
    clip.write_videofile(path+'\\'+file+'.mp4')
    print(clip)
