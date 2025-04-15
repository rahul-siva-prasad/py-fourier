import math
import numpy as np
import matplotlib.pyplot as plt

from .sigClass import Signal
from .sinLookup import SIN_ONE_DEG_LOOKUP

def f_plotGraph(*data,title=""):
    for pts in data:
        pltPoint = np.array(pts)
        plt.plot(pltPoint)
    plt.title(title)
    plt.ylabel("Amplitude")
    plt.xlabel("Sample points")
    plt.grid()
    plt.show()

def f_getSinValue(degree):
    if degree >= 0:
        floorVal = math.floor(degree)
    else:
        floorVal = math.ceil(degree)
    '''
    decimalPart = (degree - floorVal)*10
    decVal = int(round(decimalPart / 0.025)/10)'
    '''
    while floorVal < 0:
        floorVal += 360
        
    while floorVal > 360:
        floorVal -= 360
    

    if floorVal >= 0 and floorVal <=90:
        return SIN_ONE_DEG_LOOKUP[floorVal]
    elif floorVal > 90 and floorVal <= 180:
        return SIN_ONE_DEG_LOOKUP[180 - floorVal]
    elif floorVal > 180 and floorVal <= 270:
        return -1 * SIN_ONE_DEG_LOOKUP[floorVal - 180]
    elif floorVal > 270 and floorVal <= 360:
        return -1 * SIN_ONE_DEG_LOOKUP[360 - floorVal]
    else:
        assert(0)
        return math.nan

def f_buildSinWave(amp=1, freq=1, phase=0):
    sinWave = []
    pts = tuple(i + phase for i in range(0,360 * freq +1,freq))
    for deg in pts:
        sinWave.append(amp * f_getSinValue(deg))
    return Signal(sinWave)

def f_buildCosWave(amp=1, freq=1, phase=0):
    return f_buildSinWave(amp,freq,phase+90)

def f_buildTanWave(amp=1, freq=1, phase=0):
    sinVal = f_buildSinWave(amp,freq,phase)
    cosVal = f_buildCosWave(amp,freq,phase)
    tanVal =[]
    for idx in range(len(sinVal)):
        if cosVal[idx] == 0:
            tanVal.append(math.nan)
        else:
            tanVal.append(sinVal[idx]/cosVal[idx])
    return Signal(tanVal)

def f_buildDcShift(amp=1):
    dcVal = [amp for idx in range(360 +1)]
    return Signal(dcVal)
