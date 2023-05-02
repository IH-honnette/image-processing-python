import cv2
img = cv2.imread("lena.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
resized = cv2.resize(img_gray, (800, 650))
cv2.imshow("GrayLena",resized) 
cv2.waitKey(0)
cv2.destroyAllWindows()