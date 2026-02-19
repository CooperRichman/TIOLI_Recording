# Cooper Richman
# 19 February 2026
#
# The goal of this script is to record the show dubbed "Take It or Leave It" hosted on WMUA at 9-10AM every Thursday.
# This show is hosted by my good friends Hanna Weldai (DJ Han) and Sri Paladugu (DJ Joe).
# This link is to see what they have played in the past: https://widgets.spinitron.com/WMUA/show/302592/Take-It-or-Leave-It
# This link is where to listen: https://fastcast4u.com/player/qernhlca/, or alternatively 91.1FM

# Imports and whatnot
import os
import subprocess
from datetime import datetime

# Direct audio stream URL
# Note this was found by inspecting the page anf finding the actual audio stream from https://fastcast4u.com/player/qernhlca/
STREAM_URL = "https://usa5.fastcast4u.com/proxy/qernhlca?mp=/1"
OUTPUT_DIR = "TIOLI recordings"
#DURATION_SECONDS = 5400  # 90 minutes
DURATION_SECONDS = 60 # 1 minute for testing


# A function to record the actual podcast
def record(stream_url):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M")
    output_file = f"{OUTPUT_DIR}/radio_{timestamp}.mp3"

    print("Recording stream:", stream_url)

    cmd = [
        "ffmpeg",
        "-y",
        "-loglevel", "info",      # Optional: shows progress in logs
        "-i", stream_url,
        "-t", str(DURATION_SECONDS),
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "128k",
        output_file
    ]

    subprocess.run(cmd, check=True)
    print("Saved:", output_file)

# Execute
if __name__ == "__main__":
    record(STREAM_URL)
