## Run a Program On Your Raspberry Pi At Startup
### Editing rc.local
To configure your Raspberry Pi to execute specific commands upon startup, follow these steps:

Open the file /etc/rc.local with root permissions using the following command:

```shell
sudo nano /etc/rc.local
```
Insert the desired commands into the file. For example, to play a song upon Pi startup, you can use the aplay command followed by the absolute file path of the song:
```bash
sudo aplay /path/to/songfile.mp3
```
After inserting your commands, save the file and exit the text editor.

**Note:** 
- It's important to use **absolute file paths** (`/path/to/songfile.mp3`) rather than **relative paths** to ensure proper execution.
- Ensure that any scripts or commands added to `/etc/rc.local` **do not cause the boot sequence to hang**. Testing the commands thoroughly before adding them to the startup sequence is recommended.
- You can redirect the output and errors of your script to a text file for debugging purposes. For example:
  ```bash
  sudo python /home/pi/sample.py & > /home/pi/Desktop/log.txt 2>&1
  ```
- Remember to leave the line exit 0 intact at the end of the /etc/rc.local file.

By following these steps, your Raspberry Pi will execute the specified commands upon startup as part of its boot sequence.
