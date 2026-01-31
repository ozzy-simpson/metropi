#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
libdir = '/home/pi/metropi/lib'
if os.path.exists(libdir):
    sys.path.append(libdir)
from TP_lib import gt1151
from TP_lib import epd2in13_V2
from dotenv import load_dotenv
import logging
import requests
from PIL import Image,ImageDraw,ImageFont
from display_metro_graphics import Metro_Graphics

logging.basicConfig(level=logging.INFO)

## Load the env variable 
load_dotenv()

try:
    # API configuration
    station_code = 'C04'
    api_key = os.getenv('METRO_API_KEY')
    api_url = f"https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{station_code}"
    request_headers = {'api_key': api_key}

    # Fetch Metro data and display it once
    request = requests.get(api_url, request_headers).json()
    
    # Initialize the display and touch panel
    epd = epd2in13_V2.EPD_2IN13_V2()
    gt = gt1151.GT1151()
    GT_Dev = gt1151.GT_Development()
    GT_Old = gt1151.GT_Development()
    
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    gt.GT_Init()
    # epd.Clear(0xFF)
    gfx = Metro_Graphics(epd)
    gfx.display_metro(request)

    # Put the display to sleep after updating once
    epd.sleep()
    epd.Dev_exit()

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd.sleep()
    epd.Dev_exit()
    exit()
