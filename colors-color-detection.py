import numpy as np
import cv2

cap = cv2.VideoCapture('assets/Natti Natasha - To’ Esto Es Tuyo.mp4')
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([252, 95, 31])
    upper_blue = np.array([252, 94, 83])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', hsv)
    cv2.imshow('mask', mask)

    if cv2.waitKey(5) == ord('r'):
        break

cap.release()
cv2.destroyAllWindows()