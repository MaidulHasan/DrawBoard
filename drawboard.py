# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

from instructions import show_instructions
from options import show_control_panel
from options import color_to_draw_with
from options import paint_brush_size
from options import update_drawing_tool_status
from queue_ import Queue
from draw import draw


# -----------------------------------------------------------------------------------------------
###                                       DrawBoard GUI                                     ###
# -----------------------------------------------------------------------------------------------

# creating the named window DrawBoard-GUI
cv.namedWindow("DrawBoard-GUI", flags=cv.WINDOW_AUTOSIZE)

# creating the initial black board to show on the DrawBoard-GUI window
drawboard_gui = np.zeros((500, 1000, 3), dtype=np.uint8)


# global variables
is_left_down = False
mouse_X_and_mouse_Y = Queue()
color = (
    160,
    160,
    160,
)  # the default position used in the rgb trackbars when initiating
thickness = 1  # the default brush thickness when first initiating the DrawBoard-GUI
is_drawing_pen_engaged = True

# callback should go from the main window i.e, the DrawBoard-GUI window and
# various other windows (e.g, instructions window, control panel window etc.)
# should only be displayed under certain conditions


def mouse_callback(event, x, y, flags, userdata):
    global is_left_down, mouse_X_and_mouse_Y, color, thickness, drawboard_gui

    # doesn't draw if thickness == 0
    if thickness == 0:
        return drawboard_gui

    # draw only if drawing pen is engaged
    if is_drawing_pen_engaged is False:
        return drawboard_gui

    if event == cv.EVENT_LBUTTONDOWN:
        is_left_down = True
        # initialize a-new to avoid joining of two points from two different draws
        # (last point of the prev draw and first point of the current draw) with straight lines
        mouse_X_and_mouse_Y = Queue()

    if is_left_down == True and event == cv.EVENT_LBUTTONUP:
        is_left_down = False

    if is_left_down == True and event == cv.EVENT_MOUSEMOVE:
        pos_to_finish_drawing = (x, y)

        if mouse_X_and_mouse_Y.read() is None:
            mouse_X_and_mouse_Y.enqueue((x, y))
        else:
            pos_to_start_drawing = mouse_X_and_mouse_Y.dequeue()
            mouse_X_and_mouse_Y.enqueue(pos_to_finish_drawing)

            # the draw function changes the canvas in-place. So we pass drawboard_gui image as the
            # canvas and reassign it to the drawboard_gui image

            drawboard_gui = draw(
                pos_to_start_drawing,
                pos_to_finish_drawing,
                drawboard_gui,
                color,
                thickness,
            )
    # we return the drawboard_gui image after any mouse event callback since we want to
    # continuously update the drawboard_gui image that is shown on the DrawBoard-GUI window
    return drawboard_gui


# setting up mouse callback on the DrawBoard-GUI window
cv.setMouseCallback("DrawBoard-GUI", mouse_callback)


# showing the instructions window
instruction_window = show_instructions()


while True:
    # show the drawboard_gui on the DrawBoard-GUI window
    cv.imshow("DrawBoard-GUI", drawboard_gui)

    # showing the control panel (we do this inside the while loop since we want to be
    # kept updated on the control panel changes and always stay displayed while the
    # application is running)
    show_control_panel()

    # get the color to draw with on the gui
    color = color_to_draw_with()
    # get the line thickness
    thickness = paint_brush_size()

    # wait for any keyboard input and act accordingly
    keyboard_input = cv.waitKey(100)

    if keyboard_input == (ord("q") or 27):
        final_drawboard_gui_status = drawboard_gui
        break

    if keyboard_input == ord("c"):
        cv.destroyWindow(instruction_window)

    if keyboard_input == ord("d"):
        update_drawing_tool_status(1)
        is_drawing_pen_engaged = True

    if keyboard_input == ord("r"):
        update_drawing_tool_status(0)
        is_drawing_pen_engaged = False

cv.destroyAllWindows()
