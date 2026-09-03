import cv2

from src.display_utils import (
    calculate_display_scale,
    resize_for_display,
    display_to_original_bbox,
)


def select_and_initialize_tracker(frame):
    display_scale = calculate_display_scale(
        frame
    )

    display_frame = resize_for_display(
        frame,
        display_scale
    )

    display_bbox = cv2.selectROI(
        "Select Object",
        display_frame,
        fromCenter=False,
        showCrosshair=True
    )

    cv2.destroyWindow(
        "Select Object"
    )

    x, y, w, h = display_bbox

    if w == 0 or h == 0:
        raise ValueError(
            "ROI selection was cancelled or invalid."
        )

    original_bbox = (
        display_to_original_bbox(
            display_bbox,
            display_scale
        )
    )

    x, y, w, h = original_bbox

    frame_height, frame_width = (
        frame.shape[:2]
    )

    x = max(
        0,
        min(x, frame_width - 1)
    )

    y = max(
        0,
        min(y, frame_height - 1)
    )

    w = min(
        w,
        frame_width - x
    )

    h = min(
        h,
        frame_height - y
    )

    original_bbox = (
        x,
        y,
        w,
        h
    )

    tracker = (
        cv2.TrackerCSRT_create()
    )

    success = tracker.init(
        frame,
        original_bbox
    )

    if success is False:
        raise RuntimeError(
            "Failed to initialize tracker."
        )

    return tracker, original_bbox