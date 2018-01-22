# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:51:13 2018

@author: Raimund
"""

import pyautogui as screen
import os
import datetime

class CollectVideo:
    def __init__(self, file_path):
        self.file_path = file_path
        
        if not os.path.exists(file_path):
            # create folder
            os.makedirs(file_path)

    
    def getScreen(self):
        im = screen.screenshot()
        return im
        
    def showScreen(self):
        im = self.getScreen()
        im.show()
        
    def saveScreen(self):
        # save with usage of datetime
        time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")
        my_image_name = "img_{}{}".format(time, ".png")
        complete_path = os.path.join(self.file_path, my_image_name)
        print(complete_path)
        im = screen.screenshot()
        #im = screen.screenshot(complete_path)
        return complete_path
        