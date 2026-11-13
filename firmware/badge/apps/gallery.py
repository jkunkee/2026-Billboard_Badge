"""Load random artwork at timed interval- Broken by Tom Nardi"""

from apps.base_app import BaseApp
from lib.button import MenuMinus, MenuPlus, UserA, UserB, Boot
from lib.epd import display
from lib.led_bar import NUM_LEDS, leds

import time
import random

class GalleryApp(BaseApp):
    def __init__(self, name: str | None = None) -> None:
        self.name = "Gallery"
        self.sleep_ms = 100
        self.launched = False
        
        # Number of images
        self.maximage = 46

        # Which images have been shown so far
        self.shown_images = [False] * self.maximage
        
        # Time between image updates
        self.updatetime = 300
   
        # Variable to hold time since last change
        self.lastupdate = 0
    
    def random_art(self):
        if all(self.shown_images):
            self.shown_images = [False] * self.maximage

        remaining = [
            image_number
            for image_number in range(1, self.maximage + 1)
            if not self.shown_images[image_number - 1]
        ]
        image_number = random.choice(remaining)
        self.shown_images[image_number - 1] = True

        display.clear()
        display.draw_png(f'/data/gallery/{image_number:03d}.png')
        display.update()
    
    def run(self):
        if self.launched:
            self.random_art()
            self.lastupdate = time.time()
        else:
            if time.time() > self.lastupdate + self.updatetime:
                self.random_art()
                self.lastupdate = time.time()
            pass
