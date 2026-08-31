import cv2

from src.video_loader import VideoLoader

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
paused = False

while True:
    if not paused:
        success, frame = video.read_frame()

        if not success:
            break

        time = video.frame_to_time(frame_index)

        cv2.putText(
            frame,
            f"Frame: {frame_index}  Time: {time:.3f} s",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.imshow("Video", frame)

        frame_index += 1

    delay = 0 if paused else int(1000 / video.fps)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord("q"):
        break

    elif key == ord(" "):
        paused = not paused

    elif paused and key == ord("d"):
        frame_index = min(
            frame_index + 1,
            video.frame_count - 1
        )

        video.seek_frame(frame_index)

        success, frame = video.read_frame()

        if success:
            time = video.frame_to_time(frame_index)

            cv2.putText(
                frame,
                f"Frame: {frame_index}  Time: {time:.3f} s",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )

            cv2.imshow("Video", frame)

    elif paused and key == ord("a"):
        frame_index = max(
            frame_index - 1,
            0
        )

        video.seek_frame(frame_index)

        success, frame = video.read_frame()

        if success:
            time = video.frame_to_time(frame_index)

            cv2.putText(
                frame,
                f"Frame: {frame_index}  Time: {time:.3f} s",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )

            cv2.imshow("Video", frame)

video.release()
cv2.destroyAllWindows()