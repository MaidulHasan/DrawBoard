# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###   Code that will do the drawing (mouse events are handled in the drawboard.py file)     ###
# -----------------------------------------------------------------------------------------------
def draw(pos_to_start, pos_to_end, canvas, color, thickness):
    # changes the canvas in place
    cv.line(canvas, pos_to_start, pos_to_end, color, thickness)
    return canvas
