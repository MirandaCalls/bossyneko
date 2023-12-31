from machine import Pin
import time

class RgbButton:
    def __init__(self, ledNumRed, ledNumGreen, ledNumBlue, switchNum):
        self.ledPinRed = Pin(ledNumRed, Pin.OUT)
        self.ledPinGreen = Pin(ledNumGreen, Pin.OUT)
        self.ledPinBlue = Pin(ledNumBlue, Pin.OUT)
        self.switchPin = Pin(switchNum, Pin.IN, Pin.PULL_UP)
        self.switchPressCallback = None
        self.switchReleaseCallback = None
        self.switchPin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.switchHandler)
        self.lastSwitchValue = None

    def switchHandler(self, _):
        time.sleep_ms(80)

        currentValue = self.switchPin.value()
        if currentValue == self.lastSwitchValue:
            return

        if self.switchPin.value() == 1 and self.switchReleaseCallback != None:
            self.switchReleaseCallback()
        elif self.switchPressCallback != None:
            self.switchPressCallback()

        self.lastSwitchValue = currentValue

    def setSwitchPressHandler(self, callback):
        self.switchPressCallback = callback

    def setSwitchReleaseHandler(self, callback):
        self.switchReleaseCallback = callback

    def assignColor(self, red, green, blue):
        self.ledPinRed.value(0 if red else 1)
        self.ledPinBlue.value(0 if blue else 1)
        self.ledPinGreen.value(0 if green else 1)

    def turnOffLight(self):
        self.ledPinRed.value(1)
        self.ledPinBlue.value(1)
        self.ledPinGreen.value(1)

    def isButtonPressed(self):
        return self.switchPin.value() == 0

