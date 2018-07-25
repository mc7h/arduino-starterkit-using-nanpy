Arduino Starter Kit using Nanpy
===============================

There are 14 Sketches / Projects present in the 'Arduino Projects Book' that accompanies the Arduino Uno Starter Kit (http://arduino.cc/starterkit). Using Nanpy, I've started to port these over to the Python; hopefully this will be helpful for those of us looking to interact with the Arduino from our Raspberry Pis and 'big computers'.

## Sketches

1. Spaceship Interface
2. Love-o-Meter

## Issues

### Love-o-Meter 

Reading from a Temperature Sensor when the Arduino is connected to my MacBook I get the following: 

    Sensor value: 154, Volts: 0.751953125, Degrees C: 25.1953125.
    
However, on my RPi I get the following readings:

    Sensor value: 165, Volts: 0.8056640625, Degrees C: 30.56640625.
    
Obviously the Pi is wrong. I believe, it's some kind of voltage reference problem.


## Links

 * Nanpy (https://github.com/nanpy/nanpy)
 * Nanpy Firmware (https://github.com/nanpy/nanpy-firmware)


## License

None.
