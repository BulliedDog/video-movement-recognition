import cv2,os
from framing import *
video_path = "videos/swarm_of_mosquitos.mp4"
output_folder = "extracted_frames"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

framesNumber = extractFrames(output_folder, cap)

cap.release()
cv2.destroyAllWindows()
print(f"Extracted {frame_count} frames from the video.")