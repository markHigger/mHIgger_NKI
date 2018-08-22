#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:21:52 2018

@author: mhigger
"""
import PreProcPkg_v11

def init():
    Funs = PreProcPkg_v11.initialize()
    print('PreProc initialized \n')
    return Funs
def BV2Set(Funs, fileFull_input=None, fileFull_output=None):
    Funs.BV2Set_Wrap('~/Desktop/EEG_data/EEG_20180713_Test_02_ThePresent.eeg')
def term(Funs):   
    Funs.terminate()
