import cv2
import numpy as np

canvas1 = np.zeros((512,512,3), np.uint8)
canvas2 = np.zeros((512,512,3), np.uint8)

cv2.circle(canvas1, (256,256), 60, (255,0,0), -1)
cv2.rectangle(canvas2, (150,150), (350,350), (0,255,0), -1)

add = cv2.add(canvas2,canvas1)

cv2.imshow("circle",canvas1)
cv2.imshow("rectangle",canvas2)
cv2.imshow("add",add)


cv2.waitKey(0)
cv2.destroyAllWindows()