import pandas as pd
#import fileinput
#Define corisponding incorrect/correct channels
def CorrectFile(input_file, output_file):
    ChannelCorrections = \
		pd.DataFrame({'ChannelNumber' : [20, 29, 30, 
                                           31, 32, 61, 
                                           62, 63, 64],
                       'ChannelName' : ['IO', 'FT9', 'FT10', 
                                        'TP9', 'TP10', 'Fpz', 
                                        'CPz', 'POz', 'Oz'], 
				 	'Correction' : ['Oz', 'TP9', 'TP10', 
                                          'POz', 'ECG', 'FT9',
                                          'FT10', 'FPz', 'CPz'],
                       'Coors' : [[1, 90, -90], [1, -113, 18], [1, 113, -18], 
                                 [1, 67, -90], [0, 130, 74], [1, -113, -18], 
                                 [1, 113, 18], [1, 90, 90], [1, 22, -90]]})

    ChannelCorrections.set_index('ChannelNumber', inplace=True)




    # Read in the file
    f = open(input_file,'r')
    fStr = f.read()
    f.close()

    #############
    #find Channels with incorrect names in [Channel infos] section 
    #and replace with correct names
    for item in fStr.split("\n"):
        for Chans in ChannelCorrections.index:
            ChanStr = ('Ch%d' % Chans)
            #Format for Channel info - 'Ch[chanNum]=ChanName,,0.5,uV'
            if (ChanStr in item) and not ((item[len(ChanStr) + 1] == '1') or 
                (item[len(ChanStr) + 1] == '0')):
                #Insert new coordinates based off the channel and pandas chart
                newLine=('%s%s%s%s' % (item[0:5], 
                                         ChannelCorrections.loc[Chans]['Correction'],
                                         item[len(ChannelCorrections.loc[Chans]['ChannelName']) + 5:-1],
                                         item[-1]))
                fStr = fStr.replace(item, newLine)
   
    #############
    #correct  Channels with incorrect names  & sereis res in [Amplifier] section
    #NOTE: This is done seperately from the [Channel infos]  or [coordinates] 
    #section because the name formatting is different 
    for item in fStr.split("\n"):
        for Chans in ChannelCorrections.index:
            ChanStr = ('%d ' % Chans)
            #Format for AMP - 'Chan#[spc]ChanName[spc]'... '[spc]seriesRes[spc]' 
            #   where all incorrect series res are ' 0 ' and [spc] is a variable 
            #   amount of space
            if (ChanStr in item) and not ((item[len(ChanStr) + 2] == '=') or \
                (item[len(ChanStr) + 1] == '=')):
                
                #Replace Channel names
                newLine = item.replace(ChannelCorrections.loc[Chans]['ChannelName'],
                                         ChannelCorrections.loc[Chans]['Correction'])
                fStr = fStr.replace(item, newLine)
                #replace channel series resistance 
                #NOTE: all sereis res = 10kOhm except ECG = 20kOhm
                if ChannelCorrections.loc[Chans]['Correction'] == 'ECG':
                    newLine = item.replace(' 0 ', ' 20')
                else:
                    newLine = item.replace(' 0 ', ' 10')
                fStr = fStr.replace(item, newLine)
                
    #############
    #switching coordinates to correct coordinates in [coordinates] section
    #Search line-by-line checking if the cooordinate strings match the Channels that need to be corrected
    for item in fStr.split("\n"):
        for Chans in ChannelCorrections.index:
            ChanStr1 = ('Ch%d=1' % Chans)
            ChanStr2 = ('Ch%d=0' % Chans)
            #Format for [coordinates] - 'Ch[ChanNum]=[Coor]'
            if (ChanStr1 in item) or (ChanStr2 in item):
                #Insert new coordinates based off the channel and pandas chart
                newLine=('%s%d,%d,%d' % (item[0:5], 
                                         ChannelCorrections.loc[Chans, 'Coors'][0], 
                                         ChannelCorrections.loc[Chans, 'Coors'][1], 
                                         ChannelCorrections.loc[Chans, 'Coors'][2]))
                fStr = fStr.replace(item, newLine)
    ############
    
    #write to new file
    f = open(output_file, 'w+')
    f.write(fStr)
    f.close()