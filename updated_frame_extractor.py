import cv2
import os
import math
from PIL import Image

task = 1
while( task <= 23):
    cap = cv2.VideoCapture("A_Barua/Task"+ str(task) +".mp4")
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    vid = cv2.VideoCapture('A_Barua/Task'+ str(task) +'.mp4')
    if not os.path.exists('A_Barua/Task'+ str(task)):
        os.makedirs('images/A_Barua/Task'+ str(task))

    modulo = math.ceil(length/60)

    index = 1
    count = 0
    while(True):
        ret, frame = vid.read()
        if count % modulo == 0:
            if not ret:
                break
            name = './images/A_Barua/Task'+ str(task)+'/Task'+ str(task)+'-Frame' + str(index) + '.png'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)

             # rotate image
            im = Image.open(name)
            angle = -90
            out = im.rotate(angle, expand=True)
            out.save(name)
            index += 1
        count += 1
    task += 1