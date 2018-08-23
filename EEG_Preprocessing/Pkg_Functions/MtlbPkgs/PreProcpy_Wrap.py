#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:21:52 2018

@author: mhigger
"""
import PreProcPkg_v11

def init():
    Funs = PreProcPkg_v11.initialize()
    
    print('Matlab Runtime compiler initialized \n')
    return Funs
def BV2Set(Funs, fileFull_input):
    #Converts Brainvision format to eeglab Set file to be used for other MATLAB
    #   Processing
    #inputs:
    #   Funs - initialized matlab runtime compiler package (run Funs = init() first)
    #   fileFull_input - full path and file of .eeg or .vhdr file
    #Outputs:
    #   output set File - eeglab set file which contains raw eeg struct, has 
    #                       same name as input file with new extension
    #NOTE: requires .eeg, .vhdr and .vmrk to all have the same name in the 
    #       same directory
    
    #MATLAB Funcion description...
    #function complete = BV2Set_Wrap(inputFile)
    # Converts raw Brainvision vhdr header and EEG data files and converts them
    # into eeglab Set files which the filters 
    # *NOTE* saves new Set File in same directory as input direcotry since GA
    #   removal requires the Set file as well as the vmrk file with TR times
    # Input:
    #   inputFile - full file path and name of either .eeg or .vhdr file
    #       NOTE: .eeg, .vhdr and .vmrk must be in the same directory
    # Output:
    #   complete - returns 1 on function completion
    #   outputFile - eeglab set file which contains raw eeg struct
    
    
    Funs.BV2Set_Wrap(fileFull_input)
    print('BV file saved as Set file')
    
def GA_Removal(Funs, fileFull_input, fileFull_output = None):
    #Set default output filename to <inputfile> - <extension> + '_gradient.set'
    if fileFull_output == None:
        fileFull_output = \
            '.'.join(fileFull_input.split('.')[0:-1]) + '_gradient.set'
        
    Funs.GA_Removal_Wrap(fileFull_input, fileFull_output)
    print('GA Removed')
    
def Bandpass_Mat(Funs, fileFull_input, fileFull_output = None, 
                 Flow = 0.5, Fhigh = 70, order = 2):
    #Set default output filename to <inputfile> - <extension> + '_bandpass.set'
    if fileFull_output == None:
        fileFull_output = \
            '.'.join(fileFull_input.split('.')[0:-1]) + '_bandpass.set'
            
    Funs.Bandpass_Mat_Wrap(fileFull_input, fileFull_output, \
                           float(Flow), float(Fhigh), order)
    
def Notch_Mat(Funs, fileFull_input, fileFull_output = None,
              Fn = 60, Fw = 4, order = 2):
    #Set default output filename to <inputfile> - <extension> + '_notch.set'
    if fileFull_output == None:
        fileFull_output = \
            '.'.join(fileFull_input.split('.')[0:-1]) + '_notch.set'
            
    Funs.Notch_Mat_Wrap(fileFull_input, fileFull_output, \
                        float(Fn), float(Fw), order)
    
def PA_Removal(Funs, fileFull_input, fileFull_output = None):
    #Set default output filename to <inputfile> - <extension> + '_bcg.set'
    if fileFull_output == None:
        fileFull_output = \
            '.'.join(fileFull_input.split('.')[0:-1]) + '_bcg.set'
            
    Funs.PA_Removal_Wrap(fileFull_input, fileFull_output)
    
def term(Funs):   
    Funs.terminate()
    print('Matlab runtime compiler terminated')

    
