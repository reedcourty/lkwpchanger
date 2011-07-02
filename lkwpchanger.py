#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse

VERSION = '0.0.0.20110703'

if __name__ == "__main__":
    print("LK Wallpaper Changer mostly for Gabi's WinXP")
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--delay', '-d', action='store', dest='delay',
                    help='Delay')
    
    parser.add_argument('--version', '-v', action='version', version='%(prog)s '+VERSION)
    
    results = parser.parse_args()
    print 'delay =', results.delay

