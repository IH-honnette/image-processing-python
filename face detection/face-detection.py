# import required libraries
import cv2

# read the input image
img = cv2.imread('image-3.jpg')

# convert to grayscale of each frames
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# read the haarcascades to detect the faces in an image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# detects faces in the input image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                      flags=cv2.CASCADE_SCALE_IMAGE)
print('Number of detected faces:', len(faces))

# loop over all detected faces
if len(faces) > 0:
    for i, (x, y, w, h) in enumerate(faces):
        # To draw a rectangle in a face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        face = img[y:y + h, x:x + w]
        cv2.imshow(f"Cropped Face {i}", face)
        cv2.imwrite(f'face{i}.jpg', face)
        print(f"face{i}.jpg is saved")

# display the image with detected faces
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()