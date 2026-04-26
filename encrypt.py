import os
import cv2
from multiprocessing import Pool, cpu_count

from config import INPUT_VIDEO, FRAMES_DIR
from ffmpeg_utils import extract_frames
from frame_ops import process_frame
from key_utils import generate_key


# Worker function (must be top-level for multiprocessing)
def process_file(args):
    file, key = args
    path = os.path.join(FRAMES_DIR, file)

    frame = cv2.imread(path)
    processed = process_frame(frame, key)

    cv2.imwrite(path, processed)


def encrypt_video():
    password = "ayubmalik"
    key = generate_key(password)

    print("Extracting frames...")
    extract_frames(INPUT_VIDEO)

    print("Processing frames in parallel...")

    files = [f for f in os.listdir(FRAMES_DIR) if f.endswith(".png")]

    # Prepare arguments
    args = [(file, key) for file in files]

    # Use all CPU cores
    with Pool(cpu_count()) as p:
        p.map(process_file, args)

    print("Frame processing complete.")