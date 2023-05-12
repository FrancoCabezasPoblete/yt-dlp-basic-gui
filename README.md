# COMPILE
You need ffmpeg binary in a folder named ffmpeg_bin (https://www.ffmpeg.org/download.html) and PyInstaller.

```
python3 pyinstaller --onefile --noconsole --add-data "ffmpeg_bin;ffmpeg_bin" main.py
```

