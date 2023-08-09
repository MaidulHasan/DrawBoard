# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###   Controller components of the program (color mixer, brush size, drawing pen status)    ###
# -----------------------------------------------------------------------------------------------

# -------------------------------------
### create the Control Panel window
# -------------------------------------

cv.namedWindow("Control_Panel", flags=cv.WINDOW_AUTOSIZE)

# -----------------
### Color Mixer
# -----------------

# create the color_sample image to be shown in the control panel window
color_sample = np.zeros((100, 400, 3), dtype=np.uint8)


def get_color_component_values_from_tackbars():
    r = cv.getTrackbarPos("R", "Control_Panel")
    g = cv.getTrackbarPos("G", "Control_Panel")
    b = cv.getTrackbarPos("B", "Control_Panel")
    return (b, g, r)


def color_mixer():
    b, g, r = get_color_component_values_from_tackbars()
    color_sample[:, :, 0] = b
    color_sample[:, :, 1] = g
    color_sample[:, :, 2] = r
    return color_sample


# from the rgb trackbar position change callback function
# we return the result from color_mixer() i.e, the color_sample image so that color_sample
# image will be continuously updated as the rgb trackbar positions changes
def rgb_callback(pos, userdata=0):
    return color_mixer()


cv.createTrackbar("R", "Control_Panel", 160, 255, rgb_callback)
cv.createTrackbar("G", "Control_Panel", 160, 255, rgb_callback)
cv.createTrackbar("B", "Control_Panel", 160, 255, rgb_callback)


# -----------------------------
### brush size and brush color
# -----------------------------


def nothing(pos):
    pass


cv.createTrackbar("Paint Brush Size: ", "Control_Panel", 1, 5, nothing)


def paint_brush_size():
    return cv.getTrackbarPos("Paint Brush Size: ", "Control_Panel")


def color_to_draw_with():
    return get_color_component_values_from_tackbars()


# ----------------------------------------------------------------
### Show status (whether drawing tool is engaged or released)
# ----------------------------------------------------------------
def update_drawing_tool_status(pos):
    return cv.setTrackbarPos(
        "Drawing Tool Dis-engaged/Released (0)\nDrawing Tool Engaged, Draw Mode (1): ",
        "Control_Panel",
        pos,
    )


cv.createTrackbar(
    "Drawing Tool Dis-engaged/Released (0)\nDrawing Tool Engaged, Draw Mode (1): ",
    "Control_Panel",
    1,
    1,
    update_drawing_tool_status,
)


# --------------------------------------------
### Show the control panel
# --------------------------------------------
def show_control_panel():
    # the trackbar callback function will automatically update 'color' and show it using this imshow
    # function when called within a 'while True' loop in the main DrawBoard GUI file
    cv.imshow("Control_Panel", color_sample)
