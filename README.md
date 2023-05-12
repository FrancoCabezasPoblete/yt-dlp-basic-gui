# yt-dlp-basic-gui
## RELEASES
V1: MP3 & MP4 Support

## DEPENDENCIES
You need ffmpeg and ffprobe binary in a ffmpeg_bin folder next to the executable. (https://www.ffmpeg.org/download.html).

## INSTALATION
1. Download the latest release.
2. In the ffmpeg_bin directory put ffmpeg.exe & ffprobe.exe .
3. Ready to go.

## COMPILE

```
pyinstaller --onefile --noconsole --add-data "ffmpeg_bin;ffmpeg_bin" main.py
```

## TODO
- Compress executable size
- Formats customization
- Postprocessing options
- Bundle ffmpeg & ffprobe executables

