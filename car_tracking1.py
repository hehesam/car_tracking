import cv2
from stacker import stackImages
cap = cv2.VideoCapture("C:/GIT/car_tracking_videos/v2.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=25)


while True:
    _, frame = cap.read()
    width,height, _ = frame.shape
    frame = cv2.resize(frame,(height//2,width))
    mask1 = object_detector.apply(frame)
    # mask1 = cv2.dilate(mask1,None, iterations=3)
    # mask1 = cv2.erode(mask1,None, iterations=5)


    _, mask2 = cv2.threshold(mask1, 254, 255, cv2.THRESH_BINARY)
    mask3 = cv2.erode(mask2,None, iterations=2)
    mask4 = cv2.dilate(mask3,None, iterations=6)
    contours, _ = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 300:
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)



    res = stackImages(0.8, ([mask1,mask3],[mask4,frame]))
    cv2.imshow("see", res)

    if cv2.waitKey(1) & 0xFF == ord('t'):
        break