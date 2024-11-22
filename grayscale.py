import cv2
import numpy as np

img= cv2.imread('rocky.jpg')
img = cv2.resize(img,(400, 500))
cv2.imshow('before',img)
img = cv2.resize(img,(400, 500))

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convertion Image into 3 channel for concatenation process
img2 = np.zeros_like(img)
img2[:,:,0] = gray_image
img2[:,:,1] = gray_image
img2[:,:,2] = gray_image

cv2.imshow('Grayimage',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()