# [DEPRECATED]
Future idea: change to rust

# yt-dlp-basic-gui
yt-dlp-basic-gui is a minimalistic graphical user interface (GUI) for [yt-dlp](https://github.com/yt-dlp/yt-dlp), an open-source command-line tool designed to effortlessly download video and audio content from a wide range of websites.

## RELEASES
V1: MP3 & MP4 Support

## INSTALLATION
1. Download the latest release.
2. Create a Direct Access to the yt-dlp-basic-gui.exe
3. Ready to go.

## COMPILE
```
pyinstaller --noconsole --add-data "ffmpeg_bin/*.exe;ffmpeg_bin/" src/yt-dlp-basic-gui.py
```
### DEPENDENCIES
You need ffmpeg and ffprobe binary in the ffmpeg_bin folder. (https://www.ffmpeg.org/download.html).

## TODO
- Formats customization
- Postprocessing options

