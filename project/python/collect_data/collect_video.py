# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:51:13 2018

@author: Raimund
"""

import pyscreenshot as screen
import os

class CollectVideo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.num = 0
    
    def getScreen(self):
        im = screen.grab()
        return im
        
    def showScreen(self):
        im = self.getScreen()
        im.show()
        
    def saveScreen(self):
        #im = self.getScreen()
        my_image_name = "img_{}".format(self.num)
        complete_path = os.path.join(self.file_path, my_image_name)
        self.num += 1
        print(complete_path)
        
        im = screen.grab()
        im.save(complete_path)
        
        