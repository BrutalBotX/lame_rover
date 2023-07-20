import os
import system
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

pkill -f car_back.py
pkill -f car_left.py
pkill -f car_right.py
pkill -f car_halt.py

try:
        while True:   
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(38,False)
                GPIO.output(40,True)
             
finally:
    GPIO.cleanup()
    
