import cv2
import time
from face_detector import detect_object_in_the_frame
from face_detector import add_objects_to_the_frame
from face_detector import resize_image
from face_detector import scale_object_rectangles

# filename, cascade, transp = 'Sample-videos/Nenad_face.mov', "haarcascade_frontalface_default.xml", True
filename, cascade, transp = 'Sample-videos/essex_at_day.mov', 'cars.xml', False
write_to_file = False

##
face_cascade = cv2.CascadeClassifier(cascade)
video = cv2.VideoCapture(filename)

# frame_width = video.get(3)
# frame_height = video.get(4)
# print(frame_width)
# print(frame_height)

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
    frame_small = resize_image(frame, 0.16)
    object_rectangles = detect_object_in_the_frame(frame_small, face_cascade)
    object_rectangles = scale_object_rectangles(object_rectangles, 2)
    frame_medium = resize_image(frame, 0.33)
    frame_medium = add_objects_to_the_frame(frame_medium, object_rectangles)
    cv2.imshow("Capturing", frame_medium)

    if counter == 1:
        # Default resolutions of the frame are obtained.The default resolutions are system dependent.
        # We convert the resolutions from float to integer.
        frame_width = frame_medium.shape[1]
        frame_height = frame_medium.shape[0]

        # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
        # Define the fps to be equal to 10. Also frame size is passed.
        out = cv2.VideoWriter('Sample-videos/outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (frame_width, frame_height))
        if write_to_file:
            out.write(frame_medium)
    # elif not counter % 5 == 0:
    #     continue
    counter += 1

    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()


