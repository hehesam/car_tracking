import cv2
from stacker import stackImages
cap = cv2.VideoCapture("C:/GIT/car_tracking_videos/v2.mp4")

MOG2 = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
knn = cv2.createBackgroundSubtractorKNN(history=100,detectShadows=False)

while True : 
    _, frame = cap.read()
    _, frame2 = cap.read()


    mask1 = MOG2.apply(frame)
    mask2 = knn.apply(frame)
    mask3 = cv2.absdiff(frame,frame2)

    width,height, _ = frame.shape
    frame = cv2.resize(frame,(height//2,width))
    
    res = stackImages(0.8, ([mask1,mask2],[mask3,frame]))
    cv2.imshow("see", res)

    if cv2.waitKey(1) & 0xFF == ord('t'):
        break