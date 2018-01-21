# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:51:13 2018

@author: Raimund
"""

import collect_input
import collect_video

controller_name = "Logitech Driving Force GT USB"
data_path = "E:\Projekte\autonomous dirt rally\autonomous_dirt_rally\data\test"

controller = collect_input.MyController(controller_name)
video = collect_video.CollectVideo(data_path)
clock = collect_input.pygame.time.Clock()

#while False:
    #clock.tick(1)
    #collect_video.screen.grab_to_file("test")
    #print("alive")

collect_input.Ryan.status()

while controller.controller_found:
    current_input = controller.getState()
    #video.saveScreen()
    clock.tick(1)
    print(current_input)