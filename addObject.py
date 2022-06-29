import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# img[:] = 255, 0, 0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (128, 128), (384, 384), (0, 0, 255), 2)
cv2.circle(img, (256, 256), 64, (255, 0, 0), 5)
cv2.putText(img, "SHAPES", (375, 35), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)