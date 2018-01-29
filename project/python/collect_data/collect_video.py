# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:51:13 2018

@author: Raimund
"""

import pyautogui as screen
import mss
import os
import datetime
import numpy as np

class CollectVideo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.collected_videos = list()
        self.recorder = mss.mss()
        self.monitor = {'top': 0, 'left': 0, 'width': 3840, 'height': 2160}

        
        if not os.path.exists(file_path):
            # create folder
            os.makedirs(file_path)

    def __str__(self):
        return "Not implemented"
    
    def getScreen(self):
        im = screen.screenshot()
        return im
        
    def showScreen(self):
        im = self.getScreen()
        im.show()
        
    def collectScreen(self):
        # collect with usage of datetime for file_path later on
        time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")
        my_image_name = "img_{}{}".format(time, ".png")
        complete_path = os.path.join(self.file_path, my_image_name)
        im = screen.screenshot()
        
        self.collected_videos.append((complete_path, im))
        return complete_path
    
    def collectScreenFast(self):
        time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")
        my_image_name = "img_{}{}".format(time, ".png")
        complete_path = os.path.join(self.file_path, my_image_name)
        im = np.array(self.recorder.grab(self.monitor))
        
        self.collected_videos.append((complete_path, im))
        return complete_path
    
    def update_progress(self, workdone):
        print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(workdone * 50), workdone*100), end="", flush=True)
              
    def saveDataAndClear(self):
        all_imgs= float(len(self.collected_videos));
        curr_img_counter = 1.0;
        for path, im in self.collected_videos:
            im.save(path)
            progress = curr_img_counter/all_imgs
            self.update_progress(progress)
            curr_img_counter += 1
        
        print() # go to next line
        self.clearCollected()
    
    def clearCollected(self):
        self.collected_videos.clear()
    
    def deleteLatestData(self, amount_to_delete):
        if amount_to_delete > 0:
            del self.collected_videos[-amount_to_delete:]
        
    def saveScreen(self):
        # save with usage of datetime
        time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")
        my_image_name = "img_{}{}".format(time, ".png")
        complete_path = os.path.join(self.file_path, my_image_name)
        print(complete_path)
        im = screen.screenshot()
        #im = screen.screenshot(complete_path)
        return complete_path
        