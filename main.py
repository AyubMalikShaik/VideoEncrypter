from encrypt import encrypt_video
from ffmpeg_utils import rebuild_video
from config import OUTPUT_VIDEO


def main():
    encrypt_video()

    print("Rebuilding video...")
    rebuild_video(OUTPUT_VIDEO)

    print("Done!")


if __name__ == "__main__":
    main()