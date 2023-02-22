import cv2
import numpy as np

canvas = np.zeros((512,512,3) , dtype=np.uint8)
rectangle=np.zeros((400,400,3),dtype=np.uint8)
circle=np.zeros((640,640,3),dtype=np.uint8)
poly=np.zeros((640,640,3),dtype=np.uint8)
ellipse=np.zeros((640,640,3),dtype=np.uint8)
cv2.line(canvas,(10,10),(400,400),(255,0,255),thickness=4)
cv2.rectangle(rectangle,(50,50),(200,200),(255,200,255),thickness=10)
cv2.circle(circle,(300,300),100,(0,255,255),thickness=8)
point = np.array([[[50,150],[150,200],[250,350],[300,400]]])
cv2.polylines(poly, [point], True, (0,255,200),thickness=5)
cv2.ellipse(ellipse,(300,300),(80,50),10,90,360,(140,200,140),-1)



cv2.imshow("Ellipse",ellipse)
cv2.imshow("Poly",poly)
cv2.imshow("Circle",circle)
cv2.imshow("Rec",rectangle)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
