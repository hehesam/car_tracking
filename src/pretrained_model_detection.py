# it is slow and has low accuracy

import cv2

cap = cv2.VideoCapture("C:/GIT/car_tracking_videos/v2.mp4")
car_cascade = cv2.CascadeClassifier("data/cars.xml")

while True : 
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray,1.1,1)
    print(cars)
    # to draw a rectangle in each cars
    for (x,y,w,h) in cars:
        # print(x,y,w,h)
        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,0,255), 2)
        cv2.putText(frame,'car', (x+6,y-6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0,0,255),1)

    # display frame 
    cv2.imshow("aa",frame)
    if cv2.waitKey(1) & 0xFF == ord('t'):
        break


