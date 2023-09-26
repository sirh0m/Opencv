#
#
# # importing opencv
#import cv2
#
# # reading the file
#img = cv2.imread('assets/bottle.jpeg', 1)

# #resizing the image
#img = cv2.resize(img, (0, 0), fx=3, fy=3)
# # in resizing you can as well type img = cv2.resize(img, (200, 200)).These numbers are the pixels of the image
# Though for fx and fy, the values you put either multiply the images size eg by 2, 3 etc or halve it by 0.5 etc
#
# # rotating the image
#img = cv2.rotate(img, cv2.cv2.ROTATE_180)

# #writing the image to a new folder
#cv2.imwrite('new_img.jpeg', img)
#
# # displaying the image
#cv2.imshow('image', img)
#print(type(img))
#
# # wait for an infinite amount of time for you to press a key, if its 5, then i
# #it will wait for 5 seconds and if you dont press any key it will be skipped
# cv2.waitKey(0)
import random

# # after pressing the key thi method closes the windows
# #so that they dont load in the background
# cv2.destroyAllWindows()
#
#

#IMAGE MANIPULATION
import cv2
import random
img = cv2.imread('assets/water-splash-bottle-21576605.jpg', -1)

 # for i in range(100):
 #    for j in range(img.shape[1]):
 #         img[1][j] = [random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)]
tag = img[500:700, 600:900]
img[100:300, 500:600] = tag
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
