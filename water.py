import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def water(sleepyTime):
	relay = 4
	
	GPIO.setup(relay, GPIO.OUT)
	GPIO.output(relay, GPIO.LOW)
	GPIO.output(relay, GPIO.HIGH)

	time.sleep(sleepyTime)
	GPIO.output(relay, GPIO.LOW)
