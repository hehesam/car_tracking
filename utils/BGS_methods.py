import cv2
from utils.stacker import stackImages
cap = cv2.VideoCapture("C:/GIT/car_tracking_videos/v2.mp4")

MOG2 = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
knn = cv2.createBackgroundSubtractorKNN(history=100,detectShadows=False)

while True : 
    _, frame = cap.read()
    _, frame2 = cap.read()


    blured = cv2.GaussianBlur(frame,(11,11),0)
    grey = cv2.cvtColor(blured,cv2.COLOR_BGR2GRAY)

    blured2 = cv2.GaussianBlur(frame2,(11,11),0)
    grey2 = cv2.cvtColor(blured2,cv2.COLOR_BGR2GRAY)

    mask1 = MOG2.apply(grey)
    mask2 = knn.apply(grey)
    mask3 = cv2.absdiff(grey,grey2)
    # mask4 = MOG2.apply(grey)
    # mask5 = knn.apply(grey)

    width,height, _ = frame.shape
    frame = cv2.resize(frame,(height//2,width))

    res = stackImages(0.5, ([mask1,mask2],[mask3,grey]))
    cv2.imshow("see", res)

    if cv2.waitKey(1) & 0xFF == ord('t'):
        break