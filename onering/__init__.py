#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
"""

import sys
import os

class Singleton():
    
    def __init__(self):
        self.lockfile = sys.path[0] + '\\lockfile'
        try:
            if os.path.exists(self.lockfile):
                os.remove(self.lockfile)
            self.fd = os.open(self.lockfile, os.O_CREAT|os.O_EXCL|os.O_RDWR)
        except OSError:
            sys.exit("The program is already running")
            
    def __del__(self):
        if hasattr(self, 'fd'):
            os.close(self.fd)
            os.remove(self.lockfile)
        
if __name__ == "__main__":
    s1 = Singleton()
