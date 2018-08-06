#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:43:42 2018

@author: markhigger
"""
import numpy as np
import matplotlib.pyplot as plt
import math


#take in tabed csv of ROIS and turn them into a readable numpy array
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
    return dataMat

#Take in Numpy Array of ROI timeslices and return coorilation matrix
def createCorMat(inputMat):
    [numSlices, numROI] = inputMat.shape
    dataMat = np.zeros((numROI, numROI))
    for xROIidx in range(numROI):
        for yROIidx in range(xROIidx, numROI):
            if (inputMat[:, xROIidx] != inputMat[:, yROIidx]).all():
                dataMat[xROIidx, yROIidx] =  corr2(inputMat[:, xROIidx], inputMat[:, yROIidx])
    dataMat += dataMat.transpose()
    return dataMat
#used to calculate corraltion
def mean2(x):
    y = np.sum(x) / np.size(x);
    return y

#used to create corelation matrix
def corr2(a,b):
    a = a - mean2(a)
    b = b - mean2(b)

    r = (a*b).sum() / math.sqrt((a*a).sum() * (b*b).sum());
    return r

matrix = parse2mat('../../fMRI_Data/roi_stats.csv')
dataMat = createCorMat(matrix)
plt.imshow(dataMat)
    
