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
import pyrebase
import datetime
import RPi.GPIO as GPIO
import adafruit_fancyled.adafruit_fancyled as fancyű
import math

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

# LED strip configuration:
LED_COUNT      = 13     # Number of LED pixels.
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
h = 360
s = 1
v = 1
led = 4

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


def cahngeMan():
    n = 0
    global r
    global g
    global b
    global change
    global led
    global opt
            
    for i in range(strip.numPixels()):
        color = Color(r,g,b)
        strip.setPixelColor(n, color)
        strip.show()
        n = n + led

def changeAuto():
    global h
    global s
    global v
    global r
    global g
    global b
    global change
    global led
    global opt
    now = datetime.datetime.now()
    minute = now.minute % 10
    n = 0
    if minute == 5 or minute == 0:
        getData()
        if change == 1:
            db.child("opt").update({"change":0})
            h = random.randint(0,360)
            hsv2rgb(h,s,v)
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, Color(0,0,0))
                strip.show()
            for i in range(strip.numPixels()):
                opt=db.child("opt").child("opt").get().val()
                color = Color(r,g,b)
                strip.setPixelColor(n, color)
                strip.show()
                n = n + led
                time.sleep(0.1)
    else:
        db.child("opt").update({"change":1})

def snowing():
    current = random.randint(1,10)
    choices = [0.01, 0.1, 0.05, 0.005, 0.009, 0.03, 0.07, 0.001, 0.06]
    delay = random.choice(choices)
    r,g,b = 0,0,0
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()
    for i in range(255):
        opt=db.child("opt").child("opt").get().val() 
        r = r+1
        g = g+1
        b = b+1
        color = Color(r,g,b)
        strip.setPixelColor(current, color)
        strip.show()
        time.sleep(delay)
    for i in range(255):
        opt=db.child("opt").child("opt").get().val()
        r = r-1
        g = g-1
        b = b-1
        color = Color(r,g,b)
        strip.setPixelColor(current, color)
        strip.show()
        time.sleep(delay)

def rainbow():
    global r
    global g
    global b
    global led
    global change
    global opt
    h = 0
    s = 1
    v = 1
    for i in range(360):
        n = 0
        opt=db.child("opt").child("opt").get().val()
        h = h+1;
        hsv2rgb(h,s,v)
        for x in range(strip.numPixels()):
            color = Color(r,g,b)
            strip.setPixelColor(n, color)
            strip.show()
            n = n + led
        time.sleep(0.05)

def white():
    global change
    global led
    global opt
    n = 0
    if change == 1:
        db.child("opt").update({"change":0})
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0,0,0))
            strip.show()
        for i in range(strip.numPixels()):
            opt=db.child("opt").child("opt").get().val()
            color = Color(255,255,255)
            strip.setPixelColor(n, color)
            strip.show()
            n = n + led
            time.sleep(0.05)


def TurnOff():
    global change
    global led
    global opt
    n = 0
    if change == 1:
        db.child("opt").update({"change":0})
        for i in range(strip.numPixels()):
            opt=db.child("opt").child("opt").get().val()
            color = Color(0,0,0)
            strip.setPixelColor(n, color)
            strip.show()
            n = n + led
            time.sleep(0.1)

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
            getData()

            if opt == "man":
                hsv2rgb(h,s,v)
                cahngeMan()
            if opt == "auto":
                changeAuto()
            if opt == "snow":
                snowing()
            if opt == "rainbow":
                rainbow()
            if opt == "off":
                TurnOff()
            if opt == "white":
                white()


    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
