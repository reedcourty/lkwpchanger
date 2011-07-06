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
import datetime

VERSION = '0.0.0.20110706'
PICTURES_PATH = sys.path[0] + "\\pictures"
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
    
    def __init__(self, opts):
        self.options = opts
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
            except WindowsError as error:
                sys.exit(error.strerror + ': ' + self.options.pictures)
                
        if options.debug_mode:
            print("The contents of " + self.options.pictures + " directory: ")
            for entry in self.filelist:
                print("\t" + entry)
    
    def get_filelist(self):
        return self.filelist
        
    def get_next_picture(self):
        random.seed()
        try:
            picture = random.choice(self.filelist)
            self.act_picture = options.pictures + '\\' + picture
        except ValueError:
            sys.exit("The " + self.options.pictures + " directory is empty. :(")
    
    def get_hash(self, picture):
        picture_file = open(picture, 'r')
        content = picture_file.read()
        picture_file.close()
        return(hashlib.md5(content).hexdigest())
    
    def change(self):
        
        is_new_image = False
        
        self.create_filelist()
        
        while not is_new_image:
            self.get_next_picture()
        
            self.convert_to_bmp()
            
            if (len(self.filelist) <= 1) or \
                (self.get_hash(self.act_picture) \
                != self.get_hash(BACKGROUND_IM)):
                is_new_image = True
            else:
                os.remove(self.act_picture)
                     
        shutil.copyfile(self.act_picture, BACKGROUND_IM)
        os.remove(self.act_picture)
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER,
                                                   0,
                                                   BACKGROUND_IM,
                                                   SPIF_SENDWININICHANGE)
   
    def get_image_type(self):
        img = Image.open(self.act_picture)
        return img.format

    def get_converted_filename(self):
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = PICTURES_PATH + '\\converted-' + now + '.bmp'
        if self.options.debug_mode:
            print(filename)
        return filename

    def png_to_bmp(self, png_image):
        img = Image.open(png_image)
        img.load()
        if len(img.split()) == 4:
            r, g, b, _ = img.split() # The "_" fixed the unused variable warning
            img = Image.merge("RGB", (r, g, b))
        filename = self.get_converted_filename()
        img.save(filename)
        self.act_picture = filename
    
    def jpg_to_bmp(self, jpg_image):
        img = Image.open(jpg_image)
        filename = self.get_converted_filename()
        img.save(filename)
        self.act_picture = filename
        
    def bmp_to_bmp(self, bmp_image):
        filename = self.get_converted_filename()
        shutil.copyfile(bmp_image, filename)
        self.act_picture = filename
        
    def convert_to_bmp(self):
        itype = self.get_image_type()
    
        if itype == 'BMP':
            self.bmp_to_bmp(self.act_picture)
        if itype == 'PNG':
            self.png_to_bmp(self.act_picture)
        if itype == 'JPEG':
            self.jpg_to_bmp(self.act_picture)

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
        

