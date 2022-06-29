import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
path = 'images/3.jpg'
img = cv2.imread(path)

# pytesseract only accepts rgb value but opencv is in bgr so we have to convert it first
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# print(pytesseract.image_to_string(img))

# detecting characters
# hImg, wImg, _ = img.shape
# cong = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img, config=cong)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
#     cv2.putText(img, b[0], (x, hImg-y+30), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

# detecting words
boxes = pytesseract.image_to_data(img)
for n, b in enumerate(boxes.splitlines()):
    if n != 0:
        b = b.split()
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 2)
            cv2.putText(img, b[11], (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

# detecting words
# cong = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img, config=cong)
# for n, b in enumerate(boxes.splitlines()):
#     if n != 0:
#         b = b.split()
#         if len(b) == 12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 2)
#             cv2.putText(img, b[11], (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)