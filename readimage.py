import cv2
import numpy


image= cv2.imread("applecode.jpg")
image2= cv2.imread("cat.jpg")


grayImage=cv2.cvtColor(image2,cv2.COLOR_RGB2GRAY)
print(grayImage)
cv2.imshow("mywindow",grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()


# image= cv2.imread("cat.jpg")
# print(type(image))
# print(image.shape)

# print(image)