# Remote Access to Raspberry Pi 4
To remotely access your Raspberry Pi 4, you can use Secure Shell (SSH), which allows you to connect to the Pi over a network. Follow these steps to set up remote access:

## Enable SSH on Raspberry Pi:

Ensure that SSH is enabled on your Raspberry Pi by following these steps:
- Boot up your Raspberry Pi and log in.
- Run `sudo raspi-config` in the terminal.
- Navigate to `Interfacing Options` > `SSH`.
- Select `Ye`s to `enable SSH`.
- Reboot your Raspberry Pi if prompted.

## Find the IP Address of Raspberry Pi:

Determine the IP address of your Raspberry Pi on the network. You can use various methods like checking your router's connected devices list or running `hostname -I` on the Raspberry Pi.

Connect to Raspberry Pi via `SSH`:

Once you have the IP address, you can connect to your Raspberry Pi using SSH. Use the following command in the terminal:

```
ssh <username>@raspberrypi.local
```
