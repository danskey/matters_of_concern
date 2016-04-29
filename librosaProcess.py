from __future__ import print_function
import librosa
import numpy as np

##############   RMS Analysis   ##############

# Rememberer --- RMS section

def libroRMS(filepath, kRatio):
    y, sr = librosa.load(filepath) # Load the waveform as y, sr is sample rate
    clipLength = librosa.get_duration(y=y, sr=sr)
    kValue = int(clipLength/kRatio +1) #sets up relative ratio of samples

    ### get the RMS of the audio sample ###
    data = librosa.feature.rmse(y=y, hop_length=2048)
    boundaries = librosa.segment.agglomerative(data, k=kValue) # Agglomeration
    boundary_times = librosa.frames_to_time(boundaries, hop_length=2048) # ~.1s
    intervals = np.hstack([boundary_times[:-1, np.newaxis], boundary_times[1:, np.newaxis]])
    get_rms = librosa.feature.sync(data, boundaries, aggregate=np.max)

    nkValue = kValue-1 #because, for some reason, the intervals above leave out the last one
    fixedN = np.delete(get_rms, nkValue, axis=1)
    npsTurn = np.concatenate((intervals, fixedN.T), axis=1)

    #transform from np array to regular list
    flatnps = npsTurn.tolist()
    slice_value = int(kValue//3)
    rmsOut1 = sorted(flatnps, key = lambda x: int(x[2]), reverse=True)
    #rmsOut2 = slice(rmsOut1[0: slice_value])
    rmsOut2 = rmsOut1[0 : slice_value]
    rmsOut3 = sorted(rmsOut2, key = lambda x: int(x[0]))

    return rmsOut3

# Combiner --- RMS section

def comboRMS(filepath, kRatio):
    y, sr = librosa.load(filepath) # Load the waveform as y, sr is sample rate
    clipLength = librosa.get_duration(y=y, sr=sr)
    kValue = int(clipLength/kRatio +1) #sets up relative ratio of samples

    ### get the RMS of the audio sample ###
    data = librosa.feature.rmse(y=y, hop_length=2048)
    boundaries = librosa.segment.agglomerative(data, k=kValue) # Agglomeration
    boundary_times = librosa.frames_to_time(boundaries, hop_length=2048) # ~.1s
    intervals = np.hstack([boundary_times[:-1, np.newaxis], boundary_times[1:, np.newaxis]])
    get_rms = librosa.feature.sync(data, boundaries, aggregate=np.max)

    nkValue = kValue-1 #because, for some reason, the intervals above leave out the last one
    fixedN = np.delete(get_rms, nkValue, axis=1)
    npsTurn = np.concatenate((intervals, fixedN.T), axis=1)

    #transform from np array to regular list
    flatnps = npsTurn.tolist()
    slice_value = kValue//1.5
    rmsOut1 = sorted(flatnps, key = lambda x: int(x[2]), reverse=True)
    rmsOut2 = slice(rmsOut1[0: slice_value])
    rmsOut3 = sorted(rmsOut2, key = lambda x: int(x[0]))

    return rmsOut3



# def filterbyvalue(seq, value):
#    for el in seq:
#        if el.attribute==value: yield el
#
# mylist = filterbyvalue(AccesLog[1], "jpg")
