import utime
import random

class RgbButton:
    def __init__(self, ledPinRed, ledPinGreen, ledPinBlue, switchPin):
        self.ledPinRed = ledPinRed
        self.ledPinGreen = ledPinGreen
        self.ledPinBlue = ledPinBlue
        self.switchPin = switchPin

    def assignRandomColor(self):
        self.ledPinRed.value(random.randint(0,1))
        self.ledPinGreen.value(random.randint(0,1))
        self.ledPinBlue.value(random.randint(0,1))
        if (
                (self.ledPinRed.value() == 1 and self.ledPinGreen.value() == 1 and self.ledPinBlue.value() == 1) or
                (self.ledPinRed.value() ==1 and self.ledPinGreen.value() == 0 and self.ledPinBlue.value() == 1)
            ):
            self.assignRandomColor()

    def assignColor(self, redColor, blueColor, greenColor):
        self.ledPinRed.value(redColor)
        self.ledPinBlue.value(blueColor)
        self.ledPinGreen.value(greenColor)

    def turnOffLight(self):
        self.ledPinRed.value(1)
        self.ledPinBlue.value(1)
        self.ledPinGreen.value(1)

    def isButtonPressed(self):
        return self.switchPin.value() == 0
