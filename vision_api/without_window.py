import cv2

# Load the Haar Cascade classifier for human detection
haar_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Define the font and the starting count
font = cv2.FONT_HERSHEY_SIMPLEX
count = 0

while True:
    # Read a frame from the video capture object
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect humans using the Haar Cascade classifier
    humans = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Count the number of people
    count = len(humans)

    # Print the number of people counted
    print('People Count:', count)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
