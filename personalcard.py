import cv2
import numpy as np

image2=cv2.imread("cat.jpg")
print(image2)
print(image2.shape)
cat = image2[120:220,150:200]
print(cat)

text = "my own image card"

image2[0:100,50:100]=cat
cv2.putText(image2,text,(20,200),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,color=(0,0,255))

cv2.imshow("mywindow",image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
