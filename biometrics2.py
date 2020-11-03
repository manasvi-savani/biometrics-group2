import cv2
import os
import math

cap = cv2.VideoCapture("1.mp4")
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print(length)

vid = cv2.VideoCapture('1.mp4')
if not os.path.exists('images'):
    os.makedirs('images')

modulo = math.ceil(length/60)

index = 1
count = 0
while(True):
    ret, frame = vid.read()
    if count % modulo == 0:
        if not ret:
            break
        name = './images/Task1-Frame' + str(index) + '.png'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        index += 1
    count += 1
