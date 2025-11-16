import cv2, os

def extractFrames(output_folder: str, cap) -> int:
    frame_count = 0
    while True:
        ret, frame = cap.read()  # ret is True if frame is read correctly
        if not ret:
            break
        # Save frame as image file
        frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
