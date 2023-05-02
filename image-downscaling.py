import cv2
img = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED)
print('Original Dimensions : ',img.shape)
scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Save resized image
cv2.imwrite("img/capA1-01.jpg", resized)

print('Resized Dimensions : ',resized.shape)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()