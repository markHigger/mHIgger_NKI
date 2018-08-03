#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:53:39 2018

@author: markhigger
"""
import os
import EEG_Electrode_Map_Corrections as EMC
#Note: Paths are relative to the director of this file
input_dir = '../../EEG_Data/Unfixed_VHDR' #Specify input Path
output_dir = '../../EEG_Data/Fixed_VHDR/' #Specify output path
print( os.path)
for filename in os.listdir(input_dir):
    if filename.endswith(".vhdr") or filename.endswith(".py"): 
        print(os.path.join(input_dir, filename))
        print(os.path.join(output_dir, filename))
        EMC.CorrectFile(os.path.join(input_dir, filename),
                        os.path.join(output_dir, filename))
           