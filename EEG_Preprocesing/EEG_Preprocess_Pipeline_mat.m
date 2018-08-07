function EEG_Preprocess_Pipeline_mat(filepath_input, varargin)
%This is the matlab preprocesssing script for automating EEG preprocessign
%It takes in a BrainVision EEG format and creates a set of eeglab formatted
%files of filtered eegs, by default creates only the final Mat file
%
%Function can be called with :
%EEG_Preprocess_pipeline_mat(filepath_input,'peram1', val, 'peram2', val)
%   perameters do not have to be in order
%Inputs:
%   filepath_input - This is the full filename of the input vhdr file
%   filepath_output - This is the full path of the output Directory:
%       by default, this is the input directory
%   Flags:
%       saveAll_Mat/Set - saves EEG after each stage in .mat or .set format
%       saveGA_Mat/Set - saves EEG after Gradient artifact is removed
%       saveBP_Mat/Set - saves EEG after bandpass filter
%       saveNotch_Mat/Set - saves EEG after notch filter
%       savePA_Mat/Set - saves EEG after Pulse artifact is removed
%Outputs:
%   saves eeg structs in eeglab format with either mat or set, where .mat
%       files can be in Matlab, and .set files can be used in eeglab
%
%Version:
%   Current - 0.1:
%       Prefunctional Build, has input parsing and program control flow

%% Parse function input
%Set input parser names and default values
p = inputParser;
p.KeepUnmatched = true;
p.addRequired('filepath_input')
[fileDir, fileName] = fileparts(filepath_input);
p.addParameter('filepath_output', fileDir)
p.addParameter('saveAll_Mat', 0);
p.addParameter('saveAll_Set', 0);
p.addParameter('saveGA_Mat', 0);
p.addParameter('saveGA_Set', 0);
p.addParameter('saveBP_Mat', 0);
p.addParameter('saveBP_Set', 0);
p.addParameter('saveNotch_Mat', 0);
p.addParameter('saveNotch_Set', 0);
p.addParameter('savePA_Mat', 0);
p.addParameter('savePA_Set', 0);
p.addParameter('saveResamp_Mat', 1);
p.addParameter('saveResamp_Set', 0);


p.parse(filepath_input, varargin{:});

filepath_input = p.Results.filepath_input;
filepath_output = p.Results.filepath_output;

%Set flags if user input has them set or if saveALL is enabled
saveAll_Mat = p.Results.saveAll_Mat;
saveAll_Set = p.Results.saveAll_Set;
saveGA_Mat = p.Results.saveGA_Mat || saveAll_Mat;
saveGA_Set = p.Results.saveGA_Set || saveAll_Set;
saveBP_Mat = p.Results.saveBP_Mat || saveAll_Mat;
saveBP_Set = p.Results.saveBP_Set || saveAll_Set;
saveNotch_Mat = p.Results.saveNotch_Mat || saveAll_Mat;
saveNotch_Set = p.Results.saveNotch_Set || saveAll_Set;
savePA_Mat = p.Results.savePA_Mat || saveAll_Mat;
savePA_Set = p.Results.savePA_Set || saveAll_Set;
saveResamp_Mat = p.Results.saveResamp_Mat || saveAll_Mat;
saveResamp_Set = p.Results.saveResamp_Set || saveAll_Set;

%% Determain control flow of pipelines

%TODO: Deteramine and set filenames 
%filenames are [outputDir][inputfile(-extension)][Last Process][extension]
%   eg: usr/documents/EEG_data/despicableme-02_Bandpass.set
fileName_gradient = fullfile(filepath_output,[fileName,'_01_gradient']);
fileName_bandpass = fullfile(filepath_output,[fileName,'_02_bandpass']);
fileName_notch = fullfile(filepath_output,[fileName,'_03_notch']);
fileName_bcg = fullfile(filepath_output,[fileName,'_04_bcg']);
fileName_resample = fullfile(filepath_output,[fileName,'_05_resample']);

%TODO: Check if filenames exist in output path
GAExist = (exist([fileName_gradient, '.mat'],'file'));
BPExist = (exist([fileName_bandpass, '.mat'],'file'));
NotchExist = (exist([fileName_notch, '.mat'],'file'));
PAExist = (exist([fileName_bcg '.mat'],'file'));
resampExist = (exist([fileName_resample, '.mat'],'file'));

%Set Control flags - a step should not be performed if the proceding
%   files exist of previos process completion 
resample = ~resampExist;
removePA = ~PAExist && resample;
removeNotch = ~NotchExist && removePA;
removeBP = ~BPExist && removeNotch;
removeGA = ~GAExist && removeBP;


%% Remove GA from EEG
if removeGA
    fprintf('removing fMRI gradient artifact \n')
    %load in raw eeg to eeglab struct
    [fileDir_input, fileName_input] = fileparts(filepath_input);
    [EEG_Raw, ~] = pop_loadbv(fileDir_input,[fileName_input,'.vhdr']);
    %perform gradient removal
    EEG_GA = EEG_GA_Removal_Matlab(EEG_Raw);
    %TODO: save output
    if (saveGA_Mat)
        fprintf('saving GA removed EEG as mat file \n');
        EEG = EEG_GA;
        save([fileName_gradient,'.mat'],'EEG');
        clear EEG
    end
    if (saveGA_Set)
        fprintf('saving GA removed EEG as Set file \n');
        EEG = EEG_GA;
        save([fileName_gradient,'.set'],'EEG');
        clear EEG
    end
else
    fprintf('File exists with GA removed \n')
end


%% remove Bandpass from EEG
if (removeNotch)
    %if previos filtering was skipped load EEG_BA from file 
    %   else use EEG_GA from Gradient removal step
    if ~removeGA
        fileMat = load([fileName_gradient,'.mat']);
        EEG_GA = fileMat.EEG;
        clear('fileMat');
    end
    fprintf('applying bandpass filter\n')

    %perform bandpassfilter
    %set low and high end of wanted frequencies
    %OPTIONAL TODO: specify freqs & filt info from function call
    F_low = 0.5;
    F_high = 70;
    EEG_BP = EEG_Bandpass_Matlab(EEG_GA, F_low, F_high);
    %TODO: save output
    if (saveBP_Mat)
        fprintf('saving Bandpassfilterd eeg as mat file \n');
        EEG = EEG_BP;
        save([fileName_bandpass,'.mat'],'EEG_BP');
        clear EEG
    end
    if (saveBP_Set)
        fprintf('saving Bandpassfilterd eeg as set file \n');
        EEG = EEG_BP;
        save([fileName_bandpass,'.set'],'EEG_BP');
        clear EEG
    end
else
    fprintf('File with bandpass filter already exists');
end
%% filter out Notch at 60 hz
if (removeNotch)
    %if previos filtering was skipped load EEG_GA from file 
    %   else use EEG_GA from Gradient removal step
    if ~removeBP
        fileMat = load([fileName_bandpass,'.mat']);
        EEG_BP = fileMat.EEG;
        clear('fileMat');
    end
    fprintf('applying Notch filter\n')

    %perform Notch
    %set notch cutoff
    %OPTIONAL TODO: specify freqs & filt info from function call
    F_Notch = 60;
    EEG_Notch = EEG_Notch_Matlab(EEG_BP, F_Notch);
    %TODO: save output
    if (saveBP_Mat)
        fprintf('saving Notch filterd eeg as mat file \n');
        EEG = EEG_Notch;
        save([fileName_notch,'.mat'],'EEG');
        clear EEG
    end
    if (saveBP_Set)
        fprintf('saving Notch filterd eeg as set file \n');
        EEG = EEG_Notch;
        save([fileName_notch,'.set'],'EEG');
        clear EEG
    end
else
    fprintf('File with bandpass filter already exists');
end


