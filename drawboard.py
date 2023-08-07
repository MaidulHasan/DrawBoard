# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

from instructions import show_instructions
from options import show_control_panel


# -----------------------------------------------------------------------------------------------
###                                       DrawBoard GUI                                     ###
# -----------------------------------------------------------------------------------------------


# callback should go from the main window and various windows should be displayed under certain conditions

is_left_down = False
draw_mode = False


def mouse_callback(event, x, y, flags, userdata):
    global is_left_down

    if event == cv.EVENT_LBUTTONDBLCLK:
        pass


# showing the instructions window
instruction_window = show_instructions()

# creating named window as the gui black-board, binding the window for observing mouse events,
# and setting up mouse callback

drawboard_gui = np.zeros((500, 1000, 3), dtype=np.uint8)

cv.namedWindow("DrawBoard-GUI")

cv.setMouseCallback("DrawBoard-GUI", mouse_callback)

while True:
    show_control_panel()
    cv.imshow("DrawBoard-GUI", drawboard_gui)

    keyboard_input = cv.waitKey(100)
    if keyboard_input == (ord("q") or 27):
        break
    if keyboard_input == ord("c"):
        cv.destroyWindow(instruction_window)
    if keyboard_input == ord("d"):
        draw_mode = True
    if keyboard_input == ord("r"):
        draw_mode == False

cv.destroyAllWindows()
