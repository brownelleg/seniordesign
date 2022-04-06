import cv2
import dlib
import time
from PIL import Image
from numpy import array

class OpticPixels:
    @staticmethod
    def getOpticNostrilPixel(opticsFilename: str):
        # Initialize for troubleshooting
        pixelLocations = [0, 0]

        # Load the detector
        detector = dlib.get_frontal_face_detector()

        # Load the predictor
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        # read the image
        img = cv2.imread(opticsFilename)

        # Convert image into grayscale
        gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

        # Use detector to find landmarks
        faces = detector(gray)

        for face in faces:
        #    x1 = face.left()  # left point
        #    y1 = face.top()  # top point
        #    x2 = face.right()  # right point
        #    y2 = face.bottom()  # bottom point

        #    dimensions = img.shape

            # height, width, number of channels in image
        #    height = img.shape[0]
        #    width = img.shape[1]
        #    channels = img.shape[2]

            # Look for the landmarks
            landmarks = predictor(image=gray, box=face)
            x_right = landmarks.part(34).x
            y_right = landmarks.part(34).y
            pixelLocations = [x_right, y_right]

            # Draw a circle
            #cv2.circle(img=img, center=(x_right, y_right), radius=5, color=(0, 255, 0), thickness=-1)

        # show the image
        #cv2.imshow(winname="Face", mat=img)
        #cv2.imwrite('/home/pi/libseek-thermal-master/build/examples/image.png', img)

        # Wait for a key press to exit
        #cv2.waitKey(delay=0)

        # Close all windows
        #cv2.destroyAllWindows()

        return pixelLocations

    @staticmethod
    def takeOpticImage():
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        time.sleep(0.1)

        for i in range(6):
            return_value, image = camera.read()
            cv2.imwrite("im" + str(i+1) + ".png", image)
            time.sleep(5.02)

    @staticmethod
    def takeSingleOpticImage(i: int):
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        time.sleep(0.1)
        return_value, image = camera.read()
        cv2.imwrite("image" + str(i) + ".png", image)

    @staticmethod
    def checkImageDifference(filename: str):

        im = Image.open(filename)
        ar = array(im)
        total = 0

        for i in range(18):
            for j in range(18):
                total = total + ar[(i + 1) * 24, (j + 1) * 32]

        return sum(total)
