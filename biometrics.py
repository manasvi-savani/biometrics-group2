import cv2
import os
import math

task = 1
while( task <= 23):
    cap = cv2.VideoCapture("J_Strickland/Task"+ str(task) +".mp4")
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # print(length)

    vid = cv2.VideoCapture('J_Strickland/Task'+ str(task) +'.mp4')
    if not os.path.exists('J_Strickland/Task'+ str(task)):
        os.makedirs('images/J_Strickland/Task'+ str(task))

    modulo = math.ceil(length/60)

    index = 1
    count = 0
    while(True):
        ret, frame = vid.read()
        if count % modulo == 0:
            if not ret:
                break
            name = './images/J_Strickland/Task'+ str(task)+'/Task'+ str(task)+'-Frame' + str(index) + '.png'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            index += 1
        count += 1
    task += 1
