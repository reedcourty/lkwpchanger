#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
lkwpchanger
"""

import argparse
import sys

from PySide import QtGui

from model import Pictures, Options
from gui import Window, TimerThread
from onering import Singleton

VERSION = (0, 0, 0, 'alpha', 20110717)

if __name__ == "__main__":
    
    s = Singleton()
    
    print("LK Wallpaper Changer mostly for Gabi's WinXP")
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--pictures', '-p', action='store', dest='pictures',
                    help='The path of the pictures directory')
    
    parser.add_argument('--time', '-t', action='store', dest='elapsed_time',
                    help='The elapsed time between two background changes')
    
    parser.add_argument('--debug', '-d', action='store_true', default=False,
                    dest='debug_mode',
                    help='Set debug mode on')
    
    prog_version = "%s.%s.%s.%s" % (VERSION[0], VERSION[1],
                                    VERSION[2], VERSION[4])
    
    parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s ' + prog_version) 
    
    options = Options(parser.parse_args())
    
    if options.debug_mode:
        print('debug mode   =', options.debug_mode)
        print('one_running  =', options.one_running)
        print('elapsed_time =', options.elapsed_time)
        print('pictures     =', options.pictures)
    
    app = QtGui.QApplication(sys.argv)
    
    if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        QtGui.QMessageBox.critical(None, "lkwpchanger",
                                   "The application couldn't start.")
        sys.exit(1)
    
    QtGui.QApplication.setQuitOnLastWindowClosed(False)
    
    pictures = Pictures(options)
    window = Window(pictures)
    timer = TimerThread(args=(window))
    if options.one_running:
        window.change_background()
    else:
        timer.start()
    
    sys.exit(app.exec_())  

