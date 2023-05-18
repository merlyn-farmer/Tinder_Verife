import time

import pyvirtualcam
import cv2

def virtual_camera(path):
    frame = cv2.imread(path)
    time.sleep(1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    time.sleep(1)
    frame = cv2.flip(frame, 1)
    #frame = cv2.resize(frame, (1280, 720), cv2.INTER_AREA)
    width = frame.shape[1]
    height = frame.shape[0]
    print(width)
    print(height)
    cam = pyvirtualcam.Camera(width=width, height=height, fps=10)

    for i in range(4000):
        cam.send(frame)
    cam.close()
