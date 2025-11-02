import cv2
from utils.stacker import stackImages





# Create tracker object
# tracker = EuclideanDistTracker()

cap1 = cv2.VideoCapture("C:/GIT/car_tracking_videos/v1.mp4")
cap2 = cv2.VideoCapture("C:/GIT/car_tracking_videos/v2.mp4")
cap3 = cv2.VideoCapture("C:/GIT/car_tracking_videos/v3.mp4")

phase = 0
while True :

    _,frame1 = cap1.read()
    _,frame2 = cap2.read()
    _,frame3 = cap3.read()

 

    res = stackImages(0.5, ([frame1,frame2],[frame3,frame1]))
    cv2.imshow("see", res)
    
    if cv2.waitKey(1) & 0xFF == ord('t'):
        break


