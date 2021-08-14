import numpy as np
from constants import *

def normalize(signal):
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal))


def calculate_index_ppg(index, signal_acc, signal_ppg):
    return np.round(index/len(signal_acc) * len(signal_ppg))


def calculate_real_sampling_freq(
    df_empatica_acc,
    df_empatica_ppg,
    df_polar_acc,
    df_polar_ekg,
    df_samsung_acc,
    df_samsung_ppg
):
    id_start_empatica = calculate_index_ppg(ID_START_FIRST_SESSION_EMPATICA, df_empatica_acc, df_empatica_ppg)
    id_stop_empatica = calculate_index_ppg(ID_STOP_FIRST_SESSION_EMPATICA, df_empatica_acc, df_empatica_ppg)
    len_empatica = id_stop_empatica - id_start_empatica

    id_start_polar = calculate_index_ppg(ID_START_FIRST_SESSION_POLAR, df_polar_acc, df_polar_ekg)
    id_stop_polar = calculate_index_ppg(ID_STOP_FIRST_SESSION_POLAR, df_polar_acc, df_polar_ekg)
    len_polar = id_stop_polar - id_start_polar

    id_start_samsung = calculate_index_ppg(ID_START_FIRST_SESSION_SAMSUNG, df_samsung_acc, df_samsung_ppg)
    id_stop_samsung = calculate_index_ppg(ID_STOP_FIRST_SESSION_SAMSUNG, df_samsung_acc, df_samsung_ppg)
    len_samsung = id_stop_samsung - id_start_samsung

    freq_empatica = SAMPLING_FREQ_EMPATICA
    freq_polar = SAMPLING_FREQ_EMPATICA * (len_samsung-1) / (len_empatica-1)
    freq_samsung = SAMPLING_FREQ_EMPATICA * (len_polar-1) / (len_empatica-1)
    return freq_empatica, freq_polar, freq_samsung