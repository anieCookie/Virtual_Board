import cv2
from info import InfoForDraw
from video import change
import numpy as np
import test

# 27 - esc
# 13 - enter

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not capture.isOpened():
    print('камера не найдена')
    exit()

capture.set(cv2.CAP_PROP_FRAME_WIDTH, test.width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, test.height*4/3)
status = True
mask = np.ones(test.res) * 255
mask: np.ndarray = mask.astype('uint8')

info = InfoForDraw(mask=mask)

while True:
    _, frame = capture.read()
    if frame is None:
        print('камера не найдена')
        break

    frame = cv2.flip(frame, 1)

    if status:
        frame = change(frame, info)
        if type(frame) is str:
            print(frame)
            break

    cv2.imshow("camera", frame)

    match cv2.waitKey(1):
        case 13:
            if status:
                status = False
            else:
                status = True
        case 27:
            break
