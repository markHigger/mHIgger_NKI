#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:51:42 2018

@author: markhigger
"""
import PreProcpy_Wrap as Wrap
import os.path

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

#check if files exist to compute what processing needs to be done
FileExists_set = os.path.isfile(fileName_set) 
FileExists_gradient = os.path.isfile(fileName_gradient)
FileExists_bandpass = os.path.isfile(fileName_bandpass)
FileExists_notch = os.path.isfile(fileName_notch)
FileExists_bcg = os.path.isfile(fileName_bcg)
#Check which processing needs to be done, skip Processing if a file exits where
#   Processing or any Processing after exists
skip_bcg = FileExists_bcg
skip_notch = FileExists_notch or skip_bcg
skip_bandpass = FileExists_bandpass or skip_notch
skip_gradient = FileExists_gradient or skip_bandpass
skip_set = FileExists_set or skip_gradient


#initialize matlab runtime compiler with preprocessor functions
Funs = Wrap.init()

#convert brainvision data to 
if skip_set:
    print('set file already exists, skiping creation of set file')
else:
    Wrap.BV2Set(Funs, '~/Desktop/EEG_data/EEG_20180713_Test_02_ThePresent.eeg')

#Run EEG through GA removal
if skip_gradient:
    print('gradient artifact already removed')
else:
    Wrap.GA_Removal(Funs, fileName_set, fileName_gradient)

#Run EEG through Bandpass filter - uses forward-backward butterworth iir bandpass
if skip_bandpass:
    print('bandpass filter already appled')
else:
    Flow = 0.5 #low cuttoff at 0.5 Hz
    Fhigh = 70 #high cutoff at 70 Hz
    N = 2 #use second order filter 
    Wrap.Bandpass_Mat(Funs, fileName_gradient, fileName_bandpass, Flow, Fhigh, N)

#Run EEG through Notch filter - uses forward-backward butterworth iir bandstop
if skip_notch:
    print('Notch filter already applied')
else:
    Fn = 60 #Notch filter at 60Hz
    Fw = 4 #Notch width of 4Hz
    N = 2 #use second order bandstop
    Wrap.Notch_Mat(Funs, fileName_bandpass, fileName_notch, Fn, Fw, N)

#Run EEG through PA removal 
if skip_bcg:
    print('bcg already removed')
else:
    Wrap.PA_Removal(Funs, fileName_notch, fileName_bcg)

#terminate matlab runtime compiler
Wrap.term(Funs)




