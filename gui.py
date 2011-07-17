#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
GUI modul for lkwpchanger
"""

import time

class Window():
    
    def __init__(self, pictures):
        self.pictures = pictures
        self.timer_run = True
        print("Window.__init__()")
    
    def change_background(self, timer=False):
        if timer:
            while self.timer_run:
                self.pictures.change()
                time.sleep(float(self.pictures.options.elapsed_time))
        else:
            self.pictures.change()