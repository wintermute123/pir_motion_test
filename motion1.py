from gpiozero import MotionSensor, LED
from signal import pause
import time

pir = MotionSensor(17)
led = LED(4)


def turnon():
	led.on
	time.sleep(2)
	led.off	

pir.when_motion = turnon
pir.when_no_motion = led.off

pause()
