# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:51:13 2018

@author: Raimund
"""

import pygame

class MyController:
    def __init__(self, controller_name):
        self.controller_name = controller_name
        self.getController()
        
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
        if(not self.controller_found):
            return {"Not Valid":0.0}
        
        pygame.event.pump() # otherwise get_axis always returns 0.0
        
        my_controller_state = {}
        
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

class Ryan:
    def status():
        print("hahaha 2")