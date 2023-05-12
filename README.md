# yt-dlp-basic-gui
## RELEASES
V1: MP3 & MP4 Support

## INSTALATION
1. Download the latest release.
2. Create a Direct Access to the yt-dlp-basic-gui.exe
3. Ready to go.

## COMPILE
### DEPENDENCIES
You need ffmpeg and ffprobe binary in the ffmpeg_bin folder. (https://www.ffmpeg.org/download.html).
```
pyinstaller --noconsole --add-data "ffmpeg_bin/*.exe;ffmpeg_bin/" src/yt-dlp-basic-gui.py
```

## TODO
- Formats customization
- Postprocessing options
- Bundle ffmpeg & ffprobe executables

