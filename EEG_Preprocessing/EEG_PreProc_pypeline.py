#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 10:42:14 2018

@author: markhigger
"""

import mne
from mne.preprocessing import compute_proj_ecg
filepath = '../../EEG_Data/EEG_Raw/EEG_20180713_Test_03_Inscapes02.vhdr'
raw = mne.io.read_raw_brainvision(filepath)

projs, events = compute_proj_ecg(raw, n_grad=1, n_mag=1, n_eeg=0, average=True, ch_name='ECG')
print(projs)

ecg_projs = projs[-2:]
mne.viz.plot_projs_topomap(ecg_projs)
