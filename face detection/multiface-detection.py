import cv2

# Load the pre-trained model for face detection
model_path = 'opencv_face_detector_uint8.pb'
config_path = 'opencv_face_detector.pbtxt'
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

# Load the image
image = cv2.imread('image-3.jpg')

# Create a blob from the image
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104, 177, 123))

# Set the input to the network
net.setInput(blob)

# Perform face detection
detections = net.forward()

# Iterate over the detected faces
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    # Filter out weak detections by confidence threshold
    if confidence > 0.5:
        box = detections[0, 0, i, 3:7] * [image.shape[1], image.shape[0], image.shape[1], image.shape[0]]
        (startX, startY, endX, endY) = box.astype(int)

        # Draw a rectangle around the face
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
         # Crop the detected face
        face = image[startY:endY, startX:endX]

        # Save the cropped face as a separate image
        cv2.imshow(f"Cropped Face {i}", face)
        cv2.imwrite(f'cropped-multifaces/cropedFace_{i}.jpg', face)
        print(f"croped-face{i}.jpg is saved")

# Display the image with the detected faces
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()