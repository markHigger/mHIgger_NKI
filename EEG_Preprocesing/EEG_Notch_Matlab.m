function EEG_filtered = EEG_Notch_Matlab(EEG_input, Fn)
%Applys Notch filter on eeglab EEG struct to remove radient electrical
%noise
%Input:
%   EEG_input [eeglab EEG struct] - EEG_data before bandpass filter
%   Fn [float] - unwanted frequency of notch filter

EEG_data = double(EEG_input.data);
% Bandpass frequency range cutoff based on sampling rate
Fn_lo = Fn - 2;
Fn_hi = Fn + 2;
Wnotch = [Fn_lo Fn_hi]*2/F_srate;

%Design Low order butterworth Filter 
N = 2;
[a,b]=butter(N,Wnotch,'stop');

%Filter data
filterData = zeros(nChannels,nSamples);
for chanIdx = 1:nChannels
    % Notch filter 60Hz noise with notch filter
    filterData(chanIdx,:) = filtfilt(a,b,EEG_data(chanIdx,:));
end
EEG_filtered = EEG_input;
EEG_filtered.data = filterData;