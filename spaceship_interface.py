"""
Spaceship Interface 
A Python/nanpy port of the SpaceshipInterface Sketch from the Arduino Starter Kit ( http://arduino.cc/starterKit)
"""
__version__ = '1.0'
__author__ = 'mc7h'
__license__ = 'None'

from nanpy import Arduino as A
switchstate = 0

# SETUP:
A.pinMode(3, A.OUTPUT)
A.pinMode(4, A.OUTPUT)
A.pinMode(5, A.OUTPUT)

A.pinMode(2, A.INPUT)

# LOOP:
while True:
    switchState = A.digitalRead(2)
    if switchState == A.LOW:
        A.digitalWrite(3, A.HIGH) # turn the green LED on pin 3 on
        A.digitalWrite(4, A.LOW)  # turn the red LED on pin 4 off
        A.digitalWrite(5, A.LOW)  # turn the red LED on pin 5 off
    else:
        A.digitalWrite(3, A.LOW);  # turn the green LED on pin 3 off
        A.digitalWrite(4, A.LOW);  # turn the red LED on pin 4 off
        A.digitalWrite(5, A.HIGH); # turn the red LED on pin 5 on
        
        # wait for a quarter second before changing the light
        A.delay(250);
        A.digitalWrite(4, A.HIGH); #// turn the red LED on pin 4 on
        A.digitalWrite(5, A.LOW);  #// turn the red LED on pin 5 off
        
        # wait for a quarter second before changing the light
        A.delay(250);