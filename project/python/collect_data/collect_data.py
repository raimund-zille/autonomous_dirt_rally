# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:51:13 2018

@author: Raimund
"""

import collect_input
import collect_video
import os
import time
import datetime


class CollectData:
    def __init__(self, controller_name, data_path, frequenzy):
        # initialize member variables
        self.freq = frequenzy
        self.wait = 1.0/frequenzy
        self.controller_name = controller_name
        self.data_path = data_path
        self.video_collector = collect_video.CollectVideo(data_path)
        
        # create file_path for input_collector
        file_path = os.path.join(data_path, "data.csv")
        self.input_collector = collect_input.MyController(controller_name, data_path)
        
    def __str__(self):
        return "Not implemented"
        
    def collectData(self):
        # ask user how long to wait till starting to collect
        wait_sec_before_collecting_data = float(input("Time before start collecting [s]: "))
        print("Waiting ", wait_sec_before_collecting_data, " seconds.")
        time.sleep(wait_sec_before_collecting_data)
        
        # track overall time collecting data
        time_start = time.clock()
        
        # collect data
        self.collectDataTillInterupted()
        
        time_end = time.clock()
        time_collected = time_end - time_start
        
        print("Time collected: ", str(datetime.timedelta(seconds=time_collected)))
        
        # ask user how much of the latest data shall be deleted
        delete_last_x_sec = float(input("Delete last x seconds collected: "))
        print("Deleting collected data of last ",delete_last_x_sec," seconds.")
        
        # delete latest data
        amount_to_delete = int(delete_last_x_sec*self.freq)
        self.video_collector.deleteLatestData(amount_to_delete)
        self.input_collector.deleteLatestData(amount_to_delete)
        
        # save data to folder
        self.video_collector.saveDataAndClear()
        self.input_collector.saveDataAndClear();
        
        
        
        
        
    def collectDataTillInterupted(self):
        # wrap infinite loop in try catch block so user can escape with ctrl+c
        try:
            while True:
                # track time to achieve a stable 10 Hz rate
                time_before = time.clock()
                im_path = self.video_collector.collectScreen()
                self.input_collector.collectState(im_path)
                print("Collecting data! Ctrl-C to interrupted")
                time_diff = time.clock() - time_before
                
                # sleep diffrenz
                if(self.wait<=time_diff):
                    print("[Warning] can't achieve ", self.freq," Hz... time_needed: ", time_diff)
                else:
                    time.sleep(self.wait - time_diff)
        
        except KeyboardInterrupt:
            print("Finished collecting!")
            

controller_name = "Logitech Driving Force GT USB"
data_path = os.path.abspath("test")

#controller = collect_input.MyController(controller_name)
#video = collect_video.CollectVideo(data_path)
#clock = collect_input.pygame.time.Clock()
#
##while False:
#    #clock.tick(1)
#    #collect_video.screen.grab_to_file("test")
#    #print("alive")
#delta = collect_video.datetime.timedelta(0)
#for i in range(10):
#    t1 = collect_video.datetime.datetime.now()
#    img_path = video.collectScreen()
#    controller.collectState(img_path)
#    t2 = collect_video.datetime.datetime.now()
#    delta += t2-t1
#    clock.tick()
#
#video.saveCollectedAndClear()
#print(delta/10)
#print(controller.getAllStates())
#controller_file_path = os.path.join(data_path + "controlls.npy")
#
#controller.saveAllStatesAndClear(controller_file_path)
#
## Load
#test = collect_input.np.load(controller_file_path)
#print(test)

collectData = CollectData(controller_name, data_path, 10)
collectData.collectData()
print("success!!!")


                
                
                