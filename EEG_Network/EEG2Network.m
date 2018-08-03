EEG = qbin_EEG_fMRI_preprocScript_v5_OctaveComp('/Users/markhigger/Documents/MATLAB/EEG_20180713_Test_03_Inscapes02.eeg', '/Users/markhigger/Documents/MATLAB/');

EEG_data = EEG.data;

numChans = size(EEG_data, 1);
numData = size(EEG_data, 2);
F_srate = EEG.srate; % Sampling rate
order = 2;


%Flags for superMat
AllFreqFlag = 0;
AlphaFlag = 1; %calculate Cor Mat for Alpha Band
BetaFlag = 1; %calculate Cor Mat for Beta Band
GammaFlag = 1; %calculate Cor Mat for Gamma Band
makeImage = 1;
plotSpectrums = 1;

%Freq bands in Hz
AlphaFreq = [8, 12];
BetaFreq = [12, 30];
GammaFreq = [30, 100];

if AlphaFlag
    %filter Alpha band from all eeg data
    AlphaData = filterBands(EEG, AlphaFreq, 4);
    %make correlation matrix betwenn channels for alpha band
    AlphaMat = makeCorMat(AlphaData, numChans);
    if makeImage
        figure
        imagesc(AlphaMat);
    end
end
if BetaFlag
    BetaData = filterBands(EEG, BetaFreq, 8);
    BetaMat = makeCorMat(BetaData, numChans);
    if makeImage
        figure
        imagesc(BetaMat);
    end
end
if GammaFlag
    GammaData = filterBands(EEG, GammaFreq, 8);
    GammaMat = makeCorMat(GammaData, numChans);
    if makeImage
        figure
        imagesc(GammaMat);
    end
end

if plotSpectrums == 1
    %Set to show all spectrums of each band
    figure
    subplot(2,2,1)
    hold
    subplot(2,2,2)
    hold
    subplot(2,2,3)
    hold
    for chans = 1:64
        %take fft of band
        Alpha_mags = abs(fft(AlphaData(chans,:)));
        Beta_mags = abs(fft(BetaData(chans,:)));
        Gamma_mags = abs(fft(GammaData(chans,:)));
        N = length(EEG_data);
        bin_vals = [0 : N-1];
        fax_Hz = bin_vals*F_srate/N;
        N_2 = ceil(N/2);
        
        %plot magnitude of each band
        subplot(2,2,1)
        plot(fax_Hz(1:N_2), 10*log10(Alpha_mags(1:N_2)))
        subplot(2,2,2)
        plot(fax_Hz(1:N_2), 10*log10(Beta_mags(1:N_2)))
        subplot(2,2,3)
        plot(fax_Hz(1:N_2), 10*log10(Gamma_mags(1:N_2)))
    end
end

function filtData = filterBands(EEG, freqs, order)
    data = EEG.data;    
    numChans = size(data, 1);
    numData = size(data, 2);
    F_srate = EEG.srate; % Sampling rate
    
    % Bandpass frequency range cutoff based on sampling rate
    Wn = [freqs(1) freqs(2)]*2/F_srate;
    % Filter order
    N = order;
        
    % Butterworth bandpass filter
    [a,b] = butter(N,Wn); %bandpass filtering

    filtData = zeros(numChans,numData);
    for ii = 1:numChans
        % Bandpass filter signal with Butterworth filter
        filtData(ii,:) = filtfilt(a,b,double(data(ii,:)));
    end
    
end

function CorMat = makeCorMat(data, numChans)
    %
    CorMat = zeros(numChans);
    for chanYidx = 1:numChans
        for chanXidx = chanYidx:numChans
            if chanXidx ~= chanYidx
                corr = corr2(data(chanXidx, :), data(chanYidx, :));
                if abs(corr) >= 0
                    CorMat(chanXidx, chanYidx) = corr;
                end
            end
        end
    end
    CorMat = CorMat + CorMat';
end

    

