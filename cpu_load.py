#!/usr/bin/env python
# based on https://github.com/pimoroni/blinkt/blob/master/examples/cpu_load.py
# added colors depending on cpu load
import time
from sys import exit
try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

import blinkt

blinkt.set_clear_on_exit()

def show_graph(v, r, g, b):
    v *= blinkt.NUM_PIXELS
    for x in range(blinkt.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
        blinkt.set_pixel(x, r, g, b)
        v -= 1

    blinkt.show()

blinkt.set_brightness(0.04) #dim those leds

while True:
    v = psutil.cpu_percent() / 100.0
    if v > 0.7: show_graph(v, 0, 102, 255); time.sleep (0.01) #red at 70% cpu load
    elif v > 0.3: show_graph(v, 255, 255, 0); time.sleep (0.01) #yellow at 30% cpu load
    else: show_graph(v, 0, 102, 255); time.sleep(0.01) #blue
