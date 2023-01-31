import cv2
import datetime


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


def capture_video(output_filename):

    now_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f'{now_str}_{output_filename}.mov'

    video = cv2.VideoCapture(0)
    width, height = int(video.get(3)), int(video.get(4))
    output = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    while True:
        check, frame = video.read()
        cv2.imshow("Press q to stop", frame)
        output.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    output.relase()
    cv2.destroyAllWindows()

    return output_filename


def detect_face(input_filename, output_filename, transp=False, detection_rescale_factor=5):

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    if input_filename[-4:] != '.mov':
        input_filename += '.mov'
    if output_filename[-4:] != '.mov':
        output_filename += '.mov'

    video = cv2.VideoCapture(input_filename)
    width, height = int(video.get(3)), int(video.get(4))
    output = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    # Check if camera opened successfully
    if not video.isOpened():
        print("Unable to read camera feed.")
        return

    counter = 1
    while True:
        check, frame = video.read()
        if not check:
            print('End of video')
            break
        if transp:
            frame = cv2.transpose(frame)

        # make image smaller for faster face detection
        frame_small = resize_image(frame, 1 / detection_rescale_factor)

        # covert to grayscale
        gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

        # detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # resize rectangles to the original image size:
        faces = scale_object_rectangles(faces, detection_rescale_factor)

        # draw the rectangle around each face
        frame = add_objects_to_the_frame(frame, faces)

        # display
        cv2.imshow('Press q to stop', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        output.write(frame)

    video.release()
    output.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    filename = capture_video('input')
    detect_face('input', 'output')
