import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(4,GPIO.OUT)
def MOTION(PIR_PIN):
    GPIO.output(4,1)
    print "Motion Detected!   "
    print "PIR Module Test (CTRL+C to exit):"
    os.system("raspistill -t 10000 -vf")
    #    time.sleep(2)
    print "Ready"
    GPIO.output(4,0)
    
    
try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print " Quit"
GPIO.cleanup()
