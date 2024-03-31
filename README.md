# pi-configs
Configuration cheat sheet for my Raspberry Pi (current version 4).

# Table of Contents


## Remote access via SSH

## Run a Program On Your Raspberry Pi At Startup
### Editing rc.local
On your Pi, edit the file `/etc/rc.local` with root permissions:
```shell
sudo nano /etc/rc.local
```
For example, play a song when Pi wake up
```bash
sudo aplay <songfile>.mp3
```
sudo reboot

Note:
- Use absolute file names (`/home/pi/myscript.py`) rather than relative (`myscript.py`).

- Scripts in `/etc/rc.local` are added to the boot sequence. If your code gets stuck then the boot sequence cannot proceed. So be careful as to which code you are trying to run at boot and test the code a couple of times. You can also get the script’s output and error written to a text file (ex: `log.txt`) and use it to debug.
```bash
sudo python /home/pi/sample.py & > /home/pi/Desktop/log.txt 2>&1
```
- Be sure to leave the line exit 0 at the end.

