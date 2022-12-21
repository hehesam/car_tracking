import cv2
from stacker import stackImages
cap = cv2.VideoCapture("C:/GIT/car_tracking_videos/v1.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)


while True:
    _, frame = cap.read()
    width,height, _ = frame.shape
    frame = cv2.resize(frame,(height//2,width))
    mask1 = object_detector.apply(frame)
    _, mask2 = cv2.threshold(mask1, 254, 255, cv2.THRESH_BINARY)
    res = stackImages(0.8, ([mask1, mask2],[mask1,mask2]))
    cv2.imshow("see", res)

    if cv2.waitKey(1) & 0xFF == ord('t'):
        break