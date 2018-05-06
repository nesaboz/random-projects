import cv2
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


# from https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("Nenad.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
for x, y, w, h in faces:
    print(x)
    img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 3)
    # input("Press Enter to continue...")


resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
cv2.imshow("Gray", resized)
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
cv2.waitKey(0)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()



# https://realpython.com/python-matplotlib-guide/
# https://matplotlib.org/api/axes_api.html
# http://queirozf.com/entries/matplotlib-pylab-pyplot-etc-what-s-the-different-between-these
# https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html



