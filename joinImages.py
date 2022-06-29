import cv2
import numpy as np

path = 'images/4.jpg'
img = cv2.imread(path)

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow('Horizontal', imgHor)
cv2.imshow('Vertical', imgVer)
cv2.waitKey(0)