function Complete = GA_Removal_Wrap(input_Set_file, fileDir_output)
%Takes in eeglab set file with EEG struct and Removes EEG Gradient Artifact 
%   induced by MRI Scanner using the fmrib eeglab plugin pop_fmrib_fastr 
%   This should be the first step in preprocessing, as the GA removal works
%   better before other filtering, and other filtering tequniques may
%   require clean signals
%Input: 
%   input_Set_file: full path for eeglab struct file that includes the following:
%       EEG - [eeglab EEG struct] EEG without Gradient artifact removed
%   output_path: full path for directory which the following file is saved:
%       output_file - [eeglab set file] set file saved containing EEG struct
%                       with same name as input_Set_file with new Dir
%   
%Output:
%   output_EEG
%   EEG_filtered - [eeglab EEG format] EEG with GA removed

Complete = 0; %return 0 on unsucessful run
%Check for valid arguments
if nargin < 1
    error('Not enough arguments, inout file needed')
end
if nargin > 2
    error('Too many input arguments')
end

%find file directory and name of input file for filename calculations
[fileDir_input, fileName_input] = fileparts(input_Set_file);

%set output directory to input directory if not specified bby user
if nargin == 1
    fileDir_output = fileDir_input;
end

%calculate output filename as:
%   <fileDir_output>/<fileName_input>_gradient.set
fileName_output = fullfile(fileDir_output, ...
                            [fileName_input, '_gradient', '.set']);

%load in EEG 
fileMat = load('-mat', input_Set_file);
EEG_input = fileMat.EEG;
clear('fileMat');

%convert EEG data to double (unknown reason from legacy code)
EEG_input.data = double(EEG_input.data);

%Uses Gradient Artifact removal from Legacy Code with default func perams
EEG = pop_fmrib_fastr (EEG_input, [], 10, 30, 'R128', 0, 0, 0, 0, 0, 0, [], 0);

save(fileName_output,'EEG');

Complete = 1; %return 1 on sucessful run
