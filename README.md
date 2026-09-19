# pi-configs
Configuration cheat sheet for my Raspberry Pi (current version 4).

# Table of Contents
- [Remote access via SSH](#remote-access-via-ssh)
- [Command Line Audio](#command-line-audio)
- [Download Youtube Video & mp3 Extraction](#download-youtube-video-and-mp3-extraction)
- [Run a Program On Your Raspberry Pi At Startup](#run-a-program-on-your-raspberry-pi-at-startup)

## Remote Access via SSH
This section outlines the configuration steps for enabling remote access to your Raspberry Pi via SSH.

*See [here.](./remote_access.md)*

## Command Line Audio
This section explores **aplay** and **mpg321**, two command line tools for managing audio on your Raspberry Pi.

*See [here.](./command_line_audio.md)*

## Download Youtube Video and mp3 Extraction
This section covers methods for downloading YouTube videos and extracting MP3 audio files for use on your Raspberry Pi.

*See [here.](./youtube_downloader.md)* 

## Run a Program On Your Raspberry Pi At Startup
This section outlines how to configure your Raspberry Pi to automatically run a program upon startup using the rc.local file. Automating program execution on boot can be particularly useful for headless setups, enabling seamless operation without manual intervention or configuration.

*See [here.](./startup_command.md)*

## Oled screen configuration
Waveshare Oled screen. Used this command `sudo systemctl restart info_oled` to restart it. Everything is in ./oled folder. OLED screen: a Python script (`startUp.py` in the Waveshare `RaspberryPi/python/example/` folder) shows system info on the screen. It runs as a `systemd` service that starts at boot. Requires SPI and I2C enabled. Search: "run python script at boot with systemd raspberry pi".
