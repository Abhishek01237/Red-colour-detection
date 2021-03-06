import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while (1):

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,100,200])

    upper_red = np.array([5,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Original', frame)
#    edges = cv2.Canny(frame, 100, 200)
#    cv2.imshow('Edges', edges)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break    
cap.release()
cv2.destroyAllWindows()
