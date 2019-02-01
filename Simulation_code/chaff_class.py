#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:32:53 2019

@author: nehir
"""
import numpy as np

import lookup_table

class ChaffPiece():

    def __init__(self, dipole_characteristics, generated_initial_conditions):
        """
        Contains all the information needed to describe the current status od a chaff piece
        """
        self.position = generated_initial_conditions['initial_position']
        self.velocity = np.zeros((3,1)) #** THE MOTION WILL HAVE TO START IN THE DIRECCTION GIVEN BY oMEGA_0 **#
        self.length = dipole_characteristics['length']
        self.width = dipole_characteristics['width']
        self.height = dipole_characteristics['height']
        self.mass = self.length*self.width*self.height*dipole_characteristics['density']
        self.spiral_rate = generated_initial_conditions['Omega'] #Omega
        self.spiral_radius = generated_initial_conditions['spiral_radius'] #a
        self.angle_of_attack = None #alpha
        self.pitch_angle = None  #gamma
        self.drag_coefficient = None 
        self.rheynolds_number = None 
        

    def actualize_drag_coefficient(self):
        CA, CN = lookup_table.initiate_lookup(self.rheynolds_number, self.angle_of_attack)
        self.drag_coefficient = CA*np.cos(self.angle_of_attack)+CN*np.sin(self.angle_of_attack)
        return 
        
        
    def get_position(self):
        """
        Used to read out the current position of the chaff_piece
        output: position vector
        """
        tmp_position = self.position
        return tmp_position
                
                
    def set_position(self, x, y, z):
        """
        Used to write the current position of the chaff_piece
        input: new components of position vector
        """
        self.position = np.array([[x],[y],[z]])
        return
    
    def get_velocity(self):
        """
        Used to read out the current velocity of the chaff_piece
        output: velocity vector
        """
        tmp_velocity = self.velocity
        return tmp_velocity
                
                
    def set_velocity(self, vx, vy, vz):
        """
        Used to write the current velocity of the chaff_piece
        input: new components of velocity vector
        """
        self.velocity = np.array([[vx],[vy],[vz]])
        return