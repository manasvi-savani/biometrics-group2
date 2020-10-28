import cv2
import numpy as np
import os

vid = cv2.VideoCapture('1.mp4')

if not os.path.exists('images'):
    os.makedirs('images')

index = 1
while(index <= 5):
    ret, frame = vid.read()
    if not ret: 
        break
    name = './images/frame' + str(index) + '.jpg'
    print ('Creating...' + name)
    
    cv2.imwrite(name, frame)
    index += 1