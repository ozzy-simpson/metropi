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
        
        self.show = show

        self.display = display
        
        self._line = []
        self._dest = []
        self._min = []
        for i in range(show):
            self._line.append(None)
            self._dest.append(None)
            self._min.append(None)

    def display_metro(self, metro_status):
        
        # Shorten show if there are fewer trains right now!
        if len(metro_status['Trains']) < self.show:
            self.show = len(metro_status['Trains'])
            
        for i in range(self.show):
            self._line[i] = metro_status['Trains'][i]['Line']
            self._dest[i] = metro_status['Trains'][i]['Destination']   
            self._min[i] = metro_status['Trains'][i]['Min']
    
        self.update_display()

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
        
        
        for i in range(self.show):
            # Move to new line
            yVal += font_height + 5 
            
            # Line
            draw.text(
                (0, yVal),
                self._line[i],
                font=self.medium_font,
                fill=BLACK,
            )
        
            # Destination
            draw.text(
                (destX, yVal),
                self._dest[i],
                font=self.medium_font,
                fill=BLACK,
            )
            
            # Minutes
            (font_width, font_height) = medium_font.getsize(self._min[i])
            draw.text(
                (self.display.height - font_width - 5, yVal),
                self._min[i],
                font=self.medium_font,
                fill=BLACK,
            )

       
        self.display.displayPartBaseImage(self.display.getbuffer(image))
        self.display.init(self.display.FULL_UPDATE)
