import cv2
import matplotlib.pyplot as plt

#Read Image
img = cv2.imread("IMAGE.jpg")
#Convert Image To Gray Color
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img, 'gray')
plt.show()
