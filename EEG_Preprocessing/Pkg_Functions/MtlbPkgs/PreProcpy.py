#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:51:42 2018

@author: markhigger
"""
import PreProcpy_Wrap as Wrap

#get base file names and directories
fileDir_input = '~/Desktop/EEG_data/'
fileDir_output = fileDir_input
fileName_base = 'EEG_20180713_Test_02_ThePresent'

#calculate file names in input directory 
fileName_raw = fileDir_input + fileName_base + '.eeg'
fileName_set = fileDir_input + fileName_base + '.set'

#calculate file names in output file directory
fileName_gradient = fileDir_output + fileName_base + '_gradient.set'
fileName_bandpass = fileDir_output + fileName_base + '_bandpass.set'
fileName_notch = fileDir_output + fileName_base + '_notch.set'
fileName_bcg = fileDir_output + fileName_base + '_bcg.set'

#initialize matlab runtime compiler with preprocessor functions
Funs = Wrap.init()

#convert brainvision data to 
Wrap.BV2Set(Funs, '~/Desktop/EEG_data/EEG_20180713_Test_02_ThePresent.eeg')

#Run EEG through GA removal
Wrap.GA_Removal(Funs, fileName_set, fileName_gradient)

#Run EEG through Bandpass filter - uses forward-backward butterworth iir bandpass
Flow = 0.5 #low cuttoff at 0.5 Hz
Fhigh = 70 #high cutoff at 70 Hz
N = 2 #use second order filter 
Wrap.Bandpass_Mat(Funs, fileName_gradient, fileName_bandpass, Flow, Fhigh, N)

#Run EEG through Notch filter - uses forward-backward butterworth iir bandstop
Fn = 60 #Notch filter at 60Hz
Fw = 4 #Notch width of 4Hz
N = 2 #use second order bandstop
Wrap.Notch_Mat(Funs, fileName_bandpass, fileName_notch, Fn, Fw, N)

#Run EEG through PA removal 
Wrap.PA_Removal(Funs, fileName_notch, fileName_bcg)




