install:
	ampy --port /dev/ttyACM0 put src/main.py
	ampy --port /dev/ttyACM0 put src/RgbButton.py
	ampy --port /dev/ttyACM0 put src/CatLed.py

run:
	make install
	ampy --port /dev/ttyACM0 run -n src/main.py
