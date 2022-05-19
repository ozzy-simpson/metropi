from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import json

small_font = ImageFont.truetype("fonts/DejaVuSans-Bold.ttf", 16)
medium_font = ImageFont.truetype("fonts/DejaVuSans.ttf", 20)
large_font = ImageFont.truetype("fonts/DejaVuSans-Bold.ttf", 24)

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Metro_Graphics:
    def __init__(self, display):

        self.small_font = small_font
        self.medium_font = medium_font
        self.large_font = large_font

        self.display = display

        self._metro_icon = None
        self._destination_name = None
        self._location_name = None
        self._arrival_minutes = None
        self._line = None
        self._progress = None
        self._has_arrived = None

    def display_metro(self, metro_status):
     
          destination1_name = metro_status[0]['DestinationName']
          if destination1_name == "Franconia-Springfield":
            destination1_name = "Franc-Sprngfld"
          elif destination1_name == "Largo Town Center":
            destination1_name = "Largo Town Ctr"
          elif destination1_name == "Vienna/Fairfax-GMU":
            destination1_name = "Vienna/Frfx"
          elif destination1_name == "Wiehle-Reston East":
            destination1_name = "Wiehle-Rstn E"
          self._destination1_name = destination1_name
          print('Destination: ' + destination1_name)

          location1_name = metro_status[0]['LocationName']
          self.location1_name = location1_name
          print('Current Location: ' + location1_name)

          line = metro_status[0]['Line']
          self._line = line
          print('Line: ' + line)

          arrival1_minutes = metro_status[0]['Min']
          if arrival1_minutes.isdigit():
              has1_arrived = False
              arrival1_minutes = arrival1_minutes + 'min'
          else:
              has1_arrived = True

          self._has1_arrived = has1_arrived
          self._arrival1_minutes = arrival1_minutes
          print('Arrival Status: ' + arrival1_minutes)
        
        
     
          destination2_name = metro_status[1]['DestinationName']
          if destination2_name == "Franconia-Springfield":
            destination2_name = "Franc-Sprngfld"
          elif destination2_name == "Largo Town Center":
            destination2_name = "Largo Town Ctr"
          elif destination2_name == "Vienna/Fairfax-GMU":
            destination2_name = "Vienna/Frfx"
          elif destination2_name == "Wiehle-Reston East":
            destination2_name = "Wiehle-Rstn E"
          self._destination2_name = destination2_name
          print('Destination: ' + destination2_name)

          location2_name = metro_status[1]['LocationName']
          self.location2_name = location2_name
          print('Current Location: ' + location2_name)

          arrival2_minutes = metro_status[1]['Min']
          if arrival2_minutes.isdigit():
              has2_arrived = False
              arrival2_minutes = arrival2_minutes + 'min'
          else:
              has2_arrived = True

          self._has2_arrived = has2_arrived
          self._arrival2_minutes = arrival2_minutes
          print('Arrival Status: ' + arrival2_minutes)

          self.update_time()
          self.update_display()

    def update_time(self):
        now = datetime.now()
        self._time_text = now.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")

    def update_display(self):
        image = Image.new("RGB", (self.display.width, self.display.height), color=WHITE)
        image = image.transpose(Image.ROTATE_270) 
        draw = ImageDraw.Draw(image)

        # Draw the time
        (font_width, font_height) = medium_font.getsize(self._time_text)
        draw.text(
            (self.display.height - font_width - 5, 7),
            self._time_text,
            font=self.medium_font,
            fill=BLACK,
        )

        # Draw the line
        (font_width, font_height) = large_font.getsize(self._line)
        draw.text(
            (5, 5),
            self._line,
            font=self.large_font,
            fill=BLACK,
        )

        # Draw the destination
        (font_width, font_height) = medium_font.getsize(self._destination1_name)
        draw.text(
            (5, self.display.width - font_height * 4 + 2),
            self._destination1_name,
            font=self.medium_font,
            fill=BLACK,
        )
        
        # Draw line break
        # draw.line([(0, self.display.height / 2), (self.display.width, self.display.height / 2)], BLACK, 1) 
         
        # Draw the arrival time
        (font_width, font_height) = large_font.getsize(self._arrival1_minutes)
        draw.text(
            (
                self.display.height - font_width - 5,
                self.display.width - font_height * 4,
            ),
            self._arrival1_minutes,
            font=self.large_font,
            fill=BLACK,
        )

        # Draw the destination
        (font_width, font_height) = medium_font.getsize(self._destination2_name)
        draw.text(
            (5, self.display.width - font_height * 2 + 2),
            self._destination2_name,
            font=self.medium_font,
            fill=BLACK,
        )
        
        # Draw line break
        # draw.line([(0, self.display.height / 2), (self.display.width, self.display.height / 2)], BLACK, 1) 
         
        # Draw the arrival time
        (font_width, font_height) = large_font.getsize(self._arrival2_minutes)
        draw.text(
            (
                self.display.height - font_width - 5,
                self.display.width - font_height * 2,
            ),
            self._arrival2_minutes,
            font=self.large_font,
            fill=BLACK,
        )

       
        self.display.displayPartBaseImage(self.display.getbuffer(image))
        self.display.init(self.display.FULL_UPDATE)
