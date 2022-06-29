import cv2

path = 'images/4.jpg'
img = cv2.imread(path)
# (height, width, bgr)
# print(img.shape)

imgResize = cv2.resize(img, (200, 200))

# (h, w) unlike opencv which is (w, h)
imgCropped = img[100:300, 75:275]

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)