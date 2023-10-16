import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

# Capture and display the image
ret, frame = cap.read()

cv2.imshow("Image", frame)
cv2.imwrite("kavach.jpeg",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Release the camera
cap.release()
