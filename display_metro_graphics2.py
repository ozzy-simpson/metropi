from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import json

small_font = ImageFont.truetype("fonts/DejaVuSans-Bold.ttf", 16)
medium_font = ImageFont.truetype("fonts/DejaVuSans.ttf", 20)
large_font = ImageFont.truetype("fonts/DejaVuSans-Bold.ttf", 24)

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

show = 4


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
        self._line1 = None
        self._progress = None
        self._has_arrived = None

    def display_metro(self, metro_status):
    
        self._line1 = metro_status['Trains'][0]['Line']
        self._line2 = metro_status['Trains'][1]['Line']
        self._line3 = metro_status['Trains'][2]['Line']
    
        self._dest1 = metro_status['Trains'][0]['Destination']
        self._dest2 = metro_status['Trains'][1]['Destination']
        self._dest3 = metro_status['Trains'][2]['Destination']   
        
        self._min1 = metro_status['Trains'][0]['Min']
    
        self.update_time()
        self.update_display()

    def update_time(self):
        now = datetime.now()
        self._time_text = now.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")

    def update_display(self):
        image = Image.new("RGB", (self.display.width, self.display.height), color=WHITE)
        image = image.transpose(Image.ROTATE_270) 
        draw = ImageDraw.Draw(image)
        
        xVal = 0
        yVal = 0

        # Draw the headers
        ## Line
        (font_width, font_height) = large_font.getsize("LN")
        draw.text(
            (xVal, yVal),
            "LN",
            font=self.large_font,
            fill=BLACK,
        )
        xVal += font_width + 10
        destX = xVal
        ## Destination
        draw.text(
            (xVal, yVal),
            "DEST",
            font=self.large_font,
            fill=BLACK,
        )
        ## Minutes
        (font_width, font_height) = large_font.getsize("MIN")
        draw.text(
            (self.display.height - font_width - 5, yVal),
            "MIN",
            font=self.large_font,
            fill=BLACK,
        )
        
        
        for i in range(show):
            yVal += font_height + 5 #move to new line
            
            # Line
            draw.text(
                (0, yVal),
                self._line1,
                font=self.medium_font,
                fill=BLACK,
            )
            (font_width, font_height) = medium_font.getsize(self._line1)
        
            # Destination
            draw.text(
                (destX, yVal),
                self._dest1,
                font=self.medium_font,
                fill=BLACK,
            )
            (font_width, font_height) = medium_font.getsize(self._dest1)
        
            # Minutes
            (font_width, font_height) = medium_font.getsize(self._min1)
            draw.text(
                (self.display.height - font_width - 5, yVal),
                self._min1,
                font=self.medium_font,
                fill=BLACK,
            )

       
        self.display.displayPartBaseImage(self.display.getbuffer(image))
        self.display.init(self.display.FULL_UPDATE)
