# Cooper Richman
# 19 February 2026
#
# The goal of this script is to record the show dubbed "Take It or Leave It" hosted on WMUA at 9-10AM every Thursday.
# This show is hosted by my good friends Hanna Weldai (DJ Han) and Sri Paladugu (DJ Joe).
# This link is to see what they have played in the past: https://widgets.spinitron.com/WMUA/show/302592/Take-It-or-Leave-It
# This link is where to listen: https://fastcast4u.com/player/qernhlca/, or alternatively 91.1FM


# Imports and whatnot
import os
import re
import subprocess
import requests
from datetime import datetime

# Set the link, the output directory, and also the duration
PLAYER_URL = "https://fastcast4u.com/player/qernhlca/"
OUTPUT_DIR = "TIOLI recordings"
DURATION_SECONDS = 5400  # 90 minutes

# A function to find the stream
def find_stream():
    print("Fetching player page...")
    html = requests.get(PLAYER_URL, timeout=30).text

    match = re.search(r'https://[^"]+\.m3u8', html)
    if not match:
        raise Exception("Could not locate stream URL")

    return match.group(0)

# A function to record the actual podcast
def record(stream_url):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M")
    output_file = f"{OUTPUT_DIR}/radio_{timestamp}.mp3"

    print("Recording stream:", stream_url)

    cmd = [
        "ffmpeg",
        "-y",
        "-loglevel", "error",
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
    stream = find_stream()
    record(stream)
