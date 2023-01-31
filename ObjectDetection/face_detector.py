import cv2

def resize_image(frame, factor):
    return cv2.resize(frame, (int(frame.shape[1] * factor), int(frame.shape[0] * factor)))


def add_objects_to_the_frame(frame, objects):
    for x, y, w, h in objects:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
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


if __name__ == '__main__':

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    transp = False
    video = cv2.VideoCapture('input.mov')
    detection_rescale_factor = 5

    width, height= int(video.get(3)), int(video.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
    # Define the fps to be equal to 10. Also frame size is passed.
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter('output.mov', fourcc, 30, (width, height))
    # Check if camera opened successfully
    if not video.isOpened():
        print("Unable to read camera feed")

    counter = 1
    while True:
        check, frame = video.read()
        if not check:
            print('End of video')
            break
        if transp:
            frame = cv2.transpose(frame)

        # make image smaller for faster face detection
        frame_small = resize_image(frame, 1/detection_rescale_factor)

        # covert to grayscale
        gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

        # detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # resize rectangles to the original image size:
        faces = scale_object_rectangles(faces, detection_rescale_factor)

        # draw the rectangle around each face
        frame = add_objects_to_the_frame(frame, faces)

        # display
        cv2.imshow('img', frame)
        # Stop if escape key is pressed
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        output.write(frame)

    video.release()
    output.release()
    cv2.destroyAllWindows()


