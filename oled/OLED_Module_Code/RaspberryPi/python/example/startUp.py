#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import signal
import os
import socket
import psutil
import logging    
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Paths
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_OLED import OLED_2in42

# Setup logging
logging.basicConfig(level=logging.DEBUG)

def sigterm_handler(sig, frame):
    print('Signal received: ', sig)
    try:
        disp.clear()  # Clear the display or set it to a 'shutdown' message
        disp.module_exit()  # Properly close down the display module if available
        print("Display cleared and module exit cleanly.")
    except Exception as e:
        print("Failed to clean up resources properly:", e)
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
    return float(temp) / 1000

try:
    disp = OLED_2in42.OLED_2in42(spi_freq = 1000000)
    disp.Init()
    disp.clear()

    while True:
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 10)

        # Fetch system information
        ip_address = get_ip_address()
        temperature = get_cpu_temperature()
        cpu_usage = psutil.cpu_percent()
        disk_usage = psutil.disk_usage('/').percent

        # Current date and time
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
        date, time_str = current_time.split()

        # Draw the box
        draw.line([(0,0),(127,0)], fill = 0)
        draw.line([(0,0),(0,63)], fill = 0)
        draw.line([(0,63),(127,63)], fill = 0)
        draw.line([(127,0),(127,63)], fill = 0)

        # Draw the date and time
        draw.text((10, 2), date, font=font1, fill=0)  # Display date
        draw.text((90, 2), time_str, font=font1, fill=0)  # Display time
        draw.line([(7, 15),(120, 15)], fill = 0)

        # Draw the information
        draw.text((10, 16), 'IP: ' + ip_address, font=font1, fill=0)
        draw.text((10, 26), 'Temp: {:.1f} °C'.format(temperature), font=font1, fill=0)
        draw.text((10, 36), 'CPU: {} %'.format(cpu_usage), font=font1, fill=0)
        draw.text((10, 46), 'Disk: {} %'.format(disk_usage), font=font1, fill=0)

        image1 = image1.rotate(180) 
        disp.ShowImage(disp.getbuffer(image1))
        time.sleep(1)

except IOError as e:
    logging.error(e)
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()
