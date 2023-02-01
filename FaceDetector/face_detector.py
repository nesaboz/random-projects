import cv2
import datetime
import numpy as np


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


def detect_one_frame(frame, cascade, transp=False, detection_rescale_factor=5):

    if transp:
        frame = cv2.transpose(frame)

    # make image smaller for faster face detection
    frame_small = resize_image(frame, 1 / detection_rescale_factor)

    # covert to grayscale
    gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

    # detect the cascade
    objects = cascade.detectMultiScale(gray, 1.1, 4)

    # resize rectangles to the original image size:
    objects = scale_object_rectangles(objects, detection_rescale_factor)

    # draw the rectangle around each face
    frame = add_objects_to_the_frame(frame, objects)

    return frame


def detect_video(input_filename, output_filename, cascade_filename, transp=False, detection_rescale_factor=5):

    cascade = cv2.CascadeClassifier(cascade_filename)

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

    while True:
        check, frame = video.read()
        if not check:
            print('End of video')
            break

        frame = detect_one_frame(frame, cascade, transp=transp, detection_rescale_factor=detection_rescale_factor)

        # display
        cv2.imshow('Press q to stop', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        output.write(frame)

    video.release()
    output.release()
    cv2.destroyAllWindows()


def test_face_detection():
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    frame = np.load('face.npy')
    frame = detect_one_frame(frame, cascade)
    cv2.imshow('Press any key to close', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_car_detection():
    # WIP
    # TODO to build our own haar cascade: https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
    cascade = cv2.CascadeClassifier('cars.xml')
    frame = np.load('car.npy')

    detection_rescale_factor = 5

    # make image smaller for faster face detection
    frame_small = resize_image(frame, 1 / detection_rescale_factor)

    # covert to grayscale
    gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

    # detect the cascade
    objects = cascade.detectMultiScale(gray, 100, 4, minSize=(200, 200))

    # resize rectangles to the original image size:
    objects = scale_object_rectangles(objects, detection_rescale_factor)

    # draw the rectangle around each face
    frame = add_objects_to_the_frame(frame, objects)

    cv2.imshow('Press any key to close', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize_video(input_filename, output_filename, rescale_factor=5):

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
    counter = 0
    while True:
        check, frame = video.read()
        counter += 1
        if counter % 100 == 0:
            print(counter)

        if not check:
            print('End of video')
            break

        frame = resize_image(frame, rescale_factor)

        # # display
        # cv2.imshow('Press q to stop', frame)
        #
        # key = cv2.waitKey(1)
        # if key == ord('q'):
        #     break

        output.write(frame)

    video.release()
    output.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # filename = capture_video('face_input')
    detect_video('face_input', 'face_output', 'haarcascade_frontalface_default.xml')

    # detect_video('essex_at_day', 'essex_at_day_output', 'cars.xml')
    # test_face_detection()
    # test_car_detection()
    # resize_video('essex_at_day', 'essex_by_day_resized', 0.2)
