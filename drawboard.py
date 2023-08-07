# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from status import show_status


# -----------------------------------------------------------------------------------------------
###                                       DrawBoard GUI                                     ###
# -----------------------------------------------------------------------------------------------


# callback should go from the main window and various windows should be displayed under certain conditions

is_left_down = False


def mouse_callback(event, x, y, flags, userdata):
    global is_left_down

    if event == cv.EVENT_LBUTTONDBLCLK:
        show_status(can_draw=True)


# creating named window as the gui black-board, binding the window for observing mouse events,
# and setting up mouse callback

drawboard_gui = np.zeros((500, 1000, 3), dtype=np.uint8)

cv.namedWindow("DrawBoard-GUI")

cv.setMouseCallback("DrawBoard-GUI", mouse_callback)

while True:
    cv.imshow("DrawBoard-GUI", drawboard_gui)

    keyboard_input = cv.waitKey(100)
    if keyboard_input == (ord("q") or 27):
        break

cv.destroyAllWindows()
