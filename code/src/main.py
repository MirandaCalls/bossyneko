import random
from machine import Timer
from RgbButton import RgbButton
from CatLed import CatLed
import time

def main():
    color = (0, 0, 0)

    button = RgbButton(18, 19, 20, 21)
    button.turnOffLight()

    strobeCat = False
    catLed = CatLed(2)

    def wakeUpNeko():
        nonlocal color
        color = randomColor()

        button.assignColor(color[0], color[1], color[2])

        nonlocal strobeCat
        strobeCat = True

    timer = Timer()
    def sleep():
        button.turnOffLight()
        nonlocal strobeCat
        strobeCat = False

        timer.deinit()
        timer.init(period=1000 * 5, mode=Timer.ONE_SHOT, callback=lambda t: wakeUpNeko())

    wakeUpNeko()
    button.setSwitchReleaseHandler(sleep)

    while True:
        if strobeCat == False:
            time.sleep(1)
            continue

        for i in range(0, 2 * 256, 8):
            if strobeCat == False:
                catLed.assignColor(0, 0, 0)
                break;

            time.sleep(0.05)

            if (i // 256) % 2 == 0:
                val = i
            else:
                val = 255 - i

            catLed.assignColor(
                val if color[0] else 0,
                val if color[1] else 0,
                val if color[2] else 0
            )

def randomColor():
    red = bool(random.randint(0, 1))
    green = bool(random.randint(0, 1))
    blue = bool(random.randint(0, 1))
    if (
        (red == 1 and green == 1 and blue == 1) or
        (red == 1 and green == 0 and blue == 1) or
        (red == 0 and green == 0 and blue == 0)
    ):
        return randomColor()

    return (red, green, blue)

if __name__ == "__main__":
    main()
