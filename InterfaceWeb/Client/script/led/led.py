import RPi.GPIO as GPIO
import time

class Led():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(14, GPIO.IN)         # A1
        GPIO.setup(15, GPIO.IN)         # A0
        GPIO.setup(18, GPIO.IN)         # B7
        GPIO.setup(23, GPIO.IN)         # B6
        GPIO.setup(24, GPIO.IN)         # B5
        GPIO.setup(25, GPIO.IN)         # B4
        
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)          # A3
        GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)          # A2
        GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)         # B3
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)         # B2
        GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)         # B1
        GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)         # B0
        
    def getLed():
        if(GPIO.input(8)==0):
            if (GPIO.input(14)==1):
                return "led1"
            elif (GPIO.input(15)==1):
                return "led2" 
            elif (GPIO.input(18)==1):
                return "led3" 
            elif (GPIO.input(23)==1):
                return "led4" 
            elif (GPIO.input(24)==1):
                return "led5" 
            elif (GPIO.input(25)==1):
                return "led6" 
        elif(GPIO.input(7)==0):
            if (GPIO.input(14)==1):
                return "led7"
            elif (GPIO.input(15)==1):
                return "led8" 
            elif (GPIO.input(18)==1):
                return "led9" 
            elif (GPIO.input(23)==1):
                return "led10" 
            elif (GPIO.input(24)==1):
                return "led11" 
            elif (GPIO.input(25)==1):
                return "led12" 
        elif(GPIO.input(12)==0):
            if (GPIO.input(14)==1):
                return "led13"
            elif (GPIO.input(15)==1):
                return "led14" 
            elif (GPIO.input(18)==1):
                return "led15" 
            elif (GPIO.input(23)==1):
                return "led16" 
            elif (GPIO.input(24)==1):
                return "led17" 
            elif (GPIO.input(25)==1):
                return "led18" 
        elif(GPIO.input(16)==0):
            if (GPIO.input(14)==1):
                return "led19"
            elif (GPIO.input(15)==1):
                return "led20" 
            elif (GPIO.input(18)==1):
                return "led21" 
            elif (GPIO.input(23)==1):
                return "led22" 
            elif (GPIO.input(24)==1):
                return "led23" 
            elif (GPIO.input(25)==1):
                return "led24" 
        elif(GPIO.input(20)==0):
            if (GPIO.input(14)==1):
                return "led25"
            elif (GPIO.input(15)==1):
                return "led26" 
            elif (GPIO.input(18)==1):
                return "led27" 
            elif (GPIO.input(23)==1):
                return "led28" 
            elif (GPIO.input(24)==1):
                return "led29" 
            elif (GPIO.input(25)==1):
                return "led30" 
        elif(GPIO.input(21)==0):
            if (GPIO.input(14)==1):
                return "led31"
            elif (GPIO.input(15)==1):
                return "led32" 
            elif (GPIO.input(18)==1):
                return "led33" 
            elif (GPIO.input(23)==1):
                return "led34" 
            elif (GPIO.input(24)==1):
                return "led35" 
            elif (GPIO.input(25)==1):
                return "led36" 







