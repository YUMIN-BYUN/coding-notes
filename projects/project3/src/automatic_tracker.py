import cv2


def select_and_initialize_tracker(frame):
    bbox = cv2.selectROI(
        "Select Object",
        frame,
        fromCenter=False,
        showCrosshair=True
    )

    cv2.destroyWindow("Select Object")

    x, y, w, h = bbox

    if w == 0 or h == 0:
        raise ValueError("ROI selection was cancelled or invalid.")

    tracker = cv2.TrackerCSRT_create()

    success = tracker.init(frame, bbox)

    if success is False:
        raise RuntimeError("Failed to initialize tracker.")

    return tracker, bbox