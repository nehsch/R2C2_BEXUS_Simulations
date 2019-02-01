#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 04:25:56 2019

@author: nehir
"""

import pandas as pd
import numpy as np


def initiate_lookup():
    rows = [375, 750, 1500, 3000, 6000] # corresponds to Reynolds Number
    columns = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180] # corrsponds to angle of attack [deg]
    
    CA_data = np.array([[5.5, 5.3, 4.8, 3.9, 2.8, 1.4, 0, -1.6, -2.8, -3.9, -4.8, -5.3, -5.5],
                        [2.6, 2.5, 2.3, 1.8, 1.3, 0.7, 0, -0.7, -1.3, -1.8, -2.3, -2.5, -2.6],
                        [1.3, 1.3, 1.1, 0.9, 0.7, 0.3, 0, -0.3, -0.7, -0.9, -1.1, -1.3, -1.3],
                        [0.7, 0.7, 0.6, 0.5, 0.4, 0.2, 0, -0.2, -0.4, -0.5, -0.6, -0.7, -0.7],
                        [0.4, 0.4, 0.3, 0.3, 0.2, 0.1, 0, -0.1, -0.2, -0.3, -0.3, -0.4, -0.4]])
    
    CN_data = np.array([[0, 2.0, 4.0, 5.6, 6.8, 7.6, 7.9, 7.6, 6.8, 5.6, 4.0, 2.0, 0 ],
                        [0, 1.1, 2.2, 3.1, 3.8, 4.3, 4.4, 4.3, 3.8, 3.1, 2.2, 1.1, 0],
                        [0, 0.8, 1.5, 2.1, 2.6, 2.9, 3.0, 2.9, 2.6, 2.1, 1.5, 0.8, 0],
                        [0, 0.6, 1.1, 1.6, 1.9, 2.1, 2.2, 2.1, 1.9, 1.6, 1.1, 0.6, 0],
                        [0, 0.4, 0.9, 1.2, 1.5, 1.6, 1.7, 1.6, 1.5, 1.2, 0.9, 0.4, 0]])
    
    CA_lookup_table = pd.DataFrame(CA_data, rows, columns) #lookup table for axial drag coefficient
    CN_lookup_table = pd.DataFrame(CN_data, rows, columns) #lookup table for normal drag coefficient
    
    return CA_lookup_table, CN_lookup_table


CA_lookup, CN_lookup = initiate_lookup()