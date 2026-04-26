import subprocess
import os
from config import FFMPEG_PATH, FRAMES_DIR, FPS


def extract_frames(input_video):
    if not os.path.exists(FRAMES_DIR):
        os.makedirs(FRAMES_DIR)

    subprocess.run([
        FFMPEG_PATH,
        "-i", input_video,
        f"{FRAMES_DIR}/frame_%04d.png"
    ])


def rebuild_video(output_video):
    subprocess.run([
        FFMPEG_PATH,
        "-framerate", str(FPS),
        "-i", f"{FRAMES_DIR}/frame_%04d.png",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_video
    ])