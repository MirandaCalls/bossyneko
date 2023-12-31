from machine import Pin
from neopixel import NeoPixel

class CatLed:
    def __init__(self, pinNum):
        self.neoPixel = NeoPixel(Pin(pinNum, Pin.OUT), 1)

    def assignColor(self, red, green, blue):
        self.neoPixel.fill((green, red, blue))
        self.neoPixel.write()

