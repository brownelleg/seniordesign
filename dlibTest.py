import cv2
import dlib



# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# read the image
img = cv2.imread("Karis.5MeterOptics.jpg")

# Convert image into grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# Use detector to find landmarks
faces = detector(gray)

for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point

    dimensions = img.shape

    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]

    print('Image Dimension    : ', dimensions)
    print('Image Height       : ', height)
    print('Image Width        : ', width)
    print('Number of Channels : ', channels)

    # Look for the landmarks
    landmarks = predictor(image=gray, box=face)
    x_right = landmarks.part(34).x
    y_right = landmarks.part(34).y

    print('X coordinate: ' + str(x_right) + '\nY coordinate: ' + str(y_right))

    # Draw a circle
    cv2.circle(img=img, center=(x_right, y_right), radius=5, color=(0, 255, 0), thickness=-1)

# show the image
cv2.imshow(winname="Face", mat=img)

# Wait for a key press to exit
cv2.waitKey(delay=0)

# Close all windows
cv2.destroyAllWindows()
