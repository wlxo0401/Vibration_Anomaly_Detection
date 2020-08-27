import numpy as np
import math
import matplotlib as plt

def acc_int(data, fs):
    df = fs / len(data)
    data_fft = np.fft.fft(data)/len(data)
    data_fft_mag = np.power(np.multiply(data_fft, np.conj(data_fft)), 0.5)

    faxis = np.arange(0, (fs-1/len(data)), step=df)
    
    data_fft_mag = data_fft_mag[0:(math.ceil(len(data)/2))] * 2
    faxis = faxis[0:(math.ceil(len(data)/2))]
    
    rtn = np.zeros((math.floor(fs/2),1))
    for n1 in np.arange(5, math.floor(fs/2-1)):
        tmp = 0
        for n2 in np.arange(math.ceil((n1-0.5)/df+1), math.ceil((n1+0.5)/df)):
            tmp = tmp + np.power((data_fft_mag[n2]/math.sqrt(2) / (2*math.pi*faxis[n2])), 2)
        rtn[n1, 0] = math.sqrt(tmp)
    return rtn
