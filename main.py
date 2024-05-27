import yt_dlp
import time
import os
import sys

channelurl = "https://www.youtube.com/channel/CHANNEL_ID"  # use channel id or use youtube.com/@<channel_name>
outputdir = "downloads"
if not os.path.exists(outputdir):
    os.makedirs(outputdir)
options = {
    "outtmpl": os.path.join(outputdir, "%(title)s.%(ext)s"),
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "ignoreerrors": True,
    "quiet": True,
    "no_warnings": True,
}
ydl = yt_dlp.YoutubeDL(options)
with open(os.devnull, "w") as devnull:
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = devnull
    sys.stderr = devnull
    try:
        with ydl:
            ydl.download([channelurl])
    except Exception as e:
        print(f"error; {e}")

    sys.stdout = old_stdout
    sys.stderr = old_stderr

    while True:
        try:
            with ydl:
                ydl.download([channelurl])
        except Exception as e:
            print(f"error; {e}")

        time.sleep(60)
