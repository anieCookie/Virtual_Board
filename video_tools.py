from const import ml
from test import dif


def get_tool_old(x1):
    if x1 < int(151*dif) + ml:
        return "line" #Прямая линия
    elif x1 < int(301*dif) + ml:
        return "rectangle" #Прямоугольник
    elif x1 < int(451*dif) + ml:
        return "circle" #Круг
    else:
        return "mask" #Стереть всё


def index_raised(y2, y1):
    if (y1 - y2) > int(120*dif):
        return True
    return False


def get_tool(landmarks):
    """if (landmarks[12].y < landmarks[8].y < landmarks[20].y
            and landmarks[12].y < landmarks[16].y < landmarks[4].y
            and landmarks[16].x * 1920 - landmarks[12].x * 1920 < 151
            and landmarks[12].x * 1920 - landmarks[8].x * 1920 < 151
            and landmarks[6].x * 1920 - landmarks[4].x * 1920 < 190
            and landmarks[5].y * 1100 - landmarks[8].y * 1100 > 150
            and landmarks[9].y * 1100 - landmarks[12].y * 1100 > 150
            and landmarks[13].y * 1100 - landmarks[16].y * 1100 > 150
            and landmarks[1].y * 1100 - landmarks[4].y * 1100 > 150
            and landmarks[17].y * 1100 - landmarks[20].y * 1100 > 150):"""
    if (landmarks[16].x * int(1920*dif) - landmarks[12].x * int(1920*dif) < int(151*dif)
            and landmarks[12].x * int(1920*dif) - landmarks[8].x * int(1920*dif) < int(151*dif)
            and landmarks[6].x * int(1920*dif) - landmarks[4].x * int(1920*dif) < int(190*dif)
            and landmarks[5].y * int(1100*dif) - landmarks[8].y * int(1100*dif) > int(150*dif)
            and landmarks[9].y * int(1100*dif) - landmarks[12].y * int(1100*dif) > int(150*dif)
            and landmarks[13].y * int(1100*dif) - landmarks[16].y * int(1100*dif) > int(150*dif)
            and landmarks[1].y * int(1100*dif) - landmarks[4].y * int(1100*dif) > int(150*dif)
            and landmarks[17].y * int(1100*dif) - landmarks[20].y * int(1100*dif) > int(150*dif)):
        return "erase"
    elif (landmarks[8].y < landmarks[16].y
            and landmarks[8].y < landmarks[20].y
            and landmarks[8].y < landmarks[4].y
            and landmarks[8].y < landmarks[12].y
            and landmarks[9].y * int(1100*dif) - landmarks[12].y * int(1100*dif) < int(120*dif)
            and landmarks[13].y * int(1100*dif) - landmarks[16].y * int(1100*dif) < int(120*dif)
            and landmarks[17].y * int(1100*dif) - landmarks[20].y * int(1100*dif) < int(120*dif)
            and landmarks[5].x * int(1920*dif) - landmarks[4].x * int(1920*dif) > int(100*dif)):
        return 'draw'
    else:
        return None
