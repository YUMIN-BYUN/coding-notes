import cv2


DEFAULT_MAX_WIDTH = 1200
DEFAULT_MAX_HEIGHT = 700


def calculate_display_scale(
    frame,
    max_width=DEFAULT_MAX_WIDTH,
    max_height=DEFAULT_MAX_HEIGHT
):
    height, width = frame.shape[:2]

    width_scale = max_width / width
    height_scale = max_height / height

    display_scale = min(
        1.0,
        width_scale,
        height_scale
    )

    return display_scale


def resize_for_display(
    frame,
    display_scale
):
    if display_scale == 1.0:
        return frame.copy()

    height, width = frame.shape[:2]

    display_width = int(
        width * display_scale
    )

    display_height = int(
        height * display_scale
    )

    resized_frame = cv2.resize(
        frame,
        (
            display_width,
            display_height
        )
    )

    return resized_frame


def display_to_original_point(
    display_point,
    display_scale
):
    x_display, y_display = display_point

    x_original = int(
        round(
            x_display / display_scale
        )
    )

    y_original = int(
        round(
            y_display / display_scale
        )
    )

    return (
        x_original,
        y_original
    )


def display_to_original_bbox(
    display_bbox,
    display_scale
):
    x, y, w, h = display_bbox

    x_original = int(
        round(x / display_scale)
    )

    y_original = int(
        round(y / display_scale)
    )

    w_original = int(
        round(w / display_scale)
    )

    h_original = int(
        round(h / display_scale)
    )

    return (
        x_original,
        y_original,
        w_original,
        h_original
    )