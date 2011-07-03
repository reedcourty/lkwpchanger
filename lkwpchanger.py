#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
lkwpchanger
"""

import argparse

VERSION = '0.0.0.20110703'
PICTURES_PATH = ".\\pictures"

class Options():
    """
    This class store some options
    """
    def __init__(self, results):    
        self.debug_mode = results.debug_mode
        
        if results.elapsed_time == None:
            self.one_running = True
        else:
            self.one_running = False
            self.elapsed_time = results.elapsed_time
        
        if results.pictures == None:
            self.pictures = PICTURES_PATH
        else:
            self.pictures = results.pictures
        
if __name__ == "__main__":
    print("LK Wallpaper Changer mostly for Gabi's WinXP")
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--pictures', '-p', action='store', dest='pictures',
                    help='The path of the pictures directory')
    
    parser.add_argument('--time', '-t', action='store', dest='elapsed_time',
                    help='The elapsed time between two background changes')
    
    parser.add_argument('--debug', '-d', action='store_true', default=False,
                    dest='debug_mode',
                    help='Set debug mode on')
    
    parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s '+VERSION)
    
    options = Options(parser.parse_args())
    
    if options.debug_mode:
        print('debug mode   =', options.debug_mode)
        print('one_running  =', options.one_running)
        print('elapsed_time =', options.elapsed_time)
        print('pictures     =', options.pictures)
        

