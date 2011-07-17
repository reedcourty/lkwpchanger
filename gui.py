#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
GUI modul for lkwpchanger
"""

import sys
import time
import threading

from PySide import QtGui

ICONS_PATH = sys.path[0] + "\\icons\\"

class TimerThread(threading.Thread):
        
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name,
                                  verbose=verbose)
        self.window = args
    
    def run(self):
        while self.window.timer_running:
            self.window.pictures.change()
            time.sleep(float(self.window.pictures.options.elapsed_time))
        
class Window(QtGui.QDialog):
    
    def __init__(self, pictures):
        self.pictures = pictures
        self.timer_running = True
        
        super(Window, self).__init__()
        self.create_actions()
        self.create_tray_icon()
        self.set_icon()
        self.trayIcon.show()
                
    def set_icon(self):
        icon = QtGui.QIcon(ICONS_PATH + 'lkwpchanger.png')
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)
        
    def quit(self):
        self.timer_running = False
        QtGui.qApp.quit()
        
    def create_actions(self):
        
        self.changeAction = QtGui.QAction("&Change", self,
                                        triggered=self.change_background,
                                        icon=None)
        self.quitAction = QtGui.QAction("&Quit", self,
                                        triggered=self.quit,
                                        icon=QtGui.QIcon(ICONS_PATH + 'quit.png'))
    
    def create_tray_icon(self):
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.changeAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)
            
    def change_background(self):
        self.pictures.change()
