#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse
import random
import datetime
import RPi.GPIO as GPIO
import adafruit_fancyled.adafruit_fancyled as fancy
import pyrebase
import math

GPIO.setmode(GPIO.BCM)

firebaseConfig={
    "apiKey": "AIzaSyC8FbNQy8YU69Za0UkKWq-uL6lS4xDdiBU",
    "authDomain": "raspberry-8d528.firebaseapp.com",
    "databaseURL": "https://raspberry-8d528-default-rtdb.firebaseio.com",
    "projectId": "raspberry-8d528",
    "storageBucket": "raspberry-8d528.appspot.com",
    "messagingSenderId": "419957445410",
    "appId": "1:419957445410:web:350e7358ff65c0db868b7b",
    "measurementId": "G-RF182QKRYV"
    }

firebase=pyrebase.initialize_app(firebaseConfig)
 
db=firebase.database()

trigger = 17
echo = 27

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

# LED strip configuration:
LED_COUNT      = 10      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

dist = 0
r = 0
g = 0
b = 0
opt = "off"
change = 0
color = Color(red,green,blue)
maxdist = 0

def getData():
    global h
    global v
    global opt
    global change
    global led
    s = 1;
    h=db.child("color").child("h").get().val()
    v=(db.child("color").child("v").get().val()) / 100
    opt=db.child("opt").child("opt").get().val()
    change=db.child("opt").child("change").get().val()
    led=db.child("led").child("led").get().val()

def hsv2rgb(h, s, v):
    global r
    global g
    global b
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = round(int(r * 255)), round(int(g * 255)), round(int(b * 255)) 

def TurnOn() :
    db.child("opt").update({"change":0})
    n = 0
    for i in range(strip.numPixels()):
        global r
        global g
        global b
        color = Color(r,g,b)
        strip.setPixelColor(n, color)
        strip.show()
        time.sleep(0.5)
        n = n + 4
    
    time.sleep(5)
    for i in range(strip.numPixels()):
        color = Color(0,0,0)
        strip.setPixelColor(i, color)
        strip.show()
    
    db.child("opt").update({"change":1})
        
def getDistance():
    global maxdist
    maxdist=db.child("distance").child("maxdistance").get().val()
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    
    start = time.time()
    stop = time.time()
    while GPIO.input(echo) == 0:
        start = time.time()
         
    while GPIO.input(echo) == 1:
        stop = time.time()
        
    global dist
    dist = ((stop - start) * 34300) / 2
        
def TurnOff():
    for i in range(strip.numPixels()):
        color = Color(0,0,0)
        strip.setPixelColor(i, color)
        time.sleep(0.5)
        strip.show()
        

    
# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            getDistance()
            
            if dist < maxdist:
                TurnOn()

    
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)

