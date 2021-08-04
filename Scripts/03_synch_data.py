import sys
sys.path.append(".")

import pandas as pd
import numpy as np

from constants import *

def find_max_peak(signal, frequency):
    signal = first_minute(signal, frequency)
    id_max = np.argmax(signal)
    id = id_max/frequency
    return id

def first_minute(signal, frequency):
    return signal[: int(frequency*60)]

def find_shift(list_id):
    return min(list_id)

def calculate_shift(signal_polar, signal_samsung, signal_empatica):
    id_max_polar = find_max_peak(signal_polar, ACC_FREQ_POLAR)
    id_max_samsung = find_max_peak(signal_samsung, ACC_FREQ_SAMSUNG)
    id_max_empatica = find_max_peak(signal_empatica, ACC_FREQ_EMPATICA)
    shift = find_shift([id_max_polar, id_max_samsung, id_max_empatica])
    id_begin_polar = (id_max_polar - shift) * ACC_FREQ_POLAR
    id_begin_samsung = (id_max_samsung - shift) * ACC_FREQ_SAMSUNG
    id_begin_empatica = (id_max_empatica - shift) * ACC_FREQ_EMPATICA
    return id_begin_polar, id_begin_samsung, id_begin_empatica

def synchro_acc_signal(signal, frequency, id_begin):
    return signal[int(frequency*60 + np.floor(id_begin)) :] 

if __name__ == '__main__':
    ## Movement
    df_polar_move_acc = pd.read_csv('Data/02_presynch_data/ruch/polar_acc.csv')
    df_empatica_move_acc = pd.read_csv('Data/02_presynch_data/ruch/empatica_acc.csv')
    df_samsung_move_acc = pd.read_csv('Data/02_presynch_data/ruch/samsung_acc.csv')
    id_begin_polar, id_begin_samsung, id_begin_empatica = calculate_shift(df_polar_move_acc, df_samsung_move_acc, df_empatica_move_acc)
    synchro_acc_signal(df_polar_move_acc, ACC_FREQ_POLAR, id_begin_polar).to_csv('Data/03_synch_data/ruch/polar_acc.csv', index=False)
    synchro_acc_signal(df_samsung_move_acc, ACC_FREQ_SAMSUNG, id_begin_samsung).to_csv('Data/03_synch_data/ruch/samsung_acc.csv', index=False)
    synchro_acc_signal(df_empatica_move_acc, ACC_FREQ_EMPATICA, id_begin_empatica).to_csv('Data/03_synch_data/ruch/empatica_acc.csv', index=False)

    # Sitting
    df_polar_sit_acc = pd.read_csv('Data/02_presynch_data/siedzaco/polar_acc.csv')
    df_empatica_sit_acc = pd.read_csv('Data/02_presynch_data/siedzaco/empatica_acc.csv')
    df_samsung_sit_acc = pd.read_csv('Data/02_presynch_data/siedzaco/samsung_acc.csv')
    id_begin_polar, id_begin_samsung, id_begin_empatica = calculate_shift(df_polar_sit_acc, df_samsung_sit_acc, df_empatica_sit_acc)
    synchro_acc_signal(df_polar_sit_acc, ACC_FREQ_POLAR, id_begin_polar).to_csv('Data/03_synch_data/siedzaco/polar_acc.csv', index=False)
    synchro_acc_signal(df_samsung_sit_acc, ACC_FREQ_SAMSUNG, id_begin_samsung).to_csv('Data/03_synch_data/siedzaco/samsung_acc.csv', index=False)
    synchro_acc_signal(df_empatica_sit_acc, ACC_FREQ_EMPATICA, id_begin_empatica).to_csv('Data/03_synch_data/siedzaco/empatica_acc.csv', index=False)

    