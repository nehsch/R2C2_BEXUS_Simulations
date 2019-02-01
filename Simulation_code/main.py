#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 02:54:06 2019

@author: nehir
"""

import numpy as np
import initial_conditions
import chaff_class

def use_testvalues():
    """
    Sets the dipole sizes to what is used in Brunk's "Chaff Aerodynamics".
    Output: test dimensions for foil-type dipoles.
    """
    length = 0.045212 #m
    width = 0.0001524 #m
    height = 1.143e-5 #m
    density = 2698,79071 # kg/m^3
    return {'length': length, 'width': width, 'height': height, 'density': density}

def dipole_initial_conditions(nr_dipoles):
    Omega_0 = initial_conditions.initial_spiral_angle(nr_dipoles)
    Omega = initial_conditions.initiate_spiral_rate(nr_dipoles)
    a = initial_conditions.initiate_spiral_radius(nr_dipoles)
    theta = initial_conditions.initial_angle(nr_dipoles)
    position = initial_conditions.initial_position(nr_dipoles)
    return {'Omega_0': Omega_0, 'Omega': Omega, 'spiral_radius': a, 'theta': theta, 'initial_position': position} 

def initiate_chaff_pieces(nr_dipoles):
    """
    Uses the generated initial conditions to create each chaff dipole as an instance of class ChaffPiece
    input: initial conditions data
    output: list of ChaffPiece instances
    """
    pieces_dict = {}
    for i in range(nr_dipoles):
        pieces_dict[i] = chaff_class.ChaffPiece()
    return 0


if __name__=='__main__':    
    
    dipole_characteristics = use_testvalues() #length, width, height
    number_of_dipoles = 10
    
    generated_initial_conditions = dipole_initial_conditions(number_of_dipoles)
    
    dipoles_dict = initiate_chaff_pieces(number_of_dipoles, dipole_characteristics, generated_initial_conditions)
    
    
    
    
    