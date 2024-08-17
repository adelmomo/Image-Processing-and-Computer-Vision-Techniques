from EdgeDetection import EdgeDetector
from Utils import Utils
import cv2

edge_detector=EdgeDetector('Canny', kernel_size = 3, preprocessing = True)
cap=Utils.create_video_capture(0)

while True:
    ret,frame=cap.read()
    if ret:

        #compute the image edges using the predefined method
        img_edges=edge_detector.detect(frame)

        #count nonzeros edges in the scene to detect if the Camera is covered/blocked or not
        edges_count=Utils.count_non_zeros_pixels(img_edges)

        if edges_count > 0:
            frame = Utils.write_string_to_frame(frame, "Camera is not covered")
        else:
            frame = Utils.write_string_to_frame(frame, "Camera is covered")
         
         
         
        cv2.imshow('',frame)
        cv2.waitKey(1)
    else:
        break
