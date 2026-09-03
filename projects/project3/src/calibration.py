import math
import cv2

from src.display_utils import (
    calculate_display_scale,
    resize_for_display,
    display_to_original_point,
)


def calculate_scale(
    point1,
    point2,
    real_distance
):
    x1, y1 = point1
    x2, y2 = point2

    pixel_distance = math.sqrt(
        (x2 - x1) ** 2
        +
        (y2 - y1) ** 2
    )

    if pixel_distance == 0:
        raise ValueError(
            "Calibration points must be different."
        )

    if real_distance <= 0:
        raise ValueError(
            "Real distance must be positive."
        )

    scale = real_distance / pixel_distance

    return scale


def pixel_to_physical(
    pixel_point,
    origin_pixel,
    scale
):
    if scale <= 0:
        raise ValueError(
            "Scale must be positive."
        )

    x_pixel, y_pixel = pixel_point
    x_origin, y_origin = origin_pixel

    physical_x = scale * (
        x_pixel - x_origin
    )

    physical_y = scale * (
        y_origin - y_pixel
    )

    return physical_x, physical_y


def select_calibration_points(frame):
    points = []

    display_scale = calculate_display_scale(
        frame
    )

    display_frame = resize_for_display(
        frame,
        display_scale
    )

    def mouse_callback(
        event,
        x,
        y,
        flags,
        param
    ):
        nonlocal display_frame

        if (
            event == cv2.EVENT_LBUTTONDOWN
            and len(points) < 2
        ):
            original_point = (
                display_to_original_point(
                    (x, y),
                    display_scale
                )
            )

            points.append(
                original_point
            )

            cv2.circle(
                display_frame,
                (x, y),
                5,
                (0, 255, 255),
                -1
            )

            cv2.putText(
                display_frame,
                f"P{len(points)}",
                (x + 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

    window_name = (
        "Select Calibration Points"
    )

    cv2.namedWindow(
        window_name
    )

    cv2.setMouseCallback(
        window_name,
        mouse_callback
    )

    while len(points) < 2:
        cv2.imshow(
            window_name,
            display_frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            cv2.destroyWindow(
                window_name
            )

            raise RuntimeError(
                "Calibration cancelled."
            )

    cv2.imshow(
        window_name,
        display_frame
    )

    cv2.waitKey(300)

    cv2.destroyWindow(
        window_name
    )

    return points[0], points[1]


def select_origin(frame):
    origin = None

    display_scale = calculate_display_scale(
        frame
    )

    display_frame = resize_for_display(
        frame,
        display_scale
    )

    def mouse_callback(
        event,
        x,
        y,
        flags,
        param
    ):
        nonlocal origin
        nonlocal display_frame

        if event == cv2.EVENT_LBUTTONDOWN:
            origin = display_to_original_point(
                (x, y),
                display_scale
            )

            display_frame = resize_for_display(
                frame,
                display_scale
            )

            cv2.circle(
                display_frame,
                (x, y),
                6,
                (0, 0, 255),
                -1
            )

            cv2.putText(
                display_frame,
                "Origin",
                (x + 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

    window_name = "Select Origin"

    cv2.namedWindow(
        window_name
    )

    cv2.setMouseCallback(
        window_name,
        mouse_callback
    )

    while origin is None:
        cv2.imshow(
            window_name,
            display_frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            cv2.destroyWindow(
                window_name
            )

            raise RuntimeError(
                "Origin selection cancelled."
            )

    cv2.imshow(
        window_name,
        display_frame
    )

    cv2.waitKey(500)

    cv2.destroyWindow(
        window_name
    )

    return origin