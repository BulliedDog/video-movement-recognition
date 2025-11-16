import cv2, os
import numpy as np

def normalize_frame(img, target_size, mode='letterbox', fill_color=(0,0,0)):
    """
    target_size: (width, height)  
    mode: 'letterbox' (pad), 'crop' (center-crop), 'stretch' (force)
    """
    if target_size is None:
        return img
    tw, th = target_size
    h, w = img.shape[:2]

    if mode == 'stretch':
        return cv2.resize(img, (tw, th), interpolation=cv2.INTER_LINEAR)

    if mode == 'crop':
        scale = max(tw / w, th / h)
        new_w, new_h = int(w * scale), int(h * scale)
        interp = cv2.INTER_AREA if scale < 1 else cv2.INTER_LINEAR
        resized = cv2.resize(img, (new_w, new_h), interpolation=interp)
        x_off = (new_w - tw) // 2
        y_off = (new_h - th) // 2
        return resized[y_off:y_off+th, x_off:x_off+tw]

    # default: letterbox (preserve aspect ratio + pad)
    scale = min(tw / w, th / h)
    new_w, new_h = int(w * scale), int(h * scale)
    interp = cv2.INTER_AREA if scale < 1 else cv2.INTER_LINEAR
    resized = cv2.resize(img, (new_w, new_h), interpolation=interp)
    canvas = np.full((th, tw, 3), fill_color, dtype=resized.dtype)
    x_off = (tw - new_w) // 2
    y_off = (th - new_h) // 2
    canvas[y_off:y_off+new_h, x_off:x_off+new_w] = resized
    return canvas

def extractFrames(output_folder: str, cap, target_size=(1920, 1080), mode='letterbox') -> int:
    """
    Extract frames from VideoCapture into output_folder.
    If target_size is provided (width, height), each saved frame is normalized.
    Backward-compatible: call with (output_folder, cap) to keep current behavior.
    """
    frame_count = 0
    while True:
        ret, frame = cap.read()  # ret is True if frame is read correctly
        if not ret:
            break
        # Normalize frame if requested
        norm_frame = normalize_frame(frame, target_size, mode) if target_size else frame
        # Save frame as image file
        frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, norm_frame)
        frame_count += 1
    return frame_count
