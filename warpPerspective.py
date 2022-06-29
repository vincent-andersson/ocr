import cv2
import numpy as np

path = 'images/5.jpg'
img = cv2.imread(path)

width, height = 250, 350
pts1 = np.float32([[225, 93], [430, 137], [162, 380], [370,425]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)