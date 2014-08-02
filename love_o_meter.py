"""
Love O Meter
A Python/nanpy port of the LoveOMeter Sketch from the Arduino Starter Kit ( http://arduino.cc/starterKit)
"""
__version__ = '1.0'
__author__ = 'mc7h'
__license__ = 'None'

from nanpy import Arduino as A

SENSOR_PIN_A0 = 14 
BASELINE_TEMP = 20.0

# SETUP
A.pinMode(2, A.OUTPUT)
A.digitalWrite(2, A.LOW)
A.pinMode(3, A.OUTPUT)
A.digitalWrite(3, A.LOW)
A.pinMode(4, A.OUTPUT)
A.digitalWrite(4, A.LOW)

# LOOP
while True:
    sensorVal = A.analogRead(SENSOR_PIN_A0)
    voltage = (sensorVal / 1024.0) * 5.0
    temperature = (voltage - 0.5) * 100
    print("Sensor value: " + str(sensorVal) + ", Volts: " + str(voltage)  +", Degrees C: " + str(temperature) + ".")
    
    # if the current temperature is lower than the baseline turn off all LEDs
    if temperature < BASELINE_TEMP:
        A.digitalWrite(2, A.LOW)
        A.digitalWrite(3, A.LOW)
        A.digitalWrite(4, A.LOW)
    # if the temperature rises 2-4 degrees, turn an LED on 
    elif (temperature >= BASELINE_TEMP + 2 and temperature < BASELINE_TEMP + 4):
        A.digitalWrite(2, A.HIGH)
        A.digitalWrite(3, A.LOW)
        A.digitalWrite(4, A.LOW)
    # if the temperature rises 4-6 degrees, turn a second LED on  
    elif (temperature >= BASELINE_TEMP + 4 and temperature < BASELINE_TEMP + 6):
        A.digitalWrite(2, A.HIGH)
        A.digitalWrite(3, A.HIGH)
        A.digitalWrite(4, A.LOW)
    # if the temperature rises more than 6 degrees, turn all LEDs on
    elif (temperature >= BASELINE_TEMP + 6):
        A.digitalWrite(2, A.HIGH)
        A.digitalWrite(3, A.HIGH)
        A.digitalWrite(4, A.HIGH)
    A.delay(1)