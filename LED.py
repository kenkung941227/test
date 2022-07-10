import RPi.GPIO as GPIO
import time
    
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("Lights off")
GPIO.output(18,GPIO.LOW)
print("Lights on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print("Lights off")
GPIO.output(18,GPIO.LOW)
time.sleep(1)
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print("Lights off")
GPIO.output(18,GPIO.LOW)
GPIO.cleanup()
