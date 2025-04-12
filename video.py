import mediapipe as mp
import numpy as np
import cv2
import time
from const import IMAGE_PATH, ml, max_y, max_x
from video_tools import get_tool, get_tool_old, index_raised
import test


hands = mp.solutions.hands
hand_landmark = hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1)
draw = mp.solutions.drawing_utils



def get_image():
    try:
        return cv2.imread(IMAGE_PATH)
    except AttributeError:
        return "Файл не найден"


def null_mask():
    mask = np.ones((test.res)) * 255
    mask: np.ndarray = mask.astype('uint8')
    return mask


def break_changes(cap):
    cv2.destroyAllWindows()
    cap.release()


def change(frm, inf):
    rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
    op = hand_landmark.process(rgb)
    if op.multi_hand_landmarks:
        for i in op.multi_hand_landmarks:
            draw.draw_landmarks(frm, i, hands.HAND_CONNECTIONS)
            x, y = int(i.landmark[8].x * int(1920 * test.dif)), int(i.landmark[8].y * int(1100*test.dif))
            if max_x > x > ml and max_y > y:
                if inf.time_init:
                    inf.ctime = time.time()
                    inf.time_init = False
                ptime = time.time()
                cv2.circle(frm, (x, y), inf.rad, (0, 255, 255), 2)
                if inf.rad >= 6:
                    inf.rad -= 6
                if (ptime - inf.ctime) > 0.8:
                    inf.curr_tool_first = get_tool_old(x)
                    inf.time_init = True
                    inf.rad = 120
            else:
                inf.time_init = True
                inf.rad = 120
            inf.curr_tool = get_tool(i.landmark)
            if inf.curr_tool:
                inf.curr_tool_first = "select tool"
                inf.var_inits = False
            else:
                inf.curr_tool = inf.curr_tool_first
            xi, yi = int(i.landmark[12].x * int(1920 * test.dif)), int(i.landmark[12].y * int(1100*test.dif))
            y9 = int(i.landmark[9].y * int(1100*test.dif))
            x8, y8 = int(i.landmark[8].x * int(1920 * test.dif)), int(i.landmark[8].y * int(1100*test.dif))
            if inf.curr_tool:
                if inf.curr_tool == "erase":
                    x, y = int(i.landmark[11].x * int(1920 * test.dif)), int(i.landmark[11].y * int(1100*test.dif))
                    cv2.circle(frm, (x, y), 100, (0, 0, 0), -1)
                    cv2.circle(inf.mask, (x, y), 100, (255, 255, 255), -1)
                elif inf.curr_tool == "mask":
                    inf.mask = null_mask()
                    inf.curr_tool = 'select tool'
                elif inf.curr_tool == "draw":
                    if inf.prevx8 == 0 and inf.prevy8 == 0:
                        inf.prevx8 = x8
                        inf.prevy8 = y8
                        continue
                    cv2.line(inf.mask, (inf.prevx8, inf.prevy8), (x8, y8), (0, 0, 0), inf.thick)
                elif inf.curr_tool == "line":
                    if index_raised(yi, y9):
                        if not inf.var_inits:
                            inf.xii, inf.yii = x, y
                            inf.var_inits = True
                        cv2.line(frm, (inf.xii, inf.yii), (x, y), (50, 152, 255), inf.thick)
                    else:
                        if inf.var_inits:
                            cv2.line(inf.mask, (inf.xii, inf.yii), (x, y), (0, 0, 0), inf.thick)
                            inf.var_inits = False
                elif inf.curr_tool == "rectangle":
                    if index_raised(yi, y9):
                        if not inf.var_inits:
                            inf.xii, inf.yii = x, y
                            inf.var_inits = True
                        cv2.rectangle(frm, (inf.xii, inf.yii), (x, y), (0, 255, 255), inf.thick)
                    else:
                        if inf.var_inits:
                            cv2.rectangle(inf.mask, (inf.xii, inf.yii), (x, y), 0, inf.thick)
                            inf.var_inits = False
                elif inf.curr_tool == "circle":
                    if index_raised(yi, y9):
                        if not inf.var_inits:
                            inf.xii, inf.yii = x, y
                            inf.var_inits = True
                        cv2.circle(frm, (inf.xii, inf.yii), int(((inf.xii - x) ** 2 + (inf.yii - y) ** 2) ** 0.5),
                                   (255, 255, 0), inf.thick)
                    else:
                        if inf.var_inits:
                            cv2.circle(inf.mask, (inf.xii, inf.yii),
                                       int(((inf.xii - x) ** 2 + (inf.yii - y) ** 2) ** 0.5), (0, 255, 0), inf.thick)
                            inf.var_inits = False
            inf.prevx8, inf.prevy8 = x8, y8
    op = cv2.bitwise_and(frm, frm, mask=inf.mask)
    frm[:, :, 1] = op[:, :, 1]
    frm[:, :, 2] = op[:, :, 2]
    tools = get_image()
    if type(tools) is str:
        return tools
    frm[:max_y, ml:max_x] = cv2.addWeighted(src1=tools,
                                            alpha=0.7,
                                            src2=frm[:max_y, ml:max_x],
                                            beta=0.3,
                                            gamma=0)
    cv2.putText(frm,
                text=inf.curr_tool,
                org=(int(1202 * test.dif) + int(50*test.dif), int(100*test.dif)),  # 1202, 1372
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=int(4*test.dif),
                color=(0, 0, 0),
                thickness=2)
    return frm
