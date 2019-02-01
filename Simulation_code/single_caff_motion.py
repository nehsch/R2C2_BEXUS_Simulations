#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 13:18:29 2018

@author: nehir
""" 

import numpy as np
import scipy as sp # especially sp.stats
from matplotlib import pyplot as plt

# m := mass of the particle,
# rho := atmospheric density,
# Ap := surface area of the particle projected onto the plane normal to v,
# CD := drag coefficient,
# U := atmospheric velocity, the instantaneous sum of steady and turbulent components,
# v := particle velocity,
# SB = mgz := the body force,
# g := acceleration due to gravity.
# z_e := unit vector in the upward direction.

# gamma := pitch angle
# Omega := spiral rate
# a := spiral radius


def atmospheric_pressure_dry(altitude):
    p_0 = 101325    # sea level standard pressure [Pa]
    L = 0.0065      # temperature laps rate for dry air [K/m]
    T_0 = 288.15    # sea laval standard temperature [K]
    altitude_ESRANGE = 328 # [m]
    h = altitude + altitude_ESRANGE
    return p_0*(1.-L*h/T_0)

def air_density(altitude, T):
    p = atmospheric_pressure_dry(altitude)
    R_d = 287.058   # Specific gas constant for dry air, [J/(kg·K)]
    return p/(R_d*T)

def drag_coefficient(C_A, C_D, alpha):
    return C_A*np.cos(alpha)+C_N*np.sin(alpha)

def dipole_mass(length, width, height, dipole_density):
    return length*width*height*dipole_density

def projected_dipole_surface_area(length, width, alpha):
    return length*width*np.sin(alpha)

def epsylon(rho, Ap, C_D, m):
    return rho*Ap*C_D*0.5/m

#def horizontal_velocity_from_wind(u, v_0, delta_t):
#    Ap = projected_particle_surface_area()
#    return u-(u-v_0)/(1.+epsylon(rho, Ap, C_D, m)*delta_t*(u-v_0))
#
#def horizontal_displacement_from_wind(u, v_0, delta_t):
#    return P_0+u*delta_t-np.log(1.+epsylon*delta_t*(u-v_0))/epsylon
#
#def horizontal_displacement_gyration():
#    return [x_0+a*np.cos(Lambda+Omega*t), y_0+a*np.sin(Lambda+Omega*t)]

def dipole_velocity_along_path(m, g, gamma, rho, C_D, Ap):
    return np.sqrt(2*m*g*np.sin(gamma)/(rho*C_D*Ap))

def angle_of_attack(m, g, rho, v, Ap, C_D, theta):
    return np.arcsin(2*m*g*v[2]**2/(rho*Ap*C_D))**(1./3)-theta

def reynold_number(rho, v, length, mu):
    return rho*v*length/mu

def spiral_rate(v, length, theta, C_SM, C_NR):
    return 2*v*C_SM/(length*np.cos(theta)*C_NR)

def spiral_radius(v, Omega, gamma):
    return v*np.cos(gamma)/Omega

def vertical_velocity(u, v_0, delta_t, epsylon):
    c = np.sqrt(2*m*g/(rho*Ap*C_D))
    if (epsylon <= 0):
        return u[2]-c*np.tan((np.arctan2(u[2]-v_0[2])/c)-c*epsylon*delta_t)
    else:
        return u[2]-c*(u[2]-v_0[2]+c*np.tanh(c*epsylon*delta_t))/(c+(u[2]-v_0[2])*np.tanh(c*epsylon*delta_t))
        
def vertical_position(u, r_0, v_0, delta_t, epsylon):
    c = np.sqrt(2*m*g/(rho*Ap*C_D))
    if (epsylon <= 0):
        return r_0[2]+u[2]*-0.5*np.log(np.cos(c*epsylon*delta_t)+(u[2]-v_0[2])/c*np.sin(c*epsylon*delta_t))
    else:
        return r_0[2]+(u[2]+c)*delta_t-np.log(0.5/c*((u[2]+c-v_0[2])*np.exp(2*c*epsylon*delta_t)-(u[2]-c-v_0[2]))/epsylon)

def horizontal_position(u, r_0, v_0):
    x_0 = r_0[0]
    y_0 = r_0[1]
    v_0x = v_0[0]
    V_0y = v_0[1]
    u_x = u[0]
    u_y = u[1]
    return [x_0+u_x*delta_t*a*np.cos(Lambda+Omega*t)+np.log(1.+epsylon*delta_t*(u_x-v_0x))/epsylon,
            y_0+u_x*delta_t*a*np.sin(Lambda+Omega*t)+np.log(1.+epsylon*delta_t*(u_x-v_0y))/epsylon]
    
 def horizontal_velocity():
    x_0 = r_0[0]
    y_0 = r_0[1]
    v_0x = v_0[0]
    V_0y = v_0[1]
    u_x = u[0]
    u_y = u[1]
    return [u_x-(u_x-v_0x)/(1.+epsylon*delta_t*(u_x-v_0x)), u_y-(u_y-v_0y)/(1.+epsylon*delta_t*(u_y-v_0y))]



if __name__=='__main__':
    # randomly generate alpha and R_N
    # lookuptable for C_N and C_A
    # calculate C_D = drag_coefficient(C_A, C_D, alpha)
    # calculate Ap = projected_dipole_surface_area(length, width, alpha)
    # choose v_z=v*np.sin(gamma) in [1,3] m/s
    
    