import random
from machine import Timer, Pin
from RgbButton import RgbButton

def main():
    ledCatRed = Pin(0, Pin.OUT)
    ledCatRed.value(0)
    ledCatGreen = Pin(1, Pin.OUT)
    ledCatGreen.value(0)
    button = RgbButton(18, 19, 20, 21)
    button.turnOffLight()

    def wakeUpNeko():
        isRed = random.randint(0,1)
        if isRed == 1:
            button.assignColor(True, False, False)
            ledCatRed.value(1)
        else:
            button.assignColor(False, False, True)
            ledCatGreen.value(1)

    timer = Timer()
    def sleep():
        ledCatRed.value(0)
        ledCatGreen.value(0)
        button.turnOffLight()

        timer.deinit()
        timer.init(period=1000*60*60, mode=Timer.ONE_SHOT, callback=lambda t: wakeUpNeko())

    wakeUpNeko()
    button.setSwitchReleaseHandler(sleep)

if __name__ == "__main__":
    main()
