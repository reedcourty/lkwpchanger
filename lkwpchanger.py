#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
lkwpchanger
"""

import os
import argparse
import hashlib
import random
import Image
import ctypes
import shutil
import sys
import time

VERSION = '0.0.0.20110703'
PICTURES_PATH = ".\\pictures"
BACKGROUND_IM = os.environ['USERPROFILE'] + \
     '\\Local Settings\\Application Data\\Microsoft\\Wallpaper1.bmp'
SPI_SETDESKWALLPAPER = 20
SPIF_SENDWININICHANGE = 0

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

class Pictures():
    
    def __init__(self, options):
        self.options = options
        self.filelist = None
        self.create_filelist()        
        self.act_picture = None
        
        self.get_next_picture()
        
    def create_filelist(self):
        if os.path.exists(options.pictures):
            self.filelist = os.listdir(options.pictures)
        else:
            if self.options.pictures == PICTURES_PATH:
                os.mkdir(options.pictures)
            try:
                self.filelist = os.listdir(options.pictures)
            except WindowsError as e:
                sys.exit(e.strerror + ': ' + self.options.pictures)
                
        if options.debug_mode:
            print("The contents of " + self.options.pictures + " directory: ")
            for f in self.filelist:
                print("\t" + f)
    
    def get_filelist(self):
        return self.filelist
        
    def get_next_picture(self):
        random.seed()
        try:
            i = random.randint(0,len(self.filelist)-1)
            self.act_picture = options.pictures + '\\' + self.filelist[i]
        except ValueError:
            sys.exit("The " + self.options.pictures + " directory is empty. :(")
    
    def get_hash(self, picture):
        f = open(picture, 'r')
        content = f.read()
        f.close()
        return(hashlib.md5(content).hexdigest())
    
    def change(self):
        
        OK = False
        
        while not OK:
            self.get_next_picture()
        
            converted = self.convert_to_bmp()
        
            if self.get_hash(self.act_picture) != self.get_hash(BACKGROUND_IM):
                OK = True
            
        shutil.copyfile(self.act_picture, BACKGROUND_IM)
        if converted:
            os.remove(self.act_picture)
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, BACKGROUND_IM, SPIF_SENDWININICHANGE)
   
    def get_image_type(self):
        img = Image.open(self.act_picture)
        return img.format

    def png_to_bmp(self, png_image):
        img = Image.open(png_image)
        img.load()
        if len(img.split()) == 4:
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
        img.save(png_image + '.bmp')
        self.act_picture = png_image + '.bmp'
    
    def jpg_to_bmp(self, jpg_image):
        img = Image.open(jpg_image)
        img.save(jpg_image + '.bmp')
        self.act_picture = jpg_image + '.bmp'
        
    def convert_to_bmp(self):
        itype = self.get_image_type()
    
        if itype == 'BMP':
            return False
        else:
            if itype == 'PNG':
                self.png_to_bmp(self.act_picture)
            if itype == 'JPEG':
                self.jpg_to_bmp(self.act_picture)
            return True


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
    
    pictures = Pictures(options)
    if options.one_running:
        pictures.change()
    else:
        while True:
            pictures.change()
            time.sleep(float(options.elapsed_time))
        

