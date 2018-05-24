import cv2
import time


video = cv2.VideoCapture('movie.MOV')
counter = 1
while True:
    check, frame = video.read()

    frame = cv2.transpose(frame)
    frame = cv2.resize(frame, (int(frame.shape[1]/3), int(frame.shape[0]/3)))
    counter += 1
    # time.sleep(3)
    # print(check)
    # print(frame)

    if not check:
        print('End of video')
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(counter)
video.release()
cv2.destroyAllWindows()

