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
    
          self.update_time()
          self.update_display()

    def update_time(self):
        now = datetime.now()
        self._time_text = now.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")

    def update_display(self):
        image = Image.new("RGB", (self.display.width, self.display.height), color=WHITE)
        image = image.transpose(Image.ROTATE_270) 
        draw = ImageDraw.Draw(image)

        # Draw the headers
        ## Line
        (font_width, font_height) = large_font.getsize("LN")
        draw.text(
            (0, 0),
            "LN",
            font=self.large_font,
            fill=BLACK,
        )
        ## Cars
        draw.text(
            (font_width+5, 0),
            "CAR",
            font=self.large_font,
            fill=BLACK,
        )
        (font_width, font_height) = large_font.getsize("CAR")
        ## Destination
        draw.text(
            (font_width+5, 0),
            "DEST",
            font=self.large_font,
            fill=BLACK,
        )
        (font_width, font_height) = large_font.getsize("DEST")
        ## Minutes
        draw.text(
            (font_width+5, 0),
            "MIN",
            font=self.large_font,
            fill=BLACK,
        )

       
        self.display.displayPartBaseImage(self.display.getbuffer(image))
        self.display.init(self.display.FULL_UPDATE)
