
import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
 _,frame=cap.read()
 hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  #rentang warna biru dalam HSV
 lower_green = np.array([35, 100, 50])
 upper_green = np.array([85, 255, 255])
  #masking untuk mendeteksi warna biru
 mask=cv2.inRange(hsv,lower_green,upper_green)
 result=cv2.bitwise_and(frame,frame,mask=mask)
  #menampilkan hasil
 cv2.imshow("Frame",frame)
 cv2.imshow("Mask",mask)
 cv2.imshow("Result",result)
 if cv2.waitKey(1) & 0xFF==ord('q'):
  break
cap.release()
cv2.destroyAllWindows()