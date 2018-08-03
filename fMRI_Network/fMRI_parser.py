#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:43:42 2018

@author: markhigger
"""
import numpy as np
def parse2mat(input_file):
    f = open(input_file,'r')
    fStr = f.read()
    f.close()
    
    
    #get dimensions of region to initialize empty matrix 
    numRegions = 0
    numSlices = 0
    #Each line in the text that does not precede with # represents a time slice
    for item in fStr.splitlines():
        if '#' not in item:
            if numRegions == 0:
                numRegions = len(item.split())
            numSlices += 1
    
    #initialize empty mat in [R1S1, R2S1 ...; R1S2, R2S2; ...] 
    #   where Rn = ROI #n & S = Slice #n
    dataMat = np.zeros((numSlices, numRegions))
    
    
    #Each line in the text that does not precede with # represents a time slice
    Sliceidx = 0
    for item in fStr.splitlines():
        if '#' not in item:
            dataMat[Sliceidx, :] = item.split()
            Sliceidx += 1
    
        
parse2mat('../../fMRI_Data/roi_stats.csv')