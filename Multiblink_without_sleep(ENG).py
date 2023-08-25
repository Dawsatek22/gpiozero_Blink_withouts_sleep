MIT License

Copyright (c) 2023 Jonathan Dawsa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



from gpiozero import PWMLED
import time

led =  PWMLED(21) # led pin 4 BCM
led2 =  PWMLED(4) # led pin 21 BCM
ftime = 2 # how long you want the led on
offtime = 0.5 # how long you wanna led off
ltime = -1 # last time the leds changed state

        
while True:
    now = time.monotonic()
    if not led.value:
        # is it time to turn the leds on
        if now >= ltime + offtime:
            led.value = 1
            led2.value = 1
            ltime = now
    if led.value:
        # is it time to turn the leds off
        if now >= ltime + ftime:
            led.value = 0
            led2.value = 0
            ltime = now
