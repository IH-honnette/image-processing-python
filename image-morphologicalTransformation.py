import cv2
import numpy as np

img = cv2.imread('lena.jpg', 0)
resized_img = cv2.resize(img, (800, 650))

# Define kernel for morphological operations
kernel = np.ones((5,5), np.uint8)

# Apply erosion

erosion = cv2.erode(img, kernel, iterations=1)
resized_erosion = cv2.resize(erosion, (800, 650))
# Apply dilation
dilation = cv2.dilate(img, kernel, iterations=1)
resized_dilation = cv2.resize(dilation, (800, 650))

# Display the results
cv2.imshow('Original Image', resized_img)
cv2.imshow('Erosion', resized_erosion)
cv2.imshow('Dilation', resized_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()