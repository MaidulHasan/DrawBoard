# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###             Show instructions (press "d" to engage drawing pen, "r" to release,
#                     and "q" to quit and save current window status)                       ###
# -----------------------------------------------------------------------------------------------


instructions_window = np.zeros((140, 500, 3), dtype=np.uint8)
instructions = [
    "Instructions on How to Use the Program",
    "___________________________________",
    "Press 'd' to engage the drawing tool.",
    "Press 'r' to release the drawing tool.",
    "Press 'q' to save current view and exit application.",
    "Press 'c' to close the instructions window.",
]

text_pos_y = 30

for line in instructions:
    cv.putText(
        instructions_window,
        line,
        (30, text_pos_y),
        cv.FONT_HERSHEY_PLAIN,
        1.2,
        (0, 255, 0),
        2,
    )
    text_pos_y += 20


def show_instructions():
    cv.imshow("Instructions on How to Use the Program", instructions_window)
    return "Instructions on How to Use the Program"
