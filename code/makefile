install:
	ampy --port /dev/ttyACM0 put main.py
	ampy --port /dev/ttyACM0 put RgbButton.py

run:
	make install
	ampy --port /dev/ttyACM0 run -n main.py
