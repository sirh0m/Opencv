import numpy as np
import cv2

img = cv2.imread('assets/ch.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.2, 10)
corners = np.int0(corners)

for corner in corners:
    z, w = corner.ravel()
    cv2.circle(img, (z, w), 5, (0, 255, 0), 1)

    # Drawing lines in corners
for l in range(len(corners)):
    for m in range(l + 1, len(corners)):
        corner1 = tuple(corners[l][0])
        corner2 = tuple(corners[m][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))# we convert these 64bit numpy integers to regular python integers
        cv2.line(img, corner1, corner2, (), 1)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()