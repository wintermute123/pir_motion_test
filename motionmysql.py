#turn on PIR.  When Motion Detected, turn on camera for 5 seconds
import RPi.GPIO as GPIO
import time
import os
import mysql.connector
import datetime

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(4,GPIO.OUT)
def MOTION(PIR_PIN):
    GPIO.output(4,1)

    cnx = mysql.connector.connect(user='ROOT', password='Marlboro123',
                                  host='192.168.1.19',
                                  database='raspiquarium')
    cursor = cnx.cursor()

    nowtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_temp = ("insert into security"
                "(eventid, date,sensor,eventdata) "
                " values (%s, %s, %s, %s)")
    data_temp = ('',nowtime,'TheSprawlPir1','Motion Detected')
    
    cursor.execute(add_temp,data_temp)
    cnx.commit()

    cursor.close()
    cnx.close()






    print "Motion Detected!   "
    print "PIR Module Test (CTRL+C to exit):"

    os.system("raspistill -t 60000 -tl 5000 -vf -o /home/pi/images/images%d.jpg -dt  -h 480 -w 640")
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
