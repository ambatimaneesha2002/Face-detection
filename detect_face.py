import cv2
#
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(0)
# while True:
#     _,img = cap.read()
#
# # img = cv2.imread('heroine.jpg')
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#
# # for (x, y, w, h) in faces:
# #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
#     cv2.imshow('img', img)
#     k = cv2.waitKey(1)& 0xFF
#     if k == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()
#
#
#
cap = cv2.VideoCapture(0)

if (cap.isOpened() == False):
    print("Error opening video stream or file")

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()