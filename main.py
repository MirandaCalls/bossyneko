import machine
from machine import Timer
from RgbButton import RgbButton

def main():
    button = RgbButton(
        machine.Pin(18, machine.Pin.OUT),
        machine.Pin(19, machine.Pin.OUT),
        machine.Pin(20, machine.Pin.OUT),
        machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
    )

    button.assignRandomColor()
    is_pushed = False
    timer = Timer(-1)
    
    while True:
        if button.isButtonPressed():
            is_pushed = True
 
        elif not button.isButtonPressed():
            if is_pushed == True:
                button.turnOffLight()
                timer.deinit()
                timer.init(period=10000, mode=Timer.ONE_SHOT, callback=lambda t: button.assignRandomColor())

            is_pushed = False

if __name__ == "__main__":
    main()
