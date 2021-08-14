import sys
sys.path.append(".")

import pandas as pd
import numpy as np
from scipy.signal import hilbert

from constants import *

def moving_avg(signal, window_size):
    x = np.cumsum(signal, dtype=float)
    x[window_size:] = x[window_size:] - x[:-window_size]
    return x[window_size-1:]/window_size


def normalize(signal):
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal))


def procesing_using_hilbert(signal, window_size):
    signal = np.sum(signal**2, axis=1)
    signal = signal - np.mean(signal)
    signal = hilbert(signal)
    signal = np.abs(signal)
    signal = moving_avg(signal, window_size)
    signal = normalize(signal)
    return pd.DataFrame({'value': signal})


if __name__ == '__main__':
    import os 
    print(os.getcwd())
    # Movement
    ## Polar
    df_polar_move_acc = pd.read_csv('Data/01_unified_data/ruch/polar_acc.csv')
    procesing_using_hilbert(df_polar_move_acc, WINDOW_SIZE_POLAR).to_csv('Data/02_presynch_data/ruch/polar_acc.csv', index=False)

    ## Empatica
    df_empatica_move_acc = pd.read_csv('Data/01_unified_data/ruch/empatica_acc.csv')
    procesing_using_hilbert(df_empatica_move_acc, WINDOW_SIZE_EMPATICA).to_csv('Data/02_presynch_data/ruch/empatica_acc.csv', index=False)

    ## Samsung
    df_samsung_move_acc = pd.read_csv('Data/01_unified_data/ruch/samsung_acc.csv')
    procesing_using_hilbert(df_samsung_move_acc, WINDOW_SIZE_SAMSUNG).to_csv('Data/02_presynch_data/ruch/samsung_acc.csv', index=False)

    # Sitting
    ## Polar
    df_polar_sit_acc = pd.read_csv('Data/01_unified_data/siedzaco/polar_acc.csv')
    procesing_using_hilbert(df_polar_sit_acc, WINDOW_SIZE_POLAR).to_csv('Data/02_presynch_data/siedzaco/polar_acc.csv', index=False)

    ## Empatica
    df_empatica_sit_acc = pd.read_csv('Data/01_unified_data/siedzaco/empatica_acc.csv')
    procesing_using_hilbert(df_empatica_sit_acc, WINDOW_SIZE_EMPATICA).to_csv('Data/02_presynch_data/siedzaco/empatica_acc.csv', index=False)

    ## Samsung
    df_samsung_sit_acc = pd.read_csv('Data/01_unified_data/siedzaco/samsung_acc.csv')
    procesing_using_hilbert(df_samsung_sit_acc, WINDOW_SIZE_SAMSUNG).to_csv('Data/02_presynch_data/siedzaco/samsung_acc.csv', index=False)
