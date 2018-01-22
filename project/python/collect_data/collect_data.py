# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:51:13 2018

@author: Raimund
"""

import collect_input
import collect_video
import os

controller_name = "Logitech Driving Force GT USB"
data_path = os.path.abspath("test")

controller = collect_input.MyController(controller_name)
video = collect_video.CollectVideo(data_path)
clock = collect_input.pygame.time.Clock()

#while False:
    #clock.tick(1)
    #collect_video.screen.grab_to_file("test")
    #print("alive")
delta = collect_video.datetime.timedelta(0)
for i in range(10):
    t1 = collect_video.datetime.datetime.now()
    img_path = video.saveScreen()
    controller.collectState(img_path)
    t2 = collect_video.datetime.datetime.now()
    delta += t2-t1
    clock.tick(20)

video.showScreen()
print(delta/10)
print(controller.getAllStates())
controller_file_path = os.path.join(data_path + "controlls.npy")

controller.saveAllStatesAndClear(controller_file_path)

# Load
test = collect_input.np.load(controller_file_path)
print(test)