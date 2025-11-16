import cv2,os
from framing import *
video_path = "videos/swarm_of_mosquitos.mp4"
output_folder = "extracted_frames"
target_size = (1920, 1080)
normalize_mode = 'letterbox'
os.makedirs(output_folder, exist_ok=True)
cap = cv2.VideoCapture(video_path)

# FRAME EXTRACTION #
frames_number = extractFrames(output_folder, cap, target_size, normalize_mode)
# Now frames are under "./videos/", numered and normalized

cap.release()
cv2.destroyAllWindows()
print(f"Extracted {frames_number} frames from the video.")