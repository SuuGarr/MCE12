import cv2
import torch 
import os
from ultralytics import YOLO
from PIL import Image


model_path = 'H:\\code\\model1.pt'  # Replace with the actual path to your custom model .pt file
model = YOLO(model_path)



# Input file name
file = 'H:\\PrelimResult\\test2.avi'

results = model.track(source=file, show =True, tracker="bytetrack.yaml")