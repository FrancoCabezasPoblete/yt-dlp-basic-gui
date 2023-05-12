# RELEASES
V1: MP3 & MP4 support

V2: (next) customization...
# COMPILE
You need ffmpeg and ffprobe binary in a folder named ffmpeg_bin (https://www.ffmpeg.org/download.html) and PyInstaller.

```
python3 pyinstaller --onefile --noconsole --add-data "ffmpeg_bin;ffmpeg_bin" main.py
```

