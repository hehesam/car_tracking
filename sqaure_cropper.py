import cv2
cap = cv2.VideoCapture("C:/GIT/car_tracking_videos/v2.mp4")
# cap = cv2.VideoCapture(0)

clicked_list = []
point_list = []
def mousePoints(event, x,y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_list.append([x,y])
    elif event == cv2.EVENT_MOUSEMOVE:
        point_list.clear()
        point_list.append([x,y])

cropped = False

while True:
    _, frame = cap.read()

    if cropped == False:
        if len(clicked_list) == 3:
            clicked_list.clear()
        cv2.imshow("frame", frame)
        cv2.setMouseCallback("frame", mousePoints)

        if len(clicked_list)==1:
            x1,y1 = clicked_list[0]
            x2,y2 = point_list[-1]
            cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),3)
        elif len(clicked_list)==2:
            x1,y1 = clicked_list[0]
            x2,y2 = clicked_list[-1]
            cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),3)
            cropped = True
    else:
        x1,y1 = clicked_list[0]
        x2,y2 = clicked_list[-1]
        frame = frame[y1:y2, x1:x2]
        if len(clicked_list) == 3:
            cropped = False
            continue

    
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('t'):
        break