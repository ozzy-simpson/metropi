#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
libdir = 'lib'
if os.path.exists(libdir):
    sys.path.append(libdir)
from TP_lib import gt1151
from TP_lib import epd2in13_V2
from dotenv import load_dotenv
import time
import logging
import requests
from PIL import Image,ImageDraw,ImageFont
import traceback
import threading

small_font = ImageFont.truetype("fonts/DejaVuSans-Bold.ttc", 16)
medium_font = ImageFont.truetype("fonts/DejaVuSans.ttc", 20)
large_font = ImageFont.truetype("fonts/DejaVuSans-Bold.ttc", 24)

logging.basicConfig(level=logging.DEBUG)
flag_t = 1

## Load the env variable 
load_dotenv()

def pthread_irq() :
    print("pthread running")
    while flag_t == 1 :
        if(gt.digital_read(gt.INT) == 0) :
            GT_Dev.Touch = 1
        else :
            GT_Dev.Touch = 0
    print("thread:exit")

try:
    logging.info("MetroPi Demo")
    
    epd = epd2in13_V2.EPD_2IN13_V2()
    gt = gt1151.GT1151()
    GT_Dev = gt1151.GT_Development()
    GT_Old = gt1151.GT_Development()
    
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    gt.GT_Init()
    epd.Clear(0xFF)

    t = threading.Thread(target = pthread_irq)
    t.setDaemon(True)
    t.start()

    epd.init(epd.PART_UPDATE)
    
    ## Station code can be set to 'All' to get all the stations or 
    ## a specific station code such as B03
    station_code = 'C04'

    api_key = os.getenv('METRO_API_KEY')
    api_url = 'https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{}'.format(station_code)

    request_headers = {'api_key': api_key}
    refresh_display = None
    
    while True:
      if (not refresh_display) or (time.monotonic() - refresh_display) > 60:
          request = requests.get(api_url, request_headers).json()
          
          image = Image.new('1', (epd.width, epd.height), 255)   # 255: clear the frame
          draw = ImageDraw.Draw(image)
          draw.text((8, 12), 'hello world', font = medium_font, fill = 255)
          
          refresh_display = time.monotonic()

      time.sleep(60)
                
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    flag_t = 0
    epd.sleep()
    time.sleep(2)
    t.join()
    epd.Dev_exit()
    exit()
