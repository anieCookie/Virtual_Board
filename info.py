from dataclasses import dataclass
import numpy as np


@dataclass
class InfoForDraw:
    mask: np.ndarray
    ctime: float = 0
    curr_tool: str = "select tool"
    curr_tool_first: str = "select tool"
    time_init: bool = True
    var_inits: bool = False
    prevy8: float = 0
    prevx8: float = 0
    rad: float = 40
    xii: float = 0
    yii: float = 0
    thick: int = 4
