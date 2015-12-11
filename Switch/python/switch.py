#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

# A function to pass to the GPIO interupt
def callback_up(channel):
  print('Up detected on channel %s'%channel)

# A function to pass to the GPIO interupt
def callback_down(channel):
  print('Down detected on channel %s'%channel)

# A variable to store the GPIO associated with the switch
inputPin = 10

# Set the numbering scheme to use the BCM scheme
GPIO.setmode(GPIO.BCM)

# Set the GPIO associated with the PIR to be an input, with an
# internal pull up resistor.
GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Use a try-except statement to allow CTRL-C
try:
  # Can select RISING or FALLING or BOTH
  #GPIO.add_event_detect(inputPin, GPIO.RISING, callback=callback_up)
  GPIO.add_event_detect(inputPin, GPIO.FALLING, callback=callback_down)

  # Sleep forever, to keep the program running
  while True:
    time.sleep(100)

# If someone presses CTRL-C, then clean up the GPIO
except KeyboardInterrupt:
  GPIO.cleanup()
