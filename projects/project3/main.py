import cv2

from src.video_loader import VideoLoader
from src.tracking_data import (
    save_tracking_data
)
from src.automatic_tracker import (
    select_and_initialize_tracker
)
from src.calibration import (
    calculate_scale,
    pixel_to_physical,
    select_calibration_points,
    select_origin,
)
from src.display_utils import (
    calculate_display_scale,
    resize_for_display,
    display_to_original_point,
)

from src.motion_plotting import (
    plot_motion,
)


tracking_data = []
automatic_tracking_data = []


def show_video_frame(
    frame,
    display_scale
):
    display_frame = resize_for_display(
        frame,
        display_scale
    )

    cv2.imshow(
        "Video",
        display_frame
    )


def mouse_callback(
    event,
    x,
    y,
    flags,
    param
):
    if event == cv2.EVENT_LBUTTONDOWN:

        frame_index = param[
            "frame_index"
        ]

        fps = param[
            "fps"
        ]

        frame = param[
            "frame"
        ]

        display_scale = param[
            "display_scale"
        ]

        if frame is None:
            return

        x_original, y_original = (
            display_to_original_point(
                (x, y),
                display_scale
            )
        )

        time = frame_index / fps

        tracking_data.append({
            "frame": frame_index,
            "time": time,
            "x_pixel": x_original,
            "y_pixel": y_original,
        })

        cv2.circle(
            frame,
            (
                x_original,
                y_original
            ),
            5,
            (0, 0, 255),
            -1
        )

        show_video_frame(
            frame,
            display_scale
        )

        print(
            f"Recorded: "
            f"frame={frame_index}, "
            f"time={time:.3f}, "
            f"x={x_original}, "
            f"y={y_original}"
        )


# ============================================================
# 1. Video loading
# ============================================================

video_path = input(
    "Enter video file path: "
)

video = VideoLoader(
    video_path
)

info = video.get_info()

print(
    "\n=== Video Information ==="
)

print(
    f"FPS: {info['fps']}"
)

print(
    f"Resolution: "
    f"{info['width']} x "
    f"{info['height']}"
)

print(
    f"Total frames: "
    f"{info['frame_count']}"
)

print(
    f"Duration: "
    f"{info['duration']:.3f} s"
)


# ============================================================
# 2. Calibration
# ============================================================

success, calibration_frame = (
    video.read_frame()
)

if not success:
    raise RuntimeError(
        "Could not read calibration frame."
    )


print(
    "\n=== Spatial Calibration ==="
)

print(
    "Select two points with "
    "a known real distance."
)


point1, point2 = (
    select_calibration_points(
        calibration_frame
    )
)


real_distance = float(
    input(
        "Enter real distance "
        "between points (m): "
    )
)


scale = calculate_scale(
    point1,
    point2,
    real_distance
)


print(
    "\nSelect physical "
    "coordinate origin."
)


origin = select_origin(
    calibration_frame
)


print(
    "\nCalibration complete"
)

print(
    "Point 1:",
    point1
)

print(
    "Point 2:",
    point2
)

print(
    f"Scale: {scale} m/pixel"
)

print(
    "Origin:",
    origin
)


# Calibration을 위해 첫 frame을
# 읽었으므로 다시 frame 0으로 이동
video.seek_frame(0)


# ============================================================
# 3. Display / Tracking setup
# ============================================================

display_scale = (
    calculate_display_scale(
        calibration_frame
    )
)


print(
    f"Display scale: "
    f"{display_scale:.3f}"
)


print(
    "\nControls:"
)

print(
    "SPACE : Pause / Resume"
)

print(
    "D     : Next frame"
)

print(
    "A     : Previous frame"
)

print(
    "Q     : Quit"
)


frame_index = 0
displayed_frame_index = 0

paused = False
tracker_initialized = False


mouse_data = {
    "frame_index": 0,
    "fps": video.fps,
    "frame": None,
    "display_scale": display_scale,
}


cv2.namedWindow(
    "Video"
)

cv2.setMouseCallback(
    "Video",
    mouse_callback,
    mouse_data
)


# ============================================================
# 4. Main loop
# ============================================================

while True:

    if not paused:

        success, frame = (
            video.read_frame()
        )

        if not success:
            break

        displayed_frame_index = (
            frame_index
        )


        # ----------------------------------------------------
        # Tracker initialization
        # ----------------------------------------------------

        if not tracker_initialized:

            tracker, bbox = (
                select_and_initialize_tracker(
                    frame
                )
            )

            print(
                "\nTracker initialized."
            )

            print(
                "Initial bounding box:",
                bbox
            )

            tracker_initialized = True


        # ----------------------------------------------------
        # Automatic tracking
        # ----------------------------------------------------

        tracking_success, bbox = (
            tracker.update(frame)
        )


        if tracking_success:

            x, y, w, h = map(
                int,
                bbox
            )

            center_x = (
                x + w // 2
            )

            center_y = (
                y + h // 2
            )


            time = (
                video.frame_to_time(
                    displayed_frame_index
                )
            )


            physical_x, physical_y = (
                pixel_to_physical(
                    (
                        center_x,
                        center_y
                    ),
                    origin,
                    scale
                )
            )


            automatic_tracking_data.append({
                "frame":
                    displayed_frame_index,

                "time":
                    time,

                "x_pixel":
                    center_x,

                "y_pixel":
                    center_y,

                "x":
                    physical_x,

                "y":
                    physical_y,
            })


            cv2.rectangle(
                frame,
                (x, y),
                (
                    x + w,
                    y + h
                ),
                (255, 0, 0),
                2
            )


            cv2.circle(
                frame,
                (
                    center_x,
                    center_y
                ),
                5,
                (0, 255, 255),
                -1
            )


            cv2.putText(
                frame,
                (
                    f"x={physical_x:.3f} m  "
                    f"y={physical_y:.3f} m"
                ),
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2,
            )


        else:

            cv2.putText(
                frame,
                "Tracking lost - reselect ROI",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )

            show_video_frame(
                frame,
                display_scale
            )

            print(
                "\nTracking lost."
            )

            print(
                "Please select a new ROI"
            )

            tracker, bbox = (
                select_and_initialize_tracker(
                    frame
                )
            )

            print(
                "Tracker reinitialized."
            )

            print(
                "New bounding box:",
                bbox
            )

        # ----------------------------------------------------
        # Frame / time display
        # ----------------------------------------------------

        time = (
            video.frame_to_time(
                displayed_frame_index
            )
        )


        cv2.putText(
            frame,
            (
                f"Frame: "
                f"{displayed_frame_index}  "
                f"Time: {time:.3f} s"
            ),
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )


        show_video_frame(
            frame,
            display_scale
        )


        mouse_data[
            "frame_index"
        ] = displayed_frame_index

        mouse_data[
            "frame"
        ] = frame


        frame_index += 1


    # ========================================================
    # Keyboard control
    # ========================================================

    delay = (
        0
        if paused
        else int(
            1000 / video.fps
        )
    )


    key = (
        cv2.waitKey(delay)
        & 0xFF
    )


    if key == ord("q"):
        break


    elif key == ord(" "):

        paused = not paused


    # --------------------------------------------------------
    # Next frame while paused
    # --------------------------------------------------------

    elif (
        paused
        and key == ord("d")
    ):

        displayed_frame_index = min(
            displayed_frame_index + 1,
            video.frame_count - 1
        )


        video.seek_frame(
            displayed_frame_index
        )


        success, frame = (
            video.read_frame()
        )


        if success:

            time = (
                video.frame_to_time(
                    displayed_frame_index
                )
            )


            cv2.putText(
                frame,
                (
                    f"Frame: "
                    f"{displayed_frame_index}  "
                    f"Time: {time:.3f} s"
                ),
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )


            show_video_frame(
                frame,
                display_scale
            )


            mouse_data[
                "frame_index"
            ] = displayed_frame_index

            mouse_data[
                "frame"
            ] = frame


            frame_index = (
                displayed_frame_index
                + 1
            )


    # --------------------------------------------------------
    # Previous frame while paused
    # --------------------------------------------------------

    elif (
        paused
        and key == ord("a")
    ):

        displayed_frame_index = max(
            displayed_frame_index - 1,
            0
        )


        video.seek_frame(
            displayed_frame_index
        )


        success, frame = (
            video.read_frame()
        )


        if success:

            time = (
                video.frame_to_time(
                    displayed_frame_index
                )
            )


            cv2.putText(
                frame,
                (
                    f"Frame: "
                    f"{displayed_frame_index}  "
                    f"Time: {time:.3f} s"
                ),
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )


            show_video_frame(
                frame,
                display_scale
            )


            mouse_data[
                "frame_index"
            ] = displayed_frame_index

            mouse_data[
                "frame"
            ] = frame


            frame_index = (
                displayed_frame_index
                + 1
            )


# ============================================================
# 5. Save results
# ============================================================

save_tracking_data(
    "results/manual_tracking.csv",
    tracking_data
)


save_tracking_data(
    "results/automatic_tracking.csv",
    automatic_tracking_data
)


video.release()

cv2.destroyAllWindows()


print(
    "\nTracking finished."
)

print(
    f"Manual tracking points: "
    f"{len(tracking_data)}"
)

print(
    f"Automatic tracking points: "
    f"{len(automatic_tracking_data)}"
)

if automatic_tracking_data:
    plot_motion(
        automatic_tracking_data
    )