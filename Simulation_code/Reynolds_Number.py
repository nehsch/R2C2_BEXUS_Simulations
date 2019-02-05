#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:28:52 2019

@author: nehir
"""

import numpy as np
import scipy.stats as sp 

import lookup_table

"""###################
This is a way of creating matching pairs of Reynold numbers R_N and angles of attack alpha. 
Both sets are randomly created and then compared whather they fit well enough together for a real dipole.

THE RANGES OF THE DISTRIBUTION (ESPECIALLY FOR R_N) MIGHT BE WRONG ***CHECK***!
###################"""

def reynold_number_computed(rho, v, length, mu):
    """
    input: density of air, vertical velocity, value of length, kinematic viscosity of air
    output: calculated value of R_N
    """
    return rho*v*length/mu

def angle_of_attack_computed(m, g, v, rho, Ap, C_D):
    """
    input: mass, gravitational acceleration, vertical velocity, density of air, projected area, drag coefficient
    output: Calculated value of alpha
    """
    return np.arcsin((2.*m*g*v**2/(rho*Ap*C_D))**(1./3))

def create_reynolds_number(nr):
    """
    Creates a set of reynold numbers. 
    Right now the chosen distribution is a uniform distribution between 1 and 100.
    This is based on the Raynold numbers for foil chaff in Brunk's "Chaff Aerodynamics"
    """
    return sp.uniform.rvs(loc=1., scale=100., size=nr)

def create_angle_of_attack(nr):
    """
    Creates a set of angles of attack according to a normal distribution between 0 and pi.
    """
    return sp.uniform.rvs(loc=0, scale=np.pi, size=nr)

def check_match(reynolds_number, angle_of_attack):
    return 0
    

def run(number):
    v_z_ss = 0.9144 # [m/s] =  3 ft/s vertical steady state velocity (highest usually reached according to Brunk's "Chaff Aerodynamics". Might need changing.)
    
    # Ransomly generate sets of Reynolds Numbers and angles of attack.
    R_N_created = create_reynolds_number(number)
    alpha_created = create_angle_of_attack(number)
    
    # Use the generated R_N and alpha to determine the drag coefficient (using lookup thables from lookup_table.py)
    CA_lookup, CN_lookup = lookup_table.initiate_lookup()
    C_A = CA_lookup.get_value(R_N_created, alpha_created)
    C_N = CN_lookup.get_value(R_N_created, alpha_created)
    C_D = C_A*np.cos(alpha_created) + C_N*np.sin(alpha_created)
    
    # Use the known (from measurements) vertical steady state velocity and the determined drag coefficient
    # To calculate the Reynolds Number and the angle of attack.
    R_N_calculated = reynold_number_computed(rho, v_z_ss, length, mu)
    alpha_calculated = angle_of_attack_computed(m, g, v_z_ss, rho, Ap, C_D)
    

    
    
    
    