# RELEASES
V1: MP3 & MP4 Support

V2: (next) customization...
# COMPILE
You need ffmpeg and ffprobe binary in a folder named ffmpeg_bin (https://www.ffmpeg.org/download.html) and PyInstaller.

```
pyinstaller --onefile --noconsole --add-data "ffmpeg_bin;ffmpeg_bin" main.py
```

