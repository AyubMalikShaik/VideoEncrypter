import os
import cv2
from config import INPUT_VIDEO, FRAMES_DIR
from ffmpeg_utils import extract_frames
from frame_ops import process_frame


def encrypt_video():
    print("Extracting frames...")
    extract_frames(INPUT_VIDEO)

    print("Processing frames...")
    for file in os.listdir(FRAMES_DIR):
        if file.endswith(".png"):
            path = os.path.join(FRAMES_DIR, file)

            frame = cv2.imread(path)
            processed = process_frame(frame)

            cv2.imwrite(path, processed)

    print("Frame processing complete.")