import cv2
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


def add_objects_to_the_frame(frame, objects):
    """
    Add rectangles of objects to the image

    Args:
        frame:
        objects:

    Returns:

    """

    for x, y, w, h in objects:
        print(x)
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    return frame


def detect_object_in_the_frame(frame, detector):
    """
    Detects the object using detector and adds them to the image

    Args:
        frame:
        detector:

    Returns:
        object_rectangles:
    """
    # convert image to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect the object_rectangles
    object_rectangles = detector.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=2)
    return object_rectangles


def resize_image(frame, factor):
    """
    Resize image

    Args:
        frame:
        factor:

    Returns:

    """
    frame = cv2.resize(frame, (int(frame.shape[1] * factor), int(frame.shape[0] * factor)))
    return frame


def scale_object_rectangles(object_rectangles, factor):
    """
    Simple scaling of the rectangles

    Args:
        object_rectangles(list of list): list of object_rectangles, where object rectangle is list of 4 numbers
        factor (float): scaling factor

    Returns:
        (list of list): scaled objects

    """
    return [[x * factor for x in obj] for obj in object_rectangles]





if __name__ == "__main__":

    # from https://github.com/opencv/opencv/tree/master/data/haarcascades
    # load face detector
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    img = cv2.imread("Nenad.jpg")
    objects = detect_object_in_the_frame(img, face_cascade)
    img = add_objects_to_the_frame(img, objects)
    resized = resize_image(img, 0.33)
    cv2.imshow("Gray", resized)
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    cv2.waitKey(0)
    # cv2.waitKey(2000)
    # cv2.destroyAllWindows()




    # https://realpython.com/python-matplotlib-guide/
    # https://matplotlib.org/api/axes_api.html
    # http://queirozf.com/entries/matplotlib-pylab-pyplot-etc-what-s-the-different-between-these
    # https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html



