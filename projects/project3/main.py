import cv2

from src.video_loader import VideoLoader
from src.tracking_data import save_tracking_data

tracking_data = []


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        frame_index = param["frame_index"]
        fps = param["fps"]
        frame = param["frame"]

        time = frame_index / fps

        tracking_data.append({
            "frame": frame_index,
            "time": time,
            "x_pixel": x,
            "y_pixel": y,
        })

        cv2.circle(
            frame,
            (x, y),
            5,
            (0, 0, 255),
            -1
        )

        cv2.imshow("Video", frame)

        print(
            f"Recorded: frame={frame_index}, "
            f"time={time:.3f}, "
            f"x={x}, y={y}"
        )


video_path = input("Enter video file path: ")

video = VideoLoader(video_path)

info = video.get_info()

print("\n=== Video Information ===")
print(f"FPS: {info['fps']}")
print(f"Resolution: {info['width']} x {info['height']}")
print(f"Total frames: {info['frame_count']}")
print(f"Duration: {info['duration']:.3f} s")

print("\nControls:")
print("SPACE : Pause / Resume")
print("D     : Next frame")
print("A     : Previous frame")
print("Q     : Quit")


frame_index = 0
displayed_frame_index = 0
paused = False


mouse_data = {
    "frame_index": 0,
    "fps": video.fps,
    "frame": None,
}


cv2.namedWindow("Video")

cv2.setMouseCallback(
    "Video",
    mouse_callback,
    mouse_data
)


while True:

    if not paused:

        success, frame = video.read_frame()

        if not success:
            break

        displayed_frame_index = frame_index

        time = video.frame_to_time(displayed_frame_index)

        cv2.putText(
            frame,
            f"Frame: {displayed_frame_index}  Time: {time:.3f} s",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.imshow("Video", frame)

        mouse_data["frame_index"] = displayed_frame_index
        mouse_data["frame"] = frame

        frame_index += 1


    delay = 0 if paused else int(1000 / video.fps)

    key = cv2.waitKey(delay) & 0xFF


    if key == ord("q"):
        break


    elif key == ord(" "):
        paused = not paused


    elif paused and key == ord("d"):

        displayed_frame_index = min(
            displayed_frame_index + 1,
            video.frame_count - 1
        )

        video.seek_frame(displayed_frame_index)

        success, frame = video.read_frame()

        if success:

            time = video.frame_to_time(displayed_frame_index)

            cv2.putText(
                frame,
                f"Frame: {displayed_frame_index}  Time: {time:.3f} s",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )

            cv2.imshow("Video", frame)

            mouse_data["frame_index"] = displayed_frame_index
            mouse_data["frame"] = frame

            frame_index = displayed_frame_index + 1


    elif paused and key == ord("a"):

        displayed_frame_index = max(
            displayed_frame_index - 1,
            0
        )

        video.seek_frame(displayed_frame_index)

        success, frame = video.read_frame()

        if success:

            time = video.frame_to_time(displayed_frame_index)

            cv2.putText(
                frame,
                f"Frame: {displayed_frame_index}  Time: {time:.3f} s",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )

            cv2.imshow("Video", frame)

            mouse_data["frame_index"] = displayed_frame_index
            mouse_data["frame"] = frame

            frame_index = displayed_frame_index + 1


save_tracking_data(
    "results/manual_tracking.csv",
    tracking_data
)

video.release()
cv2.destroyAllWindows()