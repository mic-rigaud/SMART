import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.OUT)        # sud
GPIO.setup(20, GPIO.OUT)        # nord
GPIO.setup(21, GPIO.OUT)        # est
GPIO.setup(22, GPIO.OUT)        # ouest

GPIO.output(22, True)
time.sleep(2)
GPIO.output(22, False)

