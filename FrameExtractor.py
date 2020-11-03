import cv2
import numpy as np
import os
from ..convenience import is_cv3
import cv2
def count_frames(path, override=False):
	# grab a pointer to the video file and initialize the total
	# number of frames read
	video = cv2.VideoCapture(path)
	total = 0
	# if the override flag is passed in, revert to the manual
	# method of counting frames
	if override:
		total = count_frames_manual(video)



# set video file path of input video with name and extension
vid = cv2.VideoCapture('D:\Users\Michael\Documents\College\USF\CAP4103 (Mobile Biometrics)\biometrics-group2\Face Data\Task1')


if not os.path.exists('images'):
    os.makedirs('images')
total_frames = count_frames(vid)
modulo = total_frames/60
#for frame identity
index = 0
count = 0
while(True):
    ret, frame = vid.read()
    if count % modulo == 0:
        # Extract images
        # ret, frame = vid.read()
        # end of frames
        if not ret:
            break
        # Saves images
        name = './images/Task1-Frame' + str(index) + '.png'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

        # next frame
        index += 1
    count += 1