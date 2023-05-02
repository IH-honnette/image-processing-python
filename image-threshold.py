import cv2

# Load the image in grayscale
img = cv2.imread('lena.jpg', 0)

# Apply thresholding using a threshold value of 127
# Pixels with a value less than 127 will be set to 0
# Pixels with a value greater than or equal to 127 will be set to 255
th, threshed = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Display the thresholded image
resized = cv2.resize(threshed, (800, 650))
cv2.imshow('Thresholded Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
