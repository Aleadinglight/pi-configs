# Youtube Downloader

## Overview
Methods for downloading YouTube videos and extracting MP3 audio files for use on your Raspberry Pi. 

- [yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/Installation) is the most popular option.
- [ffmpeg](https://ffmpeg.org/): This is used to convert videos to `.mp3` format alongside with `yt-dlp`.


## Installation
### yt-dlp
Follow the instructions on the installtion page:
```shell
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o ~/.local/bin/yt-dlp
chmod a+rx ~/.local/bin/yt-dlp  # Make executable
```
### ffmpeg
Installation using `apt-get`:
```shell
sudo apt-get install ffmpeg
```

## Usage
```shell
yt-dlp "<youtube_video_link>"
```
**Note:** `yt-dlp` downloads the highest available quality by default. However, it requires `ffmpeg` to combine separate video and audio streams. Without `ffmpeg`, it downloads lower quality media that doesn't require merging, typically up to 720p.

```shell
yt-dlp -x --audio-format mp3 "<youtube_video_link>"
```
The `.mp3` file will be saved in the local folder where the code is executed.
