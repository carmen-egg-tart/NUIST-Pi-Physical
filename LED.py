import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set GPIO 18 as output mode
GPIO.setup(18, GPIO.OUT)

# Turn on the LED
print("LED on")
GPIO.output(18, GPIO.HIGH)
time.sleep(1)

# Turn off the LED
print("LED off")
GPIO.output(18, GPIO.LOW)

# Clean up GPIO settings
GPIO.cleanup()
