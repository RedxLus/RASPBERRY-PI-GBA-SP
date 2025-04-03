import RPi.GPIO as GPIO

SCREEN_POWER_GPIO = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SCREEN_POWER_GPIO, GPIO.OUT)

GPIO.output(SCREEN_POWER_GPIO, GPIO.HIGH)
