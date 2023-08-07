# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###                         Show status (Double clicked, Start drawing /
#                        Double click released, double click to start drawing)              ###
# -----------------------------------------------------------------------------------------------


def show_status(can_draw=False, click_released=False):
    status = np.zeros((100, 400, 3), dtype=np.uint8)

    if can_draw is True:
        cv.putText(
            status,
            "Double clicked",
            (30, 50),
            cv.FONT_HERSHEY_PLAIN,
            1.2,
            (0, 255, 0),
            2,
        )
        cv.putText(
            status,
            "You can start drawing now",
            (30, 80),
            cv.FONT_HERSHEY_PLAIN,
            1.2,
            (0, 255, 0),
            2,
        )

    if click_released is True:
        pass

    cv.imshow("Status", status)
