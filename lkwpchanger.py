#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse

VERSION = '0.0.0.20110702'

if __name__ == "__main__":
    print("LK Wallpaper Changer mostly for Gabi's WinXP")
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--delay', action='store', dest='delay',
                    help='Delay')
    
    parser = argparse.ArgumentParser(version=VERSION)
    
    results = parser.parse_args()
    print 'delay =', results.delay

