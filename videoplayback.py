import numpy as np
import cv2
x=cv2.VideoCapture("Video")
while (x.isOpened()) :
    ret, fream = x.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",gray)
    if cv2.waitkey(1) and 0xFF == ord("q"):
        break
x.release()
cv2.destroyAllWindows()
