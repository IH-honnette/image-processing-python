#import numpy as np
import cv2
image = cv2.imread('lena.jpg')
y=950
x=900
h=550
w=500
cropped = image[y:y+h, x:x+w]

# Save cropped image
cv2.imwrite("lena_cropped.jpg", cropped)

cv2.imshow('Lena Cropped', cropped)
cv2.waitKey(0)