import os
import cv2
import sys
import glob

# img = cv2.imread(r'C:\supreme-engine\Python_mega_course\15_170_Moving object detection\galaxy.jpg', -1)
# img = cv2.imread('galaxy.jpg', 0)
# print(type(img))
# print(img.shape)
# print(img.ndim)
#
# resized_image = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
# cv2.imwrite('Galaxy_resized.jpg', resized_image)

# # method #1
# original_folder = r'C:\supreme-engine\Python_mega_course\15_170_Moving object detection\sample-images'
# folder_to_write = r'C:\supreme-engine\Python_mega_course\15_170_Moving object detection\sample-images-resized'
# os.mkdir(folder_to_write)
# for root, dirs, files in os.walk(original_folder, topdown=False):
#     for name in files:
#         fullname = os.path.join(root, name)
#         img = cv2.imread(fullname)
#         resized_image = cv2.resize(img, (100, 100))
#         cv2.imwrite(os.path.join(folder_to_write, name), resized_image)

# method #2
original_folder = r'C:\supreme-engine\Python_mega_course\15_170_Moving object detection\sample-images'
folder_to_write = r'C:\supreme-engine\Python_mega_course\15_170_Moving object detection\sample-images-resized'
if not os.path.exists(folder_to_write):
    os.mkdir(folder_to_write)
images = glob.glob(os.path.join(original_folder, "*.jpg"))
for filename in images:
    a, just_name = os.path.split(filename)
    img = cv2.imread(filename)
    resized_image = cv2.resize(img, (100, 100))
    # cv2.imshow("Galaxy", resized_image)
    # cv2.waitKey(3000)
    # cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(folder_to_write, just_name), resized_image)
