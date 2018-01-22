# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:51:13 2018

@author: Raimund
"""

import pygame
import os
import numpy as np

class MyController:
    def __init__(self, controller_name, file_path):
        self.controller_name = controller_name
        self.getController()
        self.collected_states = list()
        
        self.file_path = file_path
        dir_path = os.path.dirname(file_path)
        # check if the dir exists
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
    def __str__(self):
        return str(self.collected_states)
                
    def getController(self):
        # search for correct controller
        pygame.init()
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        self.controller_found = False
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            
            if(joystick.get_name() == self.controller_name):
                self.controller = joystick;
                self.controller_found = True
                self.printInfo()

                    
    def printInfo(self):
        print("Name: ", self.controller.get_name())

    def getState(self):
        # the import values are:
        # Axis 0 -> steering
        # Axis 2 -> increase speed
        # Axis 3 -> decrease speed
        
        my_controller_state = {}
        
        # check if initialized
        my_controller_state["Valid"] = self.controller_found
        if(not self.controller_found):
            return my_controller_state
        
        pygame.event.pump() # otherwise get_axis always returns 0.0
        
        # Axis 0
        axis = self.controller.get_axis(0)
        #print(axis)
        my_controller_state["steering_value"] = float(axis)
        
        # Axis 2
        axis = self.controller.get_axis(2)
        #print(axis)
        my_controller_state["increase_speed"] = float(axis)
        
        # Axis 3
        axis = self.controller.get_axis(3)
        #print(axis)
        my_controller_state["decrease_speed"] = float(axis)
        
        return my_controller_state
    
    def collectState(self, corr_img_path):
        current_state = self.getState()
        current_state["img_path"] = corr_img_path
        self.collected_states.append(current_state)

    def getAllStates(self):
        return self.collected_states
    
    def deleteLatestData(self, amount_to_delete):
        if amount_to_delete > 0:
            del self.collected_states[-amount_to_delete:]

    def clearAllStates(self):
        self.collected_states.clear()
        
    def saveDataAndClear(self):
        
        np.savetxt(self.file_path, self.getAllStates())
        self.clearAllStates()
