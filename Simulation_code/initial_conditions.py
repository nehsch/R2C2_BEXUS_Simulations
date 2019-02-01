#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:43:47 2019

@author: nehir
"""

import numpy as np
import scipy.stats as sp 
from matplotlib import pyplot as plt


def initial_spiral_angle(amount_dipoles):
    """
    Initial angular position on the spiral circle
    Follows a uniform distribution between 0 and 2*pi
    """
    Omega_0 = sp.uniform.rvs(loc=0, scale=2*np.pi, size=amount_dipoles)
    return Omega_0

def initiate_spiral_rate(amount_dipoles):
    """
    Spiral rate of a dipole (remains fixed over simulation)
    Follows a gaussian distribution (mean = 3 rad/s, std = 1 rad/s)
    Taken from Brunk's "Chaff Aerodynamics" Table 2
    """
    Omega = sp.norm.rvs(loc=3, scale=1, size=amount_dipoles)
    return Omega

def initiate_spiral_radius(amount_dipoles):
    """
    Spiral radius (remains fixed over simulation)
    Follows a gaussian distribution (mean = 0.1524 m, std = 0.0508 m)
    Taken from Brunk's "Chaff Aerodynamics" Table 2
    """
    a = sp.norm.rvs(loc=0.1524, scale=0.0508, size=amount_dipoles)
    return a

def initial_angle(amount_dipoles):
    """
    Initial angle theta of dipole in air (remains fixed over simulation)
    Follows a gaussian distribution (mean = 1.22 rad, std = 0.175 rad)
    Taken from Brunk's "Chaff Aerodynamics" Table 2
    """
    theta = sp.norm.rvs(loc=1.22, scale=0.175, size=amount_dipoles)
    return theta

def initiate_pitch_angle():
    return 0

def initiate_angle_of_attack():
    return 0

def initiate_dipole_mass():
    return 0


def initial_position(cylinder_height, cylinder_radius, amount_dipoles):
    """
    Initial position of chaff pieces
    Uniformly distributed over the volume of the chaff container
    This neglects possible restrictions due to the container walls
    """
    r = sp.uniform.rvs(loc=0, scale=1, size=amount_dipoles)
    r = np.sqrt(r)*cylinder_radius
    angle = sp.uniform.rvs(loc=0, scale=2*np.pi, size=amount_dipoles)
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    z = sp.uniform.rvs(loc=0.5*cylinder_height, scale=0.5*cylinder_height, size=amount_dipoles)
    return np.array([x,y,z])