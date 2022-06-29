import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            objCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCorners == 3:
                objType = 'Triangle'
            elif objCorners == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objType = 'Square'
                else:
                    objType = 'Rectangle'
            elif objCorners == 5:
                objType = 'Pentagon'
            elif objCorners == 6:
                objType = 'Hexagon'
            elif objCorners > 6:
                objType = 'Circle'
            else:
                objType = 'None'

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

path = 'images/6.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

imgBlank = np.zeros_like(img)

# cv2.imshow('Image', img)
# cv2.imshow('Gray', imgGray)
# cv2.imshow('Blur', imgBlur)
# cv2.imshow('Canny', imgCanny)
# cv2.imshow('Blank', imgBlank)
cv2.imshow('Contour', imgContour)
cv2.waitKey(0)