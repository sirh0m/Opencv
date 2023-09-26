import numpy as np
import cv2

cap = cv2.VideoCapture('assets/Natti Natasha - To’ Esto Es Tuyo.mp4')
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # drawing a line through the image/video
    # Note: (0, 0) are the beginning coordinates of the image, that's in the top left corner.
    img = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 5)
    # drawing the line across or above the previous line
    img = cv2.line(img, (0, height), (width, 0), (255, 0, 0), 5)
    # Drawing a rectangle
    img = cv2.rectangle(img, (150, 150), (400, 400), (0, 255, 255), 5)
    # Drawing circles
    img = cv2.circle(img, (370, 370), 40, (0, 0, 0), 4)
    # Writing text
    # Note: It's considered to start from the bottom left, and we first specify the font to use.
    font = cv2. FONT_HERSHEY_TRIPLEX
    img = cv2.putText(img, 'Sam is progressing', (20, height - 20), font, 2, (255, 0, 255), 5, cv2.LOCAL_OPTIM_INNER_AND_ITER_LO)


    cv2.imshow('frame', img)

    if cv2.waitKey(5) == ord('r'):
        break

cap.release()
cv2.destroyAllWindows()