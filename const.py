import cv2
import test
if test.dif == 0.6666666666666666:
    IMAGE_PATH = r"salam.png"
else:
    IMAGE_PATH = r"toolsold.png"


ml = int((550*float(test.dif)))
max_x, max_y = int(575*test.dif) + ml, int(150*test.dif)
