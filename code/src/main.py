from machine import Timer
from RgbButton import RgbButton

def main():
    button = RgbButton(18, 19, 20, 21)
    button.assignRandomColor()

    timer = Timer()
    def sleep():
        button.turnOffLight()
        timer.deinit()
        timer.init(period=10000, mode=Timer.ONE_SHOT, callback=lambda t: button.assignRandomColor())
    button.setSwitchReleaseHandler(sleep)

if __name__ == "__main__":
    main()
